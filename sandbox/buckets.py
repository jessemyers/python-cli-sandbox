"""
Bucket functions.

"""
from typing import Iterable

from boto3 import Session


def iter_buckets(session: Session) -> Iterable[str]:
    s3 = session.client("s3")

    response = s3.list_buckets()

    yield from (
        bucket["Name"]
        for bucket in response["Buckets"]
    )
