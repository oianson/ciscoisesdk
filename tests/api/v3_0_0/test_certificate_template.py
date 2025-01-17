# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI certificate_template API fixtures and tests.

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


def is_valid_get_all_certificate_template(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_c87977b21b8f5d64852a8b6a5527928d_v3_0_0').validate(obj.response)
    return True


def get_all_certificate_template(api):
    endpoint_result = api.certificate_template.get_all_certificate_template(
        page=0,
        size=0
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_all_certificate_template(api, validator):
    try:
        assert is_valid_get_all_certificate_template(
            validator,
            get_all_certificate_template(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_certificate_template_default(api):
    endpoint_result = api.certificate_template.get_all_certificate_template(
        page=None,
        size=None
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_all_certificate_template_default(api, validator):
    try:
        assert is_valid_get_all_certificate_template(
            validator,
            get_all_certificate_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_certificate_template_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e9e38cdf5bcb5c018b7f10f1d0864215_v3_0_0').validate(obj.response)
    return True


def get_certificate_template_by_id(api):
    endpoint_result = api.certificate_template.get_certificate_template_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_certificate_template_by_id(api, validator):
    try:
        assert is_valid_get_certificate_template_by_id(
            validator,
            get_certificate_template_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_certificate_template_by_id_default(api):
    endpoint_result = api.certificate_template.get_certificate_template_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_certificate_template_by_id_default(api, validator):
    try:
        assert is_valid_get_certificate_template_by_id(
            validator,
            get_certificate_template_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_certificate_template_by_name(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_40ef36cc17a55cb38bf1fe2973dcc312_v3_0_0').validate(obj.response)
    return True


def get_certificate_template_by_name(api):
    endpoint_result = api.certificate_template.get_certificate_template_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_certificate_template_by_name(api, validator):
    try:
        assert is_valid_get_certificate_template_by_name(
            validator,
            get_certificate_template_by_name(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_certificate_template_by_name_default(api):
    endpoint_result = api.certificate_template.get_certificate_template_by_name(
        name='string'
    )
    return endpoint_result


@pytest.mark.certificate_template
def test_get_certificate_template_by_name_default(api, validator):
    try:
        assert is_valid_get_certificate_template_by_name(
            validator,
            get_certificate_template_by_name_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
