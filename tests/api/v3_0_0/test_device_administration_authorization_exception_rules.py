# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_authorization_exception_rules API fixtures and tests.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from ciscoisesdk.exceptions import MalformedRequest
from tests.environment import IDENTITY_SERVICES_ENGINE_VERSION

pytestmark = pytest.mark.skipif(IDENTITY_SERVICES_ENGINE_VERSION != '3.0.0', reason='version does not match')


def is_valid_get_all_device_admin_local_exception(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_bba3187f0be4563aa8b6ff5931a123e7_v3_0_0').validate(obj.response)
    return True


def get_all_device_admin_local_exception(api):
    endpoint_result = api.device_administration_authorization_exception_rules.get_all_device_admin_local_exception(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_get_all_device_admin_local_exception(api, validator):
    try:
        assert is_valid_get_all_device_admin_local_exception(
            validator,
            get_all_device_admin_local_exception(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_device_admin_local_exception_default(api):
    endpoint_result = api.device_administration_authorization_exception_rules.get_all_device_admin_local_exception(
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_get_all_device_admin_local_exception_default(api, validator):
    try:
        assert is_valid_get_all_device_admin_local_exception(
            validator,
            get_all_device_admin_local_exception_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_local_exception(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_12905ebcdc835e9b8d6844c1da6cf252_v3_0_0').validate(obj.response)
    return True


def create_device_admin_local_exception(api):
    endpoint_result = api.device_administration_authorization_exception_rules.create_device_admin_local_exception(
        active_validation=False,
        commands=['string'],
        payload=None,
        policy_id='string',
        profile='string',
        rule={'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_create_device_admin_local_exception(api, validator):
    try:
        assert is_valid_create_device_admin_local_exception(
            validator,
            create_device_admin_local_exception(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_local_exception_default(api):
    endpoint_result = api.device_administration_authorization_exception_rules.create_device_admin_local_exception(
        active_validation=False,
        policy_id='string',
        commands=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_create_device_admin_local_exception_default(api, validator):
    try:
        assert is_valid_create_device_admin_local_exception(
            validator,
            create_device_admin_local_exception_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_local_exception_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d8e470a4ef6a58b3b21f9adbbdcc7a46_v3_0_0').validate(obj.response)
    return True


def get_device_admin_local_exception_by_id(api):
    endpoint_result = api.device_administration_authorization_exception_rules.get_device_admin_local_exception_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_get_device_admin_local_exception_by_id(api, validator):
    try:
        assert is_valid_get_device_admin_local_exception_by_id(
            validator,
            get_device_admin_local_exception_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_local_exception_by_id_default(api):
    endpoint_result = api.device_administration_authorization_exception_rules.get_device_admin_local_exception_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_get_device_admin_local_exception_by_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_local_exception_by_id(
            validator,
            get_device_admin_local_exception_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_admin_local_exception_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_a87d60d590485830aed781bfb15b5c95_v3_0_0').validate(obj.response)
    return True


def update_device_admin_local_exception_by_id(api):
    endpoint_result = api.device_administration_authorization_exception_rules.update_device_admin_local_exception_by_id(
        active_validation=False,
        commands=['string'],
        id='string',
        payload=None,
        policy_id='string',
        profile='string',
        rule={'id': 'string', 'name': 'string', 'description': 'string', 'hitCounts': 0, 'rank': 0, 'state': 'string', 'default': True, 'condition': {'conditionType': 'string', 'isNegate': True, 'name': 'string', 'id': 'string', 'description': 'string', 'dictionaryName': 'string', 'attributeName': 'string', 'attributeId': 'string', 'operator': 'string', 'dictionaryValue': 'string', 'attributeValue': 'string', 'children': [{'conditionType': 'string', 'isNegate': True}], 'hoursRange': {'startTime': 'string', 'endTime': 'string'}, 'hoursRangeException': {'startTime': 'string', 'endTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string'], 'datesRange': {'startDate': 'string', 'endDate': 'string'}, 'datesRangeException': {'startDate': 'string', 'endDate': 'string'}}}
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_update_device_admin_local_exception_by_id(api, validator):
    try:
        assert is_valid_update_device_admin_local_exception_by_id(
            validator,
            update_device_admin_local_exception_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_device_admin_local_exception_by_id_default(api):
    endpoint_result = api.device_administration_authorization_exception_rules.update_device_admin_local_exception_by_id(
        active_validation=False,
        id='string',
        policy_id='string',
        commands=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_update_device_admin_local_exception_by_id_default(api, validator):
    try:
        assert is_valid_update_device_admin_local_exception_by_id(
            validator,
            update_device_admin_local_exception_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_local_exception_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_20c7d6bb4abf53f6aa2f40b6986f58a9_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_local_exception_by_id(api):
    endpoint_result = api.device_administration_authorization_exception_rules.delete_device_admin_local_exception_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_delete_device_admin_local_exception_by_id(api, validator):
    try:
        assert is_valid_delete_device_admin_local_exception_by_id(
            validator,
            delete_device_admin_local_exception_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_local_exception_by_id_default(api):
    endpoint_result = api.device_administration_authorization_exception_rules.delete_device_admin_local_exception_by_id(
        id='string',
        policy_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_exception_rules
def test_delete_device_admin_local_exception_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_local_exception_by_id(
            validator,
            delete_device_admin_local_exception_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
