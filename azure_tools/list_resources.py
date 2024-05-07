#!/usr/bin/env python3
"""List resources."""
import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


def main():
    """List resources for subscription and resource group."""
    credential = DefaultAzureCredential()
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    resource_group = os.environ["AZURE_RESOURCE_GROUP_NAME"]

    resource_client = ResourceManagementClient(credential, subscription_id)
    resource_list = resource_client.resources.list_by_resource_group(
        resource_group, expand="createdTime,changedTime")

    column_width = 36
    print(f"{'Resource':<{column_width}}"
          f"{'Type':<{column_width}}"
          f"{'Create date':<{column_width}}"
          f"{'Change date':<{column_width}}")
    print(f"{'-' * (column_width * 4)}")
    for resource in list(resource_list):
        print(f"{resource.name:<{column_width}}"
              f"{resource.type:<{column_width}}"
              f"{str(resource.created_time):<{column_width}}"
              f"{str(resource.changed_time):<{column_width}}")


if __name__ == "__main__":
    main()
