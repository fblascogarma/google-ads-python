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
        "ValueRuleSetDimensionEnum",
    },
)


class ValueRuleSetDimensionEnum(proto.Message):
    r"""Container for enum describing possible dimensions of a
    conversion value rule set.

    """

    class ValueRuleSetDimension(proto.Enum):
        r"""Possible dimensions of a conversion value rule set."""

        UNSPECIFIED = 0
        UNKNOWN = 1
        GEO_LOCATION = 2
        DEVICE = 3
        AUDIENCE = 4
        NO_CONDITION = 5
        ITINERARY = 6


__all__ = tuple(sorted(__protobuf__.manifest))
