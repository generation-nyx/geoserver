# coding: utf-8

"""
    OWS Services

    An OWS service refers to any of the OGC services that GeoServer supports, such as WFS, WMS, and WCS. These endpoints controls the settings of these services.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WMSInfoVersions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_geotools_util_version': 'list[str]'
    }

    attribute_map = {
        'org_geotools_util_version': 'org.geotools.util.Version'
    }

    def __init__(self, org_geotools_util_version=None, _configuration=None):  # noqa: E501
        """WMSInfoVersions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._org_geotools_util_version = None
        self.discriminator = None

        if org_geotools_util_version is not None:
            self.org_geotools_util_version = org_geotools_util_version

    @property
    def org_geotools_util_version(self):
        """Gets the org_geotools_util_version of this WMSInfoVersions.  # noqa: E501


        :return: The org_geotools_util_version of this WMSInfoVersions.  # noqa: E501
        :rtype: list[str]
        """
        return self._org_geotools_util_version

    @org_geotools_util_version.setter
    def org_geotools_util_version(self, org_geotools_util_version):
        """Sets the org_geotools_util_version of this WMSInfoVersions.


        :param org_geotools_util_version: The org_geotools_util_version of this WMSInfoVersions.  # noqa: E501
        :type: list[str]
        """

        self._org_geotools_util_version = org_geotools_util_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WMSInfoVersions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WMSInfoVersions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WMSInfoVersions):
            return True

        return self.to_dict() != other.to_dict()
