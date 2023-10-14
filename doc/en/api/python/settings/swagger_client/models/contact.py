# coding: utf-8

"""
    GeoServer Settings

    The Settings area shows global configuration for the server  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Contact(object):
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
        'address_city': 'str',
        'address_country': 'str',
        'address_type': 'str',
        'contact_email': 'str',
        'contact_organization': 'str',
        'contact_person': 'str',
        'contact_position': 'str'
    }

    attribute_map = {
        'address_city': 'addressCity',
        'address_country': 'addressCountry',
        'address_type': 'addressType',
        'contact_email': 'contactEmail',
        'contact_organization': 'contactOrganization',
        'contact_person': 'contactPerson',
        'contact_position': 'contactPosition'
    }

    def __init__(self, address_city=None, address_country=None, address_type=None, contact_email=None, contact_organization=None, contact_person=None, contact_position=None, _configuration=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address_city = None
        self._address_country = None
        self._address_type = None
        self._contact_email = None
        self._contact_organization = None
        self._contact_person = None
        self._contact_position = None
        self.discriminator = None

        if address_city is not None:
            self.address_city = address_city
        if address_country is not None:
            self.address_country = address_country
        if address_type is not None:
            self.address_type = address_type
        if contact_email is not None:
            self.contact_email = contact_email
        if contact_organization is not None:
            self.contact_organization = contact_organization
        if contact_person is not None:
            self.contact_person = contact_person
        if contact_position is not None:
            self.contact_position = contact_position

    @property
    def address_city(self):
        """Gets the address_city of this Contact.  # noqa: E501

        Server admin city  # noqa: E501

        :return: The address_city of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this Contact.

        Server admin city  # noqa: E501

        :param address_city: The address_city of this Contact.  # noqa: E501
        :type: str
        """

        self._address_city = address_city

    @property
    def address_country(self):
        """Gets the address_country of this Contact.  # noqa: E501

        Server admin country  # noqa: E501

        :return: The address_country of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this Contact.

        Server admin country  # noqa: E501

        :param address_country: The address_country of this Contact.  # noqa: E501
        :type: str
        """

        self._address_country = address_country

    @property
    def address_type(self):
        """Gets the address_type of this Contact.  # noqa: E501

        Type of address  # noqa: E501

        :return: The address_type of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this Contact.

        Type of address  # noqa: E501

        :param address_type: The address_type of this Contact.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def contact_email(self):
        """Gets the contact_email of this Contact.  # noqa: E501

        Server admin email  # noqa: E501

        :return: The contact_email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Contact.

        Server admin email  # noqa: E501

        :param contact_email: The contact_email of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_organization(self):
        """Gets the contact_organization of this Contact.  # noqa: E501

        Server admin organization  # noqa: E501

        :return: The contact_organization of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_organization

    @contact_organization.setter
    def contact_organization(self, contact_organization):
        """Sets the contact_organization of this Contact.

        Server admin organization  # noqa: E501

        :param contact_organization: The contact_organization of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_organization = contact_organization

    @property
    def contact_person(self):
        """Gets the contact_person of this Contact.  # noqa: E501

        Server admin point of contact  # noqa: E501

        :return: The contact_person of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this Contact.

        Server admin point of contact  # noqa: E501

        :param contact_person: The contact_person of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def contact_position(self):
        """Gets the contact_position of this Contact.  # noqa: E501

        Server admin point of contact job title  # noqa: E501

        :return: The contact_position of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._contact_position

    @contact_position.setter
    def contact_position(self, contact_position):
        """Sets the contact_position of this Contact.

        Server admin point of contact job title  # noqa: E501

        :param contact_position: The contact_position of this Contact.  # noqa: E501
        :type: str
        """

        self._contact_position = contact_position

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Contact):
            return True

        return self.to_dict() != other.to_dict()
