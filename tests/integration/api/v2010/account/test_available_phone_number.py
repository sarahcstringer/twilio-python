# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class AvailablePhoneNumberCountryTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "beta": null,
                "country": "United States",
                "country_code": "US",
                "subresource_uris": {
                    "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json",
                    "toll_free": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts.get(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .available_phone_numbers.get(country_code="US").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US.json'
        ))
