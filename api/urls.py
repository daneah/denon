from django.urls import path, include

from api import views


app_name = 'api'


urlpatterns = [
    path('', views.ListCommands.as_view(), name='commands'),
    path('command/<str:command_code>/', include([
        path('', views.CommandDetail.as_view(), name='command'),
        path('query/', views.CommandStatus.as_view(), name='command_status'),
        path('parameter/<str:parameter_code>/', include([
            path('', views.ParameterDetail.as_view(), name='parameter'),
            path('call/', views.Execute.as_view(), name='execute'),
        ])),
    ])),
]
