# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: DeviceAccess (experimental)

from __future__ import annotations
from cdp.util import event_class, T_JSON_DICT
from dataclasses import dataclass
import enum
import typing


class RequestId(str):
    '''
    Device request id.
    '''
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> RequestId:
        return cls(json)

    def __repr__(self):
        return 'RequestId({})'.format(super().__repr__())


class DeviceId(str):
    '''
    A device id.
    '''
    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> DeviceId:
        return cls(json)

    def __repr__(self):
        return 'DeviceId({})'.format(super().__repr__())


@dataclass
class PromptDevice:
    '''
    Device information displayed in a user prompt to select a device.
    '''
    id_: DeviceId

    #: Display name as it appears in a device request user prompt.
    name: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['id'] = self.id_.to_json()
        json['name'] = self.name
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PromptDevice:
        return cls(
            id_=DeviceId.from_json(json['id']),
            name=str(json['name']),
        )


def enable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enable events in this domain.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'DeviceAccess.enable',
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disable events in this domain.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'DeviceAccess.disable',
    }
    json = yield cmd_dict


def select_prompt(
        id_: RequestId,
        device_id: DeviceId
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Select a device in response to a DeviceAccess.deviceRequestPrompted event.

    :param id_:
    :param device_id:
    '''
    params: T_JSON_DICT = dict()
    params['id'] = id_.to_json()
    params['deviceId'] = device_id.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'DeviceAccess.selectPrompt',
        'params': params,
    }
    json = yield cmd_dict


def cancel_prompt(
        id_: RequestId
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Cancel a prompt in response to a DeviceAccess.deviceRequestPrompted event.

    :param id_:
    '''
    params: T_JSON_DICT = dict()
    params['id'] = id_.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'DeviceAccess.cancelPrompt',
        'params': params,
    }
    json = yield cmd_dict


@event_class('DeviceAccess.deviceRequestPrompted')
@dataclass
class DeviceRequestPrompted:
    '''
    A device request opened a user prompt to select a device. Respond with the
    selectPrompt or cancelPrompt command.
    '''
    id_: RequestId
    devices: typing.List[PromptDevice]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> DeviceRequestPrompted:
        return cls(
            id_=RequestId.from_json(json['id']),
            devices=[PromptDevice.from_json(i) for i in json['devices']]
        )
