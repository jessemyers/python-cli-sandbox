from unittest.mock import MagicMock

from hamcrest import assert_that, equal_to, is_

from sandbox.buckets import iter_buckets


def test_iter_buckets() -> None:
    session = MagicMock()
    session.client.return_value.list_buckets.return_value = dict(
        Buckets=[
            dict(Name="bucket1"),
            dict(Name="bucket2"),
        ],
    )

    buckets = list(iter_buckets(session))

    assert_that(buckets, is_(equal_to(["bucket1", "bucket2"])))
