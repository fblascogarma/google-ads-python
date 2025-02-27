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
        "AssetAutomationTypeEnum",
    },
)


class AssetAutomationTypeEnum(proto.Message):
    r"""Container for enum describing the type of asset automation."""

    class AssetAutomationType(proto.Enum):
        r"""The type of asset automation."""

        UNSPECIFIED = 0
        UNKNOWN = 1
        TEXT_ASSET_AUTOMATION = 2
        GENERATE_VERTICAL_YOUTUBE_VIDEOS = 3
        GENERATE_SHORTER_YOUTUBE_VIDEOS = 4
        GENERATE_LANDING_PAGE_PREVIEW = 5
        GENERATE_ENHANCED_YOUTUBE_VIDEOS = 6


__all__ = tuple(sorted(__protobuf__.manifest))
