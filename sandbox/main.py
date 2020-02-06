"""
CLI entry point.

"""
from click import command, echo

from sandbox.buckets import iter_buckets
from sandbox.session_factory import SessionFactory


@command()
@SessionFactory.options()
def main(**kwargs) -> None:
    """
    List S3 buckets.

    """
    session = SessionFactory.create(**kwargs).make_session()

    for bucket in iter_buckets(session):
        echo(bucket)


@command()
@SessionFactory.options()
def main2(*, profile_name: str, region_name: str, **kwargs) -> None:
    """
    List S3 buckets.

    """
    session = SessionFactory.create(**kwargs).make_session()

    for bucket in iter_buckets(session):
        echo(bucket)
