# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI telemetry_information API fixtures and tests.

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


def is_valid_get_all_telemetry_information(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_8f1a8ae602c95ac08676391c374274f2_v3_0_0').validate(obj.response)
    return True


def get_all_telemetry_information(api):
    endpoint_result = api.telemetry_information.get_all_telemetry_information(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.telemetry_information
def test_get_all_telemetry_information(api, validator):
    try:
        assert is_valid_get_all_telemetry_information(
            validator,
            get_all_telemetry_information(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_telemetry_information_default(api):
    endpoint_result = api.telemetry_information.get_all_telemetry_information(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.telemetry_information
def test_get_all_telemetry_information_default(api, validator):
    try:
        assert is_valid_get_all_telemetry_information(
            validator,
            get_all_telemetry_information_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_telemetry_info_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_13891f52605b5f6481f6a99ec8a7e8e6_v3_0_0').validate(obj.response)
    return True


def get_telemetry_info_by_id(api):
    endpoint_result = api.telemetry_information.get_telemetry_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.telemetry_information
def test_get_telemetry_info_by_id(api, validator):
    try:
        assert is_valid_get_telemetry_info_by_id(
            validator,
            get_telemetry_info_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_telemetry_info_by_id_default(api):
    endpoint_result = api.telemetry_information.get_telemetry_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.telemetry_information
def test_get_telemetry_info_by_id_default(api, validator):
    try:
        assert is_valid_get_telemetry_info_by_id(
            validator,
            get_telemetry_info_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
