# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.7.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnalysisResultResponseResultAicoeci(object):
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
        'requirements': 'RequirementsDef',
        'requirements_lock': 'RequirementsLockDef'
    }

    attribute_map = {
        'requirements': 'requirements',
        'requirements_lock': 'requirements_lock'
    }

    def __init__(self, requirements=None, requirements_lock=None):  # noqa: E501
        """AnalysisResultResponseResultAicoeci - a model defined in Swagger"""  # noqa: E501
        self._requirements = None
        self._requirements_lock = None
        self.discriminator = None
        self.requirements = requirements
        self.requirements_lock = requirements_lock

    @property
    def requirements(self):
        """Gets the requirements of this AnalysisResultResponseResultAicoeci.  # noqa: E501


        :return: The requirements of this AnalysisResultResponseResultAicoeci.  # noqa: E501
        :rtype: RequirementsDef
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this AnalysisResultResponseResultAicoeci.


        :param requirements: The requirements of this AnalysisResultResponseResultAicoeci.  # noqa: E501
        :type: RequirementsDef
        """
        if requirements is None:
            raise ValueError("Invalid value for `requirements`, must not be `None`")  # noqa: E501

        self._requirements = requirements

    @property
    def requirements_lock(self):
        """Gets the requirements_lock of this AnalysisResultResponseResultAicoeci.  # noqa: E501


        :return: The requirements_lock of this AnalysisResultResponseResultAicoeci.  # noqa: E501
        :rtype: RequirementsLockDef
        """
        return self._requirements_lock

    @requirements_lock.setter
    def requirements_lock(self, requirements_lock):
        """Sets the requirements_lock of this AnalysisResultResponseResultAicoeci.


        :param requirements_lock: The requirements_lock of this AnalysisResultResponseResultAicoeci.  # noqa: E501
        :type: RequirementsLockDef
        """
        if requirements_lock is None:
            raise ValueError("Invalid value for `requirements_lock`, must not be `None`")  # noqa: E501

        self._requirements_lock = requirements_lock

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
        if issubclass(AnalysisResultResponseResultAicoeci, dict):
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
        if not isinstance(other, AnalysisResultResponseResultAicoeci):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
