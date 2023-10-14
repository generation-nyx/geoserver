# coding: utf-8

"""
    GeoWebCache DiskQuota

    The REST API for Disk Quota management provides a RESTful interface through which clients can configure the disk usage limits and expiration policies for a GeoWebCache instance through simple HTTP calls.  Since disk usage increases geometrically by zoom level, one single seeding task could fill up an entire storage device. Because of this, GeoWebCache employs a disk quota system where one can specify the maximum amount of disk space to use for a particular layer, as well as logic on how to proceed when that quota is reached. There are two different policies for managing the disk quotas - Least Frequently Used (LFU) and Least Recently Used (LRU).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.disk_quota_global_quota import DiskQuotaGlobalQuota  # noqa: E501
from swagger_client.rest import ApiException


class TestDiskQuotaGlobalQuota(unittest.TestCase):
    """DiskQuotaGlobalQuota unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDiskQuotaGlobalQuota(self):
        """Test DiskQuotaGlobalQuota"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.disk_quota_global_quota.DiskQuotaGlobalQuota()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
