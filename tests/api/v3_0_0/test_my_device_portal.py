# -*- coding: utf-8 -*-
"""IdentityServicesEngineAPI my_device_portal API fixtures and tests.

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


def is_valid_get_all_my_device_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_90a71ccf29f05ee29af909b07bb9c754_v3_0_0').validate(obj.response)
    return True


def get_all_my_device_portal(api):
    endpoint_result = api.my_device_portal.get_all_my_device_portal(
        filter='value1,value2',
        filter_type='string',
        page=0,
        size=0,
        sortasc='string',
        sortdsc='string'
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_get_all_my_device_portal(api, validator):
    try:
        assert is_valid_get_all_my_device_portal(
            validator,
            get_all_my_device_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_all_my_device_portal_default(api):
    endpoint_result = api.my_device_portal.get_all_my_device_portal(
        filter=None,
        filter_type=None,
        page=None,
        size=None,
        sortasc=None,
        sortdsc=None
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_get_all_my_device_portal_default(api, validator):
    try:
        assert is_valid_get_all_my_device_portal(
            validator,
            get_all_my_device_portal_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_my_device_portal(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_e643a5ac8bca55f58ea8d6260c57eafe_v3_0_0').validate(obj.response)
    return True


def create_my_device_portal(api):
    endpoint_result = api.my_device_portal.create_my_device_portal(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string', 'availableSsids': []}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestToCreateAccounts': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireAccessCode': True, 'requireScrolling': True, 'displayFrequency': 'string'}, 'employeeChangePasswordSettings': {'allowEmployeeToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string'}}
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_create_my_device_portal(api, validator):
    try:
        assert is_valid_create_my_device_portal(
            validator,
            create_my_device_portal(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_my_device_portal_default(api):
    endpoint_result = api.my_device_portal.create_my_device_portal(
        active_validation=False,
        customizations=None,
        description=None,
        id=None,
        name=None,
        payload=None,
        portal_type=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_create_my_device_portal_default(api, validator):
    try:
        assert is_valid_create_my_device_portal(
            validator,
            create_my_device_portal_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_my_device_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_4bb3528d280652678f8e211b9e418e66_v3_0_0').validate(obj.response)
    return True


def get_my_device_portal_by_id(api):
    endpoint_result = api.my_device_portal.get_my_device_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_get_my_device_portal_by_id(api, validator):
    try:
        assert is_valid_get_my_device_portal_by_id(
            validator,
            get_my_device_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_my_device_portal_by_id_default(api):
    endpoint_result = api.my_device_portal.get_my_device_portal_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_get_my_device_portal_by_id_default(api, validator):
    try:
        assert is_valid_get_my_device_portal_by_id(
            validator,
            get_my_device_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_my_device_portal_by_id(json_schema_validate, obj):
    if not obj:
        return False
    assert hasattr(obj, 'headers')
    assert hasattr(obj, 'content')
    assert hasattr(obj, 'text')
    assert hasattr(obj, 'response')
    json_schema_validate('jsd_83079c64b769537ea7c586565f6ed2a2_v3_0_0').validate(obj.response)
    return True


def update_my_device_portal_by_id(api):
    endpoint_result = api.my_device_portal.update_my_device_portal_by_id(
        active_validation=False,
        customizations={'portalTheme': {'id': 'string', 'name': 'string', 'themeData': 'string'}, 'portalTweakSettings': {'bannerColor': 'string', 'bannerTextColor': 'string', 'pageBackgroundColor': 'string', 'pageLabelAndTextColor': 'string'}, 'language': {'viewLanguage': 'string'}, 'globalCustomizations': {'mobileLogoImage': {'data': 'string'}, 'desktopLogoImage': {'data': 'string'}, 'bannerImage': {'data': 'string'}, 'bannerTitle': 'string', 'contactText': 'string', 'footerElement': 'string'}, 'pageCustomizations': {'data': [{'key': 'string', 'value': 'string'}]}},
        description='string',
        id='string',
        name='string',
        payload=None,
        portal_type='string',
        settings={'portalSettings': {'httpsPort': 0, 'allowedInterfaces': ['string'], 'certificateGroupTag': 'string', 'endpointIdentityGroup': 'string', 'fqdn': 'string', 'authenticationMethod': 'string', 'idleTimeout': 0, 'displayLang': 'string', 'fallbackLanguage': 'string', 'alwaysUsedLanguage': 'string', 'availableSsids': []}, 'loginPageSettings': {'requireAccessCode': True, 'maxFailedAttemptsBeforeRateLimit': 0, 'timeBetweenLoginsDuringRateLimit': 0, 'includeAup': True, 'aupDisplay': 'string', 'requireAupAcceptance': True, 'requireAupScrolling': True, 'allowGuestToCreateAccounts': True, 'allowGuestToChangePassword': True, 'allowAlternateGuestPortal': True, 'allowGuestToUseSocialAccounts': True, 'allowShowGuestForm': True, 'socialConfigs': []}, 'aupSettings': {'includeAup': True, 'useDiffAupForEmployees': True, 'skipAupForEmployees': True, 'requireAccessCode': True, 'requireScrolling': True, 'displayFrequency': 'string'}, 'employeeChangePasswordSettings': {'allowEmployeeToChangePwd': True}, 'postLoginBannerSettings': {'includePostAccessBanner': True}, 'supportInfoSettings': {'includeSupportInfoPage': True, 'includeMacAddr': True, 'includeIpAddress': True, 'includeBrowserUserAgent': True, 'includePolicyServer': True, 'includeFailureCode': True, 'emptyFieldDisplay': 'string'}}
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_update_my_device_portal_by_id(api, validator):
    try:
        assert is_valid_update_my_device_portal_by_id(
            validator,
            update_my_device_portal_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_my_device_portal_by_id_default(api):
    endpoint_result = api.my_device_portal.update_my_device_portal_by_id(
        active_validation=False,
        id='string',
        customizations=None,
        description=None,
        name=None,
        payload=None,
        portal_type=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.my_device_portal
def test_update_my_device_portal_by_id_default(api, validator):
    try:
        assert is_valid_update_my_device_portal_by_id(
            validator,
            update_my_device_portal_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
