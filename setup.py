from distutils.core import setup

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
    "structlog",
    "allure-pytest"
]

setup(
    name='dm_api_account',
    version='0.0.2',
    packages=['dm_api_account'],
    url="https://github.com/allezov/openapi-templates.git",
    license='Apache-2.0 license',
    author="lezov",
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account'
)
# setup(
#     name='dm_api_account_clients',
#     version='0.0.5',
#     packages=['dm_api_account'],
#     url='https://github.com/allezov/dm_api_account.git',
#     license='Apache-2.0 license',
#     author='lezov',
#     author_email='-',
#     install_requires=REQUIRES,
#     description='dm_api_account_clients'
# )
