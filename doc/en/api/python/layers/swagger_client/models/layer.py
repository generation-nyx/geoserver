# coding: utf-8

"""
    GeoServer Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Layer(object):
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
        'name': 'str',
        'path': 'str',
        'type': 'str',
        'default_style': 'StyleReference',
        'styles': 'LayerStyles',
        'resource': 'LayerResource',
        'opaque': 'bool',
        'metadata': 'list[MetadataEntry]',
        'attribution': 'LayerAttribution',
        'authority_urls': 'list[AuthorityURL]',
        'identifiers': 'list[Identifier]'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'type': 'type',
        'default_style': 'defaultStyle',
        'styles': 'styles',
        'resource': 'resource',
        'opaque': 'opaque',
        'metadata': 'metadata',
        'attribution': 'attribution',
        'authority_urls': 'authorityURLs',
        'identifiers': 'identifiers'
    }

    def __init__(self, name=None, path=None, type=None, default_style=None, styles=None, resource=None, opaque=None, metadata=None, attribution=None, authority_urls=None, identifiers=None, _configuration=None):  # noqa: E501
        """Layer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._path = None
        self._type = None
        self._default_style = None
        self._styles = None
        self._resource = None
        self._opaque = None
        self._metadata = None
        self._attribution = None
        self._authority_urls = None
        self._identifiers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if type is not None:
            self.type = type
        if default_style is not None:
            self.default_style = default_style
        if styles is not None:
            self.styles = styles
        if resource is not None:
            self.resource = resource
        if opaque is not None:
            self.opaque = opaque
        if metadata is not None:
            self.metadata = metadata
        if attribution is not None:
            self.attribution = attribution
        if authority_urls is not None:
            self.authority_urls = authority_urls
        if identifiers is not None:
            self.identifiers = identifiers

    @property
    def name(self):
        """Gets the name of this Layer.  # noqa: E501

        Name of the layer  # noqa: E501

        :return: The name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Layer.

        Name of the layer  # noqa: E501

        :param name: The name of this Layer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this Layer.  # noqa: E501

        Location of the layer in the WMS capabilities layer tree  # noqa: E501

        :return: The path of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Layer.

        Location of the layer in the WMS capabilities layer tree  # noqa: E501

        :param path: The path of this Layer.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def type(self):
        """Gets the type of this Layer.  # noqa: E501

        Type of published layer. Can be VECTOR, RASTER, REMOTE, WMS or GROUP. Must be consistent with resource definition.  # noqa: E501

        :return: The type of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Layer.

        Type of published layer. Can be VECTOR, RASTER, REMOTE, WMS or GROUP. Must be consistent with resource definition.  # noqa: E501

        :param type: The type of this Layer.  # noqa: E501
        :type: str
        """
        allowed_values = ["VECTOR", "RASTER", "REMOTE", "WMS", "GROUP"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def default_style(self):
        """Gets the default_style of this Layer.  # noqa: E501


        :return: The default_style of this Layer.  # noqa: E501
        :rtype: StyleReference
        """
        return self._default_style

    @default_style.setter
    def default_style(self, default_style):
        """Sets the default_style of this Layer.


        :param default_style: The default_style of this Layer.  # noqa: E501
        :type: StyleReference
        """

        self._default_style = default_style

    @property
    def styles(self):
        """Gets the styles of this Layer.  # noqa: E501


        :return: The styles of this Layer.  # noqa: E501
        :rtype: LayerStyles
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this Layer.


        :param styles: The styles of this Layer.  # noqa: E501
        :type: LayerStyles
        """

        self._styles = styles

    @property
    def resource(self):
        """Gets the resource of this Layer.  # noqa: E501


        :return: The resource of this Layer.  # noqa: E501
        :rtype: LayerResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Layer.


        :param resource: The resource of this Layer.  # noqa: E501
        :type: LayerResource
        """

        self._resource = resource

    @property
    def opaque(self):
        """Gets the opaque of this Layer.  # noqa: E501

        Controls layer transparency (whether the layer is opaque or transparent).  # noqa: E501

        :return: The opaque of this Layer.  # noqa: E501
        :rtype: bool
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque):
        """Sets the opaque of this Layer.

        Controls layer transparency (whether the layer is opaque or transparent).  # noqa: E501

        :param opaque: The opaque of this Layer.  # noqa: E501
        :type: bool
        """

        self._opaque = opaque

    @property
    def metadata(self):
        """Gets the metadata of this Layer.  # noqa: E501


        :return: The metadata of this Layer.  # noqa: E501
        :rtype: list[MetadataEntry]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Layer.


        :param metadata: The metadata of this Layer.  # noqa: E501
        :type: list[MetadataEntry]
        """

        self._metadata = metadata

    @property
    def attribution(self):
        """Gets the attribution of this Layer.  # noqa: E501


        :return: The attribution of this Layer.  # noqa: E501
        :rtype: LayerAttribution
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this Layer.


        :param attribution: The attribution of this Layer.  # noqa: E501
        :type: LayerAttribution
        """

        self._attribution = attribution

    @property
    def authority_urls(self):
        """Gets the authority_urls of this Layer.  # noqa: E501


        :return: The authority_urls of this Layer.  # noqa: E501
        :rtype: list[AuthorityURL]
        """
        return self._authority_urls

    @authority_urls.setter
    def authority_urls(self, authority_urls):
        """Sets the authority_urls of this Layer.


        :param authority_urls: The authority_urls of this Layer.  # noqa: E501
        :type: list[AuthorityURL]
        """

        self._authority_urls = authority_urls

    @property
    def identifiers(self):
        """Gets the identifiers of this Layer.  # noqa: E501


        :return: The identifiers of this Layer.  # noqa: E501
        :rtype: list[Identifier]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this Layer.


        :param identifiers: The identifiers of this Layer.  # noqa: E501
        :type: list[Identifier]
        """

        self._identifiers = identifiers

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
        if issubclass(Layer, dict):
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
        if not isinstance(other, Layer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Layer):
            return True

        return self.to_dict() != other.to_dict()
