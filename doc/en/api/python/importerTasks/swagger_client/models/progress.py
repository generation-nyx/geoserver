# coding: utf-8

"""
    GeoServer Importer Extension - Tasks

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The tasks endpoint controls individual tasks within an import job. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Progress(object):
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
        'progress': 'str',
        'total': 'str',
        'state': 'str',
        'message': 'str'
    }

    attribute_map = {
        'progress': 'progress',
        'total': 'total',
        'state': 'state',
        'message': 'message'
    }

    def __init__(self, progress=None, total=None, state=None, message=None, _configuration=None):  # noqa: E501
        """Progress - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._progress = None
        self._total = None
        self._state = None
        self._message = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if total is not None:
            self.total = total
        if state is not None:
            self.state = state
        if message is not None:
            self.message = message

    @property
    def progress(self):
        """Gets the progress of this Progress.  # noqa: E501

        Number of operations completed  # noqa: E501

        :return: The progress of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Progress.

        Number of operations completed  # noqa: E501

        :param progress: The progress of this Progress.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def total(self):
        """Gets the total of this Progress.  # noqa: E501

        Total number of operations  # noqa: E501

        :return: The total of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Progress.

        Total number of operations  # noqa: E501

        :param total: The total of this Progress.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def state(self):
        """Gets the state of this Progress.  # noqa: E501

        State of the task.  # noqa: E501

        :return: The state of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Progress.

        State of the task.  # noqa: E501

        :param state: The state of this Progress.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "READY", "RUNNING", "NO_CRS", "NO_BOUNDS", "NO_FORMAT", "BAD_FORMAT", "ERROR", "CANCELED", "COMPLETE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def message(self):
        """Gets the message of this Progress.  # noqa: E501

        Error message. Only shown if state is \"ERROR\"  # noqa: E501

        :return: The message of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Progress.

        Error message. Only shown if state is \"ERROR\"  # noqa: E501

        :param message: The message of this Progress.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(Progress, dict):
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
        if not isinstance(other, Progress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Progress):
            return True

        return self.to_dict() != other.to_dict()
