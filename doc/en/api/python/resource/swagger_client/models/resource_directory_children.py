# coding: utf-8

"""
    GeoServer Resources

    A resource is any item in the data directory that does not represent configuration. Typical resources include styles and icons.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ResourceDirectoryChildren(object):
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
        'child': 'list[ResourceDirectoryChildrenChild]'
    }

    attribute_map = {
        'child': 'child'
    }

    def __init__(self, child=None, _configuration=None):  # noqa: E501
        """ResourceDirectoryChildren - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._child = None
        self.discriminator = None

        if child is not None:
            self.child = child

    @property
    def child(self):
        """Gets the child of this ResourceDirectoryChildren.  # noqa: E501


        :return: The child of this ResourceDirectoryChildren.  # noqa: E501
        :rtype: list[ResourceDirectoryChildrenChild]
        """
        return self._child

    @child.setter
    def child(self, child):
        """Sets the child of this ResourceDirectoryChildren.


        :param child: The child of this ResourceDirectoryChildren.  # noqa: E501
        :type: list[ResourceDirectoryChildrenChild]
        """

        self._child = child

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
        if issubclass(ResourceDirectoryChildren, dict):
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
        if not isinstance(other, ResourceDirectoryChildren):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceDirectoryChildren):
            return True

        return self.to_dict() != other.to_dict()
