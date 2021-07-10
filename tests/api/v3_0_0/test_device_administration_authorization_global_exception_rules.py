# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI device_administration_authorization_global_exception_rules API fixtures and tests.

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


def is_valid_get_device_admin_policy_set_global_exception_rule_list(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_d407475db88f596390eab0a3e8c1d162_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_set_global_exception_rule_list(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.get_device_admin_policy_set_global_exception_rule_list(

    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_get_device_admin_policy_set_global_exception_rule_list(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_global_exception_rule_list(
            validator,
            get_device_admin_policy_set_global_exception_rule_list(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_set_global_exception_rule_list_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.get_device_admin_policy_set_global_exception_rule_list(

    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_get_device_admin_policy_set_global_exception_rule_list_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_global_exception_rule_list(
            validator,
            get_device_admin_policy_set_global_exception_rule_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_admin_policy_set_global_exception(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8558ade26d445251a45cc753f68d21bc_v3_0_0').validate(obj.response)
    return True


def create_device_admin_policy_set_global_exception(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.create_device_admin_policy_set_global_exception(
        active_validation=False,
        commands=['string'],
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        profile='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'}
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_create_device_admin_policy_set_global_exception(api, validator):
    try:
        assert is_valid_create_device_admin_policy_set_global_exception(
            validator,
            create_device_admin_policy_set_global_exception(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_device_admin_policy_set_global_exception_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.create_device_admin_policy_set_global_exception(
        active_validation=False,
        commands=None,
        link=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_create_device_admin_policy_set_global_exception_default(api, validator):
    try:
        assert is_valid_create_device_admin_policy_set_global_exception(
            validator,
            create_device_admin_policy_set_global_exception_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_reset_hit_counts_device_admin_global_exceptions(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_6b273ca0ffac58c3921f658152c03dbb_v3_0_0').validate(obj.response)
    return True


def reset_hit_counts_device_admin_global_exceptions(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.reset_hit_counts_device_admin_global_exceptions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_reset_hit_counts_device_admin_global_exceptions(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_global_exceptions(
            validator,
            reset_hit_counts_device_admin_global_exceptions(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def reset_hit_counts_device_admin_global_exceptions_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.reset_hit_counts_device_admin_global_exceptions(
        active_validation=False,
        payload=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_reset_hit_counts_device_admin_global_exceptions_default(api, validator):
    try:
        assert is_valid_reset_hit_counts_device_admin_global_exceptions(
            validator,
            reset_hit_counts_device_admin_global_exceptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_admin_policy_set_global_exception_by_rule_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_3a3d7e48a50d58a8a5d5720f9d55cf45_v3_0_0').validate(obj.response)
    return True


def get_device_admin_policy_set_global_exception_by_rule_id(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.get_device_admin_policy_set_global_exception_by_rule_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_get_device_admin_policy_set_global_exception_by_rule_id(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_global_exception_by_rule_id(
            validator,
            get_device_admin_policy_set_global_exception_by_rule_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_admin_policy_set_global_exception_by_rule_id_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.get_device_admin_policy_set_global_exception_by_rule_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_get_device_admin_policy_set_global_exception_by_rule_id_default(api, validator):
    try:
        assert is_valid_get_device_admin_policy_set_global_exception_by_rule_id(
            validator,
            get_device_admin_policy_set_global_exception_by_rule_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_put_device_admin_policy_set_global_exception_by_rule_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_28042265da96552991705623287a164c_v3_0_0').validate(obj.response)
    return True


def put_device_admin_policy_set_global_exception_by_rule_id(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.put_device_admin_policy_set_global_exception_by_rule_id(
        active_validation=False,
        commands=['string'],
        link={'href': 'string', 'rel': 'string', 'type': 'string'},
        payload=None,
        profile='string',
        rule={'condition': {'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}, 'description': 'string', 'id': 'string', 'name': 'string', 'attributeName': 'string', 'attributeValue': 'string', 'dictionaryName': 'string', 'dictionaryValue': 'string', 'operator': 'string', 'children': [{'conditionType': 'string', 'isNegate': True, 'link': {'href': 'string', 'rel': 'string', 'type': 'string'}}], 'datesRange': {'endDate': 'string', 'startDate': 'string'}, 'datesRangeException': {'endDate': 'string', 'startDate': 'string'}, 'hoursRange': {'endTime': 'string', 'startTime': 'string'}, 'hoursRangeException': {'endTime': 'string', 'startTime': 'string'}, 'weekDays': ['string'], 'weekDaysException': ['string']}, 'default': True, 'hitCounts': 0, 'id': 'string', 'name': 'string', 'rank': 0, 'state': 'string'},
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_put_device_admin_policy_set_global_exception_by_rule_id(api, validator):
    try:
        assert is_valid_put_device_admin_policy_set_global_exception_by_rule_id(
            validator,
            put_device_admin_policy_set_global_exception_by_rule_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def put_device_admin_policy_set_global_exception_by_rule_id_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.put_device_admin_policy_set_global_exception_by_rule_id(
        active_validation=False,
        rule_id='string',
        commands=None,
        link=None,
        payload=None,
        profile=None,
        rule=None
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_put_device_admin_policy_set_global_exception_by_rule_id_default(api, validator):
    try:
        assert is_valid_put_device_admin_policy_set_global_exception_by_rule_id(
            validator,
            put_device_admin_policy_set_global_exception_by_rule_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_admin_policyset_global_exception_by_rule_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_10281a20040d51a1ba61f4d210195e59_v3_0_0').validate(obj.response)
    return True


def delete_device_admin_policyset_global_exception_by_rule_id(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.delete_device_admin_policyset_global_exception_by_rule_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_delete_device_admin_policyset_global_exception_by_rule_id(api, validator):
    try:
        assert is_valid_delete_device_admin_policyset_global_exception_by_rule_id(
            validator,
            delete_device_admin_policyset_global_exception_by_rule_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_device_admin_policyset_global_exception_by_rule_id_default(api):
    endpoint_result = api.device_administration_authorization_global_exception_rules.delete_device_admin_policyset_global_exception_by_rule_id(
        rule_id='string'
    )
    return endpoint_result


@pytest.mark.device_administration_authorization_global_exception_rules
def test_delete_device_admin_policyset_global_exception_by_rule_id_default(api, validator):
    try:
        assert is_valid_delete_device_admin_policyset_global_exception_by_rule_id(
            validator,
            delete_device_admin_policyset_global_exception_by_rule_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
