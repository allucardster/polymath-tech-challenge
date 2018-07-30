import collections
import requests
import xmltodict
from xmler import dict2xml
from xml.dom.minidom import parseString
import src.settings as settings

class EbayClient:
    """
    Allow to access into specific Ebay API endpoints
    """

    def _getApiAuthToken(self):
        """
        Get default api auth token
        """
        return settings.EBAY_API_AUTH_TOKEN

    def _getHeaders(self, callName):
        """
        Get default headers for any api calls
        """
        return {
            'X-EBAY-API-CALL-NAME': callName,
            'X-EBAY-API-APP-NAME': settings.EBAY_API_APP_NAME,
            'X-EBAY-API-CERT-NAME': settings.EBAY_API_CERT_NAME,
            'X-EBAY-API-DEV-NAME': settings.EBAY_API_DEV_NAME,
            'X-EBAY-API-SITEID': settings.EBAY_API_SITEID,
            'X-EBAY-API-COMPATIBILITY-LEVEL': settings.EBAY_API_COMPATIBILITY_LEVEL
        }

    def getAllCategories(self):
        """
        Retrieve all categories from Ebay
        """
        callName = 'GetCategories'
        url = settings.EBAY_API_URL
        headers = self._getHeaders(callName)
        body = {
            'GetCategoriesRequest': {
                '@attrs': { 'xmlns': 'urn:ebay:apis:eBLBaseComponents' },
                'RequesterCredentials': { 'eBayAuthToken': self._getApiAuthToken() },
                'CategorySiteID': '0',
                'DetailLevel': 'ReturnAll',
                'ViewAllNodes': 'true'
            }
        }
        data = f'<?xml version="1.0" encoding="UTF-8"?>{dict2xml(body)}'
        response = requests.post(url, headers=headers, data=data)
        payload = xmltodict.parse(response.content)
        
        if 'GetCategoriesResponse' in payload:
            for cat in payload['GetCategoriesResponse']['CategoryArray']['Category']:
                yield cat
        else:
            return []
