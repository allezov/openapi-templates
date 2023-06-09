"""
    DM.API Account

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dm-api-account"
VERSION = "v1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "structlog",
  "allure-pytest",
]

setup(
    name='dm_api_account',
    version=VERSION,
    description="DM.API Account",
    author="author",
    author_email="author@email.ru",
    url="https://github.com/allezov/openapi-templates.git",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)
