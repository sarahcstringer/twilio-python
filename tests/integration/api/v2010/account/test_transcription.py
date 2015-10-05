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


class TranscriptionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "date_created": "Sun, 13 Feb 2011 02:12:08 +0000",
                "date_updated": "Sun, 13 Feb 2011 02:30:01 +0000",
                "duration": "1",
                "price": "-0.05000",
                "recording_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "failed",
                "transcription_text": "(blank)",
                "type": "fast",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts.get(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .transcriptions.get(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json'
        ))
