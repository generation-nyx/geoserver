# coding: utf-8

"""
    GeoServer Importer Extension - Main

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The main endpoint manages individual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Database(object):
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
        'type': 'str',
        'format': 'str',
        'href': 'str',
        'properties': 'object',
        'tables': 'list[Table]'
    }

    attribute_map = {
        'type': 'type',
        'format': 'format',
        'href': 'href',
        'properties': 'properties',
        'tables': 'tables'
    }

    def __init__(self, type=None, format=None, href=None, properties=None, tables=None, _configuration=None):  # noqa: E501
        """Database - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._format = None
        self._href = None
        self._properties = None
        self._tables = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if href is not None:
            self.href = href
        if properties is not None:
            self.properties = properties
        if tables is not None:
            self.tables = tables

    @property
    def type(self):
        """Gets the type of this Database.  # noqa: E501

        \"database\"  # noqa: E501

        :return: The type of this Database.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Database.

        \"database\"  # noqa: E501

        :param type: The type of this Database.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """Gets the format of this Database.  # noqa: E501


        :return: The format of this Database.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Database.


        :param format: The format of this Database.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def href(self):
        """Gets the href of this Database.  # noqa: E501

        URL to the database endpoint  # noqa: E501

        :return: The href of this Database.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Database.

        URL to the database endpoint  # noqa: E501

        :param href: The href of this Database.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def properties(self):
        """Gets the properties of this Database.  # noqa: E501

        Database connection parameters. Actual paramaters vary depending on the type of database.  # noqa: E501

        :return: The properties of this Database.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Database.

        Database connection parameters. Actual paramaters vary depending on the type of database.  # noqa: E501

        :param properties: The properties of this Database.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def tables(self):
        """Gets the tables of this Database.  # noqa: E501


        :return: The tables of this Database.  # noqa: E501
        :rtype: list[Table]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this Database.


        :param tables: The tables of this Database.  # noqa: E501
        :type: list[Table]
        """

        self._tables = tables

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
        if issubclass(Database, dict):
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
        if not isinstance(other, Database):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Database):
            return True

        return self.to_dict() != other.to_dict()
