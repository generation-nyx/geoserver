# coding: utf-8

"""
    GeoServer WMTS Store Layers

    A WMTS store is a store whose source is a remote WMTS service. Also known as \"Cascading WMTS\". A WMTS store layer is a layer from this store.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WMTSStoreLayerInfoKeywords(object):
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
        'string': 'str'
    }

    attribute_map = {
        'string': 'string'
    }

    def __init__(self, string=None, _configuration=None):  # noqa: E501
        """WMTSStoreLayerInfoKeywords - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._string = None
        self.discriminator = None

        if string is not None:
            self.string = string

    @property
    def string(self):
        """Gets the string of this WMTSStoreLayerInfoKeywords.  # noqa: E501

        Keyword  # noqa: E501

        :return: The string of this WMTSStoreLayerInfoKeywords.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this WMTSStoreLayerInfoKeywords.

        Keyword  # noqa: E501

        :param string: The string of this WMTSStoreLayerInfoKeywords.  # noqa: E501
        :type: str
        """

        self._string = string

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
        if issubclass(WMTSStoreLayerInfoKeywords, dict):
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
        if not isinstance(other, WMTSStoreLayerInfoKeywords):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WMTSStoreLayerInfoKeywords):
            return True

        return self.to_dict() != other.to_dict()
