#!/usr/bin/env python
from setuptools import find_packages, setup


project = "sandbox"
version = "0.1.0"


url = "https://github.com/jessemyers/python-cli-sandbox"

try:
    with open("README.md") as file_:
        long_description = file_.read()
except IOError:
    long_description = "See {}".format(url)


setup(
    name=project,
    version=version,
    description="Example CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jesse Myers",
    url=url,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "boto3>=1.10.20",
        "click>=7.0",
    ],
    entry_points={
        "console_scripts": [
            "list-buckets = sandbox.main:main",
        ],
    },
    extras_require=dict(
        lint=[
            "flake8>=3.7.9",
            "flake8-isort>=2.7.0",
        ],
        test=[
            "coverage>=4.5.4",
            "PyHamcrest>=1.9.0",
            "pytest>=5.3.5",
        ],
        typehinting=[
            "mypy>=0.740.0",
        ],
    ),
)
