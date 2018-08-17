import logging

from django import http
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import View

from api import models, telnet


LOGGER = logging.getLogger(__name__)


class ListCommands(View):
    def get(self, request):
        all_commands = models.Command.objects.all()
        return http.JsonResponse({
            'commands': [{
                'code': command.denon_code,
                'name': command.readable_name,
                'description': command.description,
                'queryable': command.queryable,
                'icon': command.icon_code,
                'self': request.build_absolute_uri(reverse('api:command', kwargs={'command_code': command.denon_code})),
            } for command in all_commands]
        })


class CommandDetail(View):
    def get(self, request, command_code):
        command = get_object_or_404(models.Command, denon_code=command_code.upper())
        command_parameters = models.Parameter.objects.filter(command=command)
        return http.JsonResponse({
            'code': command.denon_code,
            'name': command.readable_name,
            'description': command.description,
            'queryable': command.queryable,
            'icon': command.icon_code,
            'parameters': [{
                'code': parameter.denon_code,
                'name': parameter.readable_name,
                'description': parameter.description,
                'icon': parameter.icon_code,
                'url': request.build_absolute_uri(reverse('api:parameter', kwargs={
                    'command_code': command.denon_code,
                    'parameter_code': parameter.denon_code,
                }))
            } for parameter in command_parameters],
            'self': request.build_absolute_uri(reverse('api:command', kwargs={'command_code': command.denon_code})),
        })


class CommandStatus(View):
    def get(self, request, command_code):
        command = get_object_or_404(models.Command, denon_code=command_code.upper())
        return http.HttpResponse(telnet.send_telnet_command(f'{command.denon_code}?'))


class ParameterDetail(View):
    def get(self, request, command_code, parameter_code):
        parameter = get_object_or_404(
            models.Parameter,
            command__denon_code=command_code.upper(),
            denon_code=parameter_code.upper()
        )

        return http.JsonResponse({
            'code': parameter.denon_code,
            'name': parameter.readable_name,
            'description': parameter.description,
            'icon': parameter.icon_code,
            'command': {
                'code': parameter.command.denon_code,
                'name': parameter.command.readable_name,
                'description': parameter.command.description,
                'queryable': parameter.command.queryable,
                'icon': parameter.command.icon_code,
                'url': request.build_absolute_uri(reverse('api:command', kwargs={'command_code': parameter.command.denon_code})),
            },
            'self': request.build_absolute_uri(reverse('api:parameter', kwargs={
                'command_code': parameter.command.denon_code,
                'parameter_code': parameter.denon_code,
            }))
        })


class Execute(View):
    def get(self, request, command_code, parameter_code):
        command = get_object_or_404(models.Command, denon_code=command_code.upper())
        parameter = get_object_or_404(models.Parameter, denon_code=parameter_code.upper(), command__denon_code=command_code.upper())

        return http.HttpResponse(telnet.send_telnet_command(f'{command.denon_code}{parameter.denon_code}'))
