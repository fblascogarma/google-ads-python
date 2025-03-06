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
        "FlightPlaceholderFieldEnum",
    },
)


class FlightPlaceholderFieldEnum(proto.Message):
    r"""Values for Flight placeholder fields.
    For more information about dynamic remarketing feeds, see
    https://support.google.com/google-ads/answer/6053288.

    """

    class FlightPlaceholderField(proto.Enum):
        r"""Possible values for Flight placeholder fields.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            DESTINATION_ID (2):
                Data Type: STRING. Required. Destination id.
                Example: PAR, LON. For feed items that only have
                destination id, destination id must be a unique
                key. For feed items that have both destination
                id and origin id, then the combination must be a
                unique key.
            ORIGIN_ID (3):
                Data Type: STRING. Origin id. Example: PAR,
                LON. Optional. Combination of destination id and
                origin id must be unique per offer.
            FLIGHT_DESCRIPTION (4):
                Data Type: STRING. Required. Main headline
                with product name to be shown in dynamic ad.
            ORIGIN_NAME (5):
                Data Type: STRING. Shorter names are
                recommended.
            DESTINATION_NAME (6):
                Data Type: STRING. Shorter names are
                recommended.
            FLIGHT_PRICE (7):
                Data Type: STRING. Price to be shown in the
                ad. Example: "100.00 USD".
            FORMATTED_PRICE (8):
                Data Type: STRING. Formatted price to be
                shown in the ad. Example: "Starting at $100.00
                USD", "$80 - $100".
            FLIGHT_SALE_PRICE (9):
                Data Type: STRING. Sale price to be shown in
                the ad. Example: "80.00 USD".
            FORMATTED_SALE_PRICE (10):
                Data Type: STRING. Formatted sale price to be
                shown in the ad. Example: "On sale for $80.00",
                "$60 - $80".
            IMAGE_URL (11):
                Data Type: URL. Image to be displayed in the
                ad.
            FINAL_URLS (12):
                Data Type: URL_LIST. Required. Final URLs for the ad when
                using Upgraded URLs. User will be redirected to these URLs
                when they click on an ad, or when they click on a specific
                flight for ads that show multiple flights.
            FINAL_MOBILE_URLS (13):
                Data Type: URL_LIST. Final mobile URLs for the ad when using
                Upgraded URLs.
            TRACKING_URL (14):
                Data Type: URL. Tracking template for the ad
                when using Upgraded URLs.
            ANDROID_APP_LINK (15):
                Data Type: STRING. Android app link. Must be formatted as:
                android-app://{package_id}/{scheme}/{host_path}. The
                components are defined as follows: package_id: app ID as
                specified in Google Play. scheme: the scheme to pass to the
                application. Can be HTTP, or a custom scheme. host_path:
                identifies the specific content within your application.
            SIMILAR_DESTINATION_IDS (16):
                Data Type: STRING_LIST. List of recommended destination IDs
                to show together with this item.
            IOS_APP_LINK (17):
                Data Type: STRING. iOS app link.
            IOS_APP_STORE_ID (18):
                Data Type: INT64. iOS app store ID.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        DESTINATION_ID = 2
        ORIGIN_ID = 3
        FLIGHT_DESCRIPTION = 4
        ORIGIN_NAME = 5
        DESTINATION_NAME = 6
        FLIGHT_PRICE = 7
        FORMATTED_PRICE = 8
        FLIGHT_SALE_PRICE = 9
        FORMATTED_SALE_PRICE = 10
        IMAGE_URL = 11
        FINAL_URLS = 12
        FINAL_MOBILE_URLS = 13
        TRACKING_URL = 14
        ANDROID_APP_LINK = 15
        SIMILAR_DESTINATION_IDS = 16
        IOS_APP_LINK = 17
        IOS_APP_STORE_ID = 18


__all__ = tuple(sorted(__protobuf__.manifest))
