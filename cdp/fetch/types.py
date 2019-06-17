'''
DO NOT EDIT THIS FILE

This file is generated from the CDP definitions. If you need to make changes,
edit the generator and regenerate all of the modules.

Domain: fetch
Experimental: True
'''

from dataclasses import dataclass, field
import typing

from ..network import types as network


class RequestId(str):
    '''
    Unique request identifier.
    '''
    @classmethod
    def from_response(cls, response):
        return cls(response)

    def __repr__(self):
        return 'RequestId({})'.format(str.__repr__(self))



class RequestStage:
    '''
    Stages of the request to handle. Request will intercept before the request is
    sent. Response will intercept after the response is received (but before response
    body is received.
    '''
    REQUEST = "Request"
    RESPONSE = "Response"


@dataclass
class RequestPattern:
    #: Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is
    #: backslash. Omitting is equivalent to "*".
    url_pattern: str

    #: If set, only requests for matching resource types will be intercepted.
    resource_type: network.ResourceType

    #: Stage at wich to begin intercepting requests. Default is Request.
    request_stage: RequestStage

    @classmethod
    def from_response(cls, response):
        return cls(
            url_pattern=str(response.get('urlPattern')),
            resource_type=network.ResourceType.from_response(response.get('resourceType')),
            request_stage=RequestStage.from_response(response.get('requestStage')),
        )


@dataclass
class HeaderEntry:
    '''
    Response HTTP header entry
    '''
    name: str

    value: str

    @classmethod
    def from_response(cls, response):
        return cls(
            name=str(response.get('name')),
            value=str(response.get('value')),
        )


@dataclass
class AuthChallenge:
    '''
    Authorization challenge for HTTP status code 401 or 407.
    '''
    #: Source of the authentication challenge.
    source: str

    #: Origin of the challenger.
    origin: str

    #: The authentication scheme used, such as basic or digest
    scheme: str

    #: The realm of the challenge. May be empty.
    realm: str

    @classmethod
    def from_response(cls, response):
        return cls(
            source=str(response.get('source')),
            origin=str(response.get('origin')),
            scheme=str(response.get('scheme')),
            realm=str(response.get('realm')),
        )


@dataclass
class AuthChallengeResponse:
    '''
    Response to an AuthChallenge.
    '''
    #: The decision on what to do in response to the authorization challenge.  Default means
    #: deferring to the default behavior of the net stack, which will likely either the Cancel
    #: authentication or display a popup dialog box.
    response: str

    #: The username to provide, possibly empty. Should only be set if response is
    #: ProvideCredentials.
    username: str

    #: The password to provide, possibly empty. Should only be set if response is
    #: ProvideCredentials.
    password: str

    @classmethod
    def from_response(cls, response):
        return cls(
            response=str(response.get('response')),
            username=str(response.get('username')),
            password=str(response.get('password')),
        )
