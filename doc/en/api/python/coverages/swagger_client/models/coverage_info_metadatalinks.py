# coding: utf-8

"""
    GeoServer Coverages

    A coverage is a raster data set which originates from a coverage store.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class CoverageInfoMetadatalinks(object):
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
        'metadata_link': 'list[CoverageInfoMetadatalinksMetadataLink]'
    }

    attribute_map = {
        'metadata_link': 'metadataLink'
    }

    def __init__(self, metadata_link=None, _configuration=None):  # noqa: E501
        """CoverageInfoMetadatalinks - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metadata_link = None
        self.discriminator = None

        if metadata_link is not None:
            self.metadata_link = metadata_link

    @property
    def metadata_link(self):
        """Gets the metadata_link of this CoverageInfoMetadatalinks.  # noqa: E501

        A collection of metadata links for the resource.  # noqa: E501

        :return: The metadata_link of this CoverageInfoMetadatalinks.  # noqa: E501
        :rtype: list[CoverageInfoMetadatalinksMetadataLink]
        """
        return self._metadata_link

    @metadata_link.setter
    def metadata_link(self, metadata_link):
        """Sets the metadata_link of this CoverageInfoMetadatalinks.

        A collection of metadata links for the resource.  # noqa: E501

        :param metadata_link: The metadata_link of this CoverageInfoMetadatalinks.  # noqa: E501
        :type: list[CoverageInfoMetadatalinksMetadataLink]
        """

        self._metadata_link = metadata_link

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
        if issubclass(CoverageInfoMetadatalinks, dict):
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
        if not isinstance(other, CoverageInfoMetadatalinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoverageInfoMetadatalinks):
            return True

        return self.to_dict() != other.to_dict()
