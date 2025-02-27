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
        "TrackingCodePageFormatEnum",
    },
)


class TrackingCodePageFormatEnum(proto.Message):
    r"""Container for enum describing the format of the web page
    where the tracking tag and snippet will be installed.

    """

    class TrackingCodePageFormat(proto.Enum):
        r"""The format of the web page where the tracking tag and snippet
        will be installed.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        HTML = 2
        AMP = 3


__all__ = tuple(sorted(__protobuf__.manifest))
