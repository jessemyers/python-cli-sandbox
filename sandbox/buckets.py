"""
Bucket functions.

"""
from typing import List

from boto3 import Session


def iter_buckets(session: Session) -> List[str]:
    s3 = session.client("s3")

    response = s3.list_buckets()

    return [
        bucket["Name"]
        for bucket in response["Buckets"]
    ]
