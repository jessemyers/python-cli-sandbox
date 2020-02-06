"""
CLI entry point.

"""
from os import environ

from boto3 import Session
from click import command, echo, option

from sandbox.buckets import iter_buckets


@command()
@option(
    "--profile-name",
    "--profile",
    envvar="AWS_PROFILE",
    help="AWS profile name",
)
@option(
    "--region-name",
    "--region",
    default=environ.get("AWS_DEFAULT_REGION", "us-west-2"),
    envvar="AWS_REGION",
    help="AWS region name",
)
def main(*, profile_name: str, region_name: str, **kwargs) -> None:
    """
    List S3 buckets.

    """
    session = Session(
        profile_name=profile_name,
        region_name=region_name,
    )

    for bucket in iter_buckets(session):
        echo(bucket)
