# coding: utf-8

"""
    GeoWebCache GridSets

    A Grid Set is a set of tile grids associated with a coordinate reference system.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-geoserver-gwcgridsets"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="GeoWebCache GridSets",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoWebCache GridSets"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A Grid Set is a set of tile grids associated with a coordinate reference system.  # noqa: E501
    """
)
