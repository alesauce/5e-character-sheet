import requests
from enum import Enum
import logging


SRD_5E_API_BASE_URL = "https://www.dnd5eapi.co/api/"
ACCEPTABLE_STATUS_CODES = [200]
logger = logging.getLogger(__name__)


class SrdApiBaseEndpoints(Enum):
    RACES = "races"
    CLASSES = "classes"
    SPELLS = "spells"


class SrdApiReader:
    def __init__(self) -> None:
        pass

    def get_base_endpoint(self, base_endpoint:SrdApiBaseEndpoints):
        logger.info(f"Requesting from base endpoint: {base_endpoint.value}")
        target_endpoint = SRD_5E_API_BASE_URL + base_endpoint.value
        headers = {'Accept': 'application/json'}
        response = requests.get(target_endpoint, headers)
        if response.status_code not in ACCEPTABLE_STATUS_CODES:
            logger.exception("that's not good, lol")
        response_data = response.json()
        return response_data["results"]
