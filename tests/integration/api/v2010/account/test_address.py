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


class AddressTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "city": "SF",
                "customer_name": "name",
                "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",
                "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",
                "friendly_name": null,
                "iso_country": "US",
                "postal_code": "94019",
                "region": "CA",
                "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "street": "4th",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts.get(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .addresses.get(sid="ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
