#!/usr/bin/env python
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example is to get impact metrics for a custom budget; 

This is for users who want to input a different budget than the recommended one.

Example uses: 
1) Performance Max for the campaign type
2) United States for the geo targeting 
3) Maximize Conversions Value for the bidding strategy.

To get budget recommendations, run get_budget_recommendations.py.
"""


import argparse
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def main(client, customer_id, budget_amount_user):
    """The main method that creates all necessary entities for the example.

    Args:
        client: an initialized GoogleAdsClient instance.
        customer_id: a client customer ID.
        budget_amount_user: a budget amount (not in micros) advertiser wants to use.
    """
    # Start Recommendation Service.
    reco_service = client.get_service("RecommendationService")

    # Build Request.
    reco_request = client.get_type("GenerateRecommendationsRequest")

    reco_request.customer_id = customer_id
    reco_request.recommendation_types = ["CAMPAIGN_BUDGET"]
    reco_request.advertising_channel_type = "PERFORMANCE_MAX"
    reco_request.bidding_info.bidding_strategy_type = "MAXIMIZE_CONVERSION_VALUE"
    reco_request.positive_locations_ids = [2840]  # 2840 is for United States
    reco_request.asset_group_info = [{ "final_url": "https://www.your-company.com/" }]
    reco_request.budget_info.current_budget = round((budget_amount_user*1000000), 2)  # because current_budget takes micros

    # Send Request.
    results = reco_service.generate_recommendations(reco_request)

    recommendations = results.recommendations

    budget_impact_metrics = []    # List to store impact metrics for user input budget

    for reco in recommendations:
        if hasattr(reco, 'campaign_budget_recommendation'):
            campaign_budget_reco = reco.campaign_budget_recommendation

            if hasattr(campaign_budget_reco, 'budget_options'):
                for budget_option in campaign_budget_reco.budget_options:
                    if hasattr(budget_option, 'impact') and hasattr(budget_option, 'budget_amount_micros'): # Check if both exist
                        impact = budget_option.impact
                        budget_amount = budget_option.budget_amount_micros

                        if hasattr(impact, 'potential_metrics'):
                            if budget_amount/1000000 == budget_amount_user:
                                budget_data = {
                                    "budget_amount": round((budget_amount/1000000), 2),
                                    "potential_metrics": impact.potential_metrics
                                }
                                budget_impact_metrics.append(budget_data)
                        else:
                            print("potential_metrics not found for this budget option.")
                    else:
                        print("impact or budget_amount_micros not found for this budget option.")
            else:
                print("budget_options not found for this recommendation.")
        else:
            print("campaign_budget_recommendation not found for this recommendation.")

    print("budget_impact_metrics:")
    print(budget_impact_metrics)
    """
    budget_impact_metrics:
    [{'budget_amount': 100.0, 'potential_metrics': cost_micros: 700000000
    conversions: 12
    conversions_value: 481.12592352792007
    }]
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=("Get impact metrics for Performance Max budget."))
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    parser.add_argument(
        "-b",
        "--budget_amount_user",
        type=int,
        required=True,
        help=(
            "A budget amount (not in micros) advertiser wants to use."
        ),
    )

    args = parser.parse_args()

    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v18")

    try:
        main(
            googleads_client,
            args.customer_id,
            args.budget_amount_user,
        )
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'Error with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)