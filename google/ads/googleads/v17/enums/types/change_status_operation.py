# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v17.enums",
    marshal="google.ads.googleads.v17",
    manifest={
        "ChangeStatusOperationEnum",
    },
)


class ChangeStatusOperationEnum(proto.Message):
    r"""Container for enum describing operations for the ChangeStatus
    resource.

    """

    class ChangeStatusOperation(proto.Enum):
        r"""Status of the changed resource

        Values:
            UNSPECIFIED (0):
                No value has been specified.
            UNKNOWN (1):
                Used for return value only. Represents an
                unclassified resource unknown in this version.
            ADDED (2):
                The resource was created.
            CHANGED (3):
                The resource was modified.
            REMOVED (4):
                The resource was removed.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        ADDED = 2
        CHANGED = 3
        REMOVED = 4


__all__ = tuple(sorted(__protobuf__.manifest))
