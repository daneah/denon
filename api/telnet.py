import logging
import telnetlib

from django.conf import settings


LOGGER = logging.getLogger(__name__)


def send_telnet_command(command: str, wait_for_response=True) -> str:
    response = b''

    LOGGER.debug('Initiating connection to receiver...')
    with telnetlib.Telnet(host=settings.DENON_IP_ADDRESS, port=23, timeout=2) as telnet:
        LOGGER.debug(f'Sending {command} to receiver...')
        telnet.write(command.upper().encode('ascii') + b'\r')

        if wait_for_response:
            LOGGER.debug('Reading response from receiver...')
            response = telnet.read_some()

        return response.decode('ascii')
