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


class ApplicationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2010-04-01",
                "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",
                "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",
                "friendly_name": "Application Friendly Name",
                "message_status_callback": "http://www.example.com/sms-status-callback",
                "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sms_fallback_method": "GET",
                "sms_fallback_url": "http://www.example.com/sms-fallback",
                "sms_method": "GET",
                "sms_status_callback": "http://www.example.com/sms-status-callback",
                "sms_url": "http://example.com",
                "status_callback": "http://example.com",
                "status_callback_method": "GET",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "voice_caller_id_lookup": false,
                "voice_fallback_method": "GET",
                "voice_fallback_url": "http://www.example.com/voice-callback",
                "voice_method": "GET",
                "voice_url": "http://example.com"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts.get(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .applications.get(sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
