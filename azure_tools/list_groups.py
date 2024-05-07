#!/usr/bin/env python3
"""List groups."""
import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def main():
    """List groups for subscription."""
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

    resource_client = ResourceManagementClient(credential, subscription_id)
    group_list = resource_client.resource_groups.list()

    column_width = 40
    print(f"{'Resource Group':<{column_width}}"
          f"{'Location':<{column_width}}")
    print(f"{'-' * (column_width * 4)}")
    for group in list(group_list):
        print(f"{group.name:<{column_width}}"
              f"{group.location:<{column_width}}")


if __name__ == "__main__":
    main()
