from dataclasses import dataclass
from os import environ
from typing import Any, Iterable, Type

from boto3 import Session
from click import option


@dataclass
class SessionFactory:
    profile_name: str
    region_name: str

    def make_session(self) -> Session:
        return Session(
            profile_name=self.profile_name,
            region_name=self.region_name,
        )

    @classmethod
    def iter_options(cls: Type["SessionFactory"]) -> Iterable[Any]:
        yield option(
            "--profile-name",
            "--profile",
            envvar="AWS_PROFILE",
            help="AWS profile name",
        )
        yield option(
            "--region-name",
            "--region",
            default=environ.get("AWS_DEFAULT_REGION", "us-west-2"),
            envvar="AWS_REGION",
            help="AWS region name",
        )

    @classmethod
    def options(cls: Type["SessionFactory"]):
        def wrapper(func):
            for decorator in cls.iter_options():
                func = decorator(func)
            return func
        return wrapper

    @classmethod
    def create(cls: Type["SessionFactory"],
               *,
               profile_name: str,
               region_name: str,
               **kwargs) -> "SessionFactory":
        return cls(
            profile_name=profile_name,
            region_name=region_name,
        )
