# -*- coding: utf-8 -*-
"""Identity Services Engine getSponsorGroupById data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7(object):
    """getSponsorGroupById request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorEaa0D7C339D152B688876C2E10F51Fe7, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "SponsorGroup": {
                "properties": {
                "autoNotification": {
                "type": "boolean"
                },
                "createPermissions": {
                "properties": {
                "canCreateRandomAccounts": {
                "type": "boolean"
                },
                "canImportMultipleAccounts": {
                "type": "boolean"
                },
                "canSetFutureStartDate": {
                "type": "boolean"
                },
                "canSpecifyUsernamePrefix": {
                "type": "boolean"
                },
                "importBatchSizeLimit": {
                "type": "integer"
                },
                "randomBatchSizeLimit": {
                "type": "integer"
                },
                "startDateFutureLimitDays": {
                "type": "integer"
                }
                },
                "required": [
                "canImportMultipleAccounts",
                "importBatchSizeLimit",
                "canCreateRandomAccounts",
                "randomBatchSizeLimit",
                "canSpecifyUsernamePrefix",
                "canSetFutureStartDate",
                "startDateFutureLimitDays"
                ],
                "type": "object"
                },
                "description":
                 {
                "type": "string"
                },
                "guestTypes": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "id": {
                "type": "string"
                },
                "isDefaultGroup": {
                "type": "boolean"
                },
                "isEnabled": {
                "type": "boolean"
                },
                "link": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "required": [
                "rel",
                "href",
                "type"
                ],
                "type": "object"
                },
                "locations": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "managePermission": {
                "type": "string"
                },
                "memberGroups": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "name": {
                "type": "string"
                },
                "otherPermissions": {
                "properties": {
                "canAccessViaRest": {
                "type": "boolean"
                },
                "canApproveSelfregGuests": {
                "type": "boolean"
                },
                "canDeleteGuestAccounts": {
                "type": "boolean"
                },
                "canExtendGuestAccounts": {
                "type": "boolean"
                },
                "canReinstateSuspendedAccounts": {
                "type": "boolean"
                },
                "canResetGuestPasswords": {
                "type": "boolean"
                },
                "canSendSmsNotifications": {
                "type": "boolean"
                },
                "canSuspendGuestAccounts": {
                "type": "boolean"
                },
                "canUpdateGuestContactInfo": {
                "type": "boolean"
                },
                "canViewGuestPasswords": {
                "type": "boolean"
                },
                "limitApprovalToSponsorsGuests": {
                "type": "boolean"
                },
                "requireSuspensionReason": {
                "type": "boolean"
                }
                },
                "required": [
                "canUpdateGuestContactInfo",
                "canViewGuestPasswords",
                "canSendSmsNotifications",
                "canResetGuestPasswords",
                "canExtendGuestAccounts",
                "canDeleteGuestAccounts",
                "canSuspendGuestAccounts",
                "requireSuspensionReason",
                "canReinstateSuspendedAccounts",
                "canApproveSelfregGuests",
                "limitApprovalToSponsorsGuests",
                "canAccessViaRest"
                ],
                "type": "object"
                }
                },
                "type": "object"
                }
                },
                "required": [
                "SponsorGroup"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
