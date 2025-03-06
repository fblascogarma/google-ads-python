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
        "LegacyAppInstallAdAppStoreEnum",
    },
)


class LegacyAppInstallAdAppStoreEnum(proto.Message):
    r"""Container for enum describing app store type in a legacy app
    install ad.

    """

    class LegacyAppInstallAdAppStore(proto.Enum):
        r"""App store type in a legacy app install ad.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            APPLE_APP_STORE (2):
                Apple iTunes.
            GOOGLE_PLAY (3):
                Google Play.
            WINDOWS_STORE (4):
                Windows Store.
            WINDOWS_PHONE_STORE (5):
                Windows Phone Store.
            CN_APP_STORE (6):
                The app is hosted in a Chinese app store.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLE_APP_STORE = 2
        GOOGLE_PLAY = 3
        WINDOWS_STORE = 4
        WINDOWS_PHONE_STORE = 5
        CN_APP_STORE = 6


__all__ = tuple(sorted(__protobuf__.manifest))
