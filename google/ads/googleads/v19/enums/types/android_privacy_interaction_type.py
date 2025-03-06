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
    package="google.ads.googleads.v19.enums",
    marshal="google.ads.googleads.v19",
    manifest={
        "AndroidPrivacyInteractionTypeEnum",
    },
)


class AndroidPrivacyInteractionTypeEnum(proto.Message):
    r"""The interaction type enum for Android privacy shared key."""

    class AndroidPrivacyInteractionType(proto.Enum):
        r"""Enumerates interaction types

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                The value is unknown in this version.
            CLICK (2):
                The physical click interaction type.
            ENGAGED_VIEW (3):
                The 10 seconds engaged view interaction type.
            VIEW (4):
                The view (ad impression) interaction type.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICK = 2
        ENGAGED_VIEW = 3
        VIEW = 4


__all__ = tuple(sorted(__protobuf__.manifest))
