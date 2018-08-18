import atexit
import logging
import telnetlib

from django.conf import settings


LOGGER = logging.getLogger(__name__)


DENON = telnetlib.Telnet(host=settings.DENON_IP_ADDRESS, port=23, timeout=2)
atexit.register(DENON.close)


def send_telnet_command(command: str, wait_for_response=True) -> str:
    response = b''

    LOGGER.debug(f'Sending {command} to receiver...')
    DENON.write(command.upper().encode('ascii') + b'\r')

    if wait_for_response:
        LOGGER.debug('Reading response from receiver...')
        response = DENON.read_some()

    return response.decode('ascii')
