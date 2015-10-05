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


class ParticipantTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-05-13T23:03:12Z",
                "duration": 685,
                "end_time": "2015-05-13T23:14:40Z",
                "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "2015-05-13T23:03:15Z",
                "status": "disconnected",
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        self.twilio.conversations.v1.conversations.get(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .participants.get(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        ))
