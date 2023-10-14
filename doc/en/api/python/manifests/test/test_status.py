# coding: utf-8

"""
    GeoServer Manifests API

    GeoServer provides a REST service to expose a listing of all loaded JARs and resources on the running instance. This is useful for bug reports and to keep track of extensions deployed into the application.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.status import Status  # noqa: E501
from swagger_client.rest import ApiException


class TestStatus(unittest.TestCase):
    """Status unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatus(self):
        """Test Status"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.status.Status()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
