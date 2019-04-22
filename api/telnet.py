import atexit
import logging
import telnetlib

from django.conf import settings


LOGGER = logging.getLogger(__name__)


def send_telnet_command(command: str, wait_for_response=True) -> str:
    response = b''

    LOGGER.debug(f'Sending {command} to receiver...')
    with telnetlib.Telnet(settings.DENON_IP_ADDRESS, port=23, timeout=2) as denon:
        denon.write(command.upper().encode('ascii') + b'\r')

        if wait_for_response:
            LOGGER.debug('Reading response from receiver...')
            response = denon.read_some()

    return response.decode('ascii')
