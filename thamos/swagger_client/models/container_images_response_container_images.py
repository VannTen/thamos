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

class ContainerImagesResponseContainerImages(object):
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
        'environment_name': 'str',
        'python_version': 'str',
        'env_image_name': 'str',
        'env_image_tag': 'str',
        'image_sha': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'thoth_image_name': 'str',
        'thoth_image_version': 'str',
        'cuda_version': 'str',
        'environment_type': 'str',
        'package_extract_document_id': 'str',
        '_datetime': 'str',
        'quay_repo_url': 'str',
        'image_analysis_url': 'str'
    }

    attribute_map = {
        'environment_name': 'environment_name',
        'python_version': 'python_version',
        'env_image_name': 'env_image_name',
        'env_image_tag': 'env_image_tag',
        'image_sha': 'image_sha',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'thoth_image_name': 'thoth_image_name',
        'thoth_image_version': 'thoth_image_version',
        'cuda_version': 'cuda_version',
        'environment_type': 'environment_type',
        'package_extract_document_id': 'package_extract_document_id',
        '_datetime': 'datetime',
        'quay_repo_url': 'quay_repo_url',
        'image_analysis_url': 'image_analysis_url'
    }

    def __init__(self, environment_name=None, python_version=None, env_image_name=None, env_image_tag=None, image_sha=None, os_name=None, os_version=None, thoth_image_name=None, thoth_image_version=None, cuda_version=None, environment_type=None, package_extract_document_id=None, _datetime=None, quay_repo_url=None, image_analysis_url=None):  # noqa: E501
        """ContainerImagesResponseContainerImages - a model defined in Swagger"""  # noqa: E501
        self._environment_name = None
        self._python_version = None
        self._env_image_name = None
        self._env_image_tag = None
        self._image_sha = None
        self._os_name = None
        self._os_version = None
        self._thoth_image_name = None
        self._thoth_image_version = None
        self._cuda_version = None
        self._environment_type = None
        self._package_extract_document_id = None
        self.__datetime = None
        self._quay_repo_url = None
        self._image_analysis_url = None
        self.discriminator = None
        self.environment_name = environment_name
        self.python_version = python_version
        self.env_image_name = env_image_name
        self.env_image_tag = env_image_tag
        self.image_sha = image_sha
        self.os_name = os_name
        self.os_version = os_version
        self.thoth_image_name = thoth_image_name
        self.thoth_image_version = thoth_image_version
        self.cuda_version = cuda_version
        self.environment_type = environment_type
        self.package_extract_document_id = package_extract_document_id
        self._datetime = _datetime
        self.quay_repo_url = quay_repo_url
        self.image_analysis_url = image_analysis_url

    @property
    def environment_name(self):
        """Gets the environment_name of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The environment_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this ContainerImagesResponseContainerImages.


        :param environment_name: The environment_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def python_version(self):
        """Gets the python_version of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The python_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this ContainerImagesResponseContainerImages.


        :param python_version: The python_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._python_version = python_version

    @property
    def env_image_name(self):
        """Gets the env_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The env_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._env_image_name

    @env_image_name.setter
    def env_image_name(self, env_image_name):
        """Sets the env_image_name of this ContainerImagesResponseContainerImages.


        :param env_image_name: The env_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._env_image_name = env_image_name

    @property
    def env_image_tag(self):
        """Gets the env_image_tag of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The env_image_tag of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._env_image_tag

    @env_image_tag.setter
    def env_image_tag(self, env_image_tag):
        """Sets the env_image_tag of this ContainerImagesResponseContainerImages.


        :param env_image_tag: The env_image_tag of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._env_image_tag = env_image_tag

    @property
    def image_sha(self):
        """Gets the image_sha of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The image_sha of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._image_sha

    @image_sha.setter
    def image_sha(self, image_sha):
        """Sets the image_sha of this ContainerImagesResponseContainerImages.


        :param image_sha: The image_sha of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._image_sha = image_sha

    @property
    def os_name(self):
        """Gets the os_name of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The os_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this ContainerImagesResponseContainerImages.


        :param os_name: The os_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

    @property
    def os_version(self):
        """Gets the os_version of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The os_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ContainerImagesResponseContainerImages.


        :param os_version: The os_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def thoth_image_name(self):
        """Gets the thoth_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The thoth_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._thoth_image_name

    @thoth_image_name.setter
    def thoth_image_name(self, thoth_image_name):
        """Sets the thoth_image_name of this ContainerImagesResponseContainerImages.


        :param thoth_image_name: The thoth_image_name of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._thoth_image_name = thoth_image_name

    @property
    def thoth_image_version(self):
        """Gets the thoth_image_version of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The thoth_image_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._thoth_image_version

    @thoth_image_version.setter
    def thoth_image_version(self, thoth_image_version):
        """Sets the thoth_image_version of this ContainerImagesResponseContainerImages.


        :param thoth_image_version: The thoth_image_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._thoth_image_version = thoth_image_version

    @property
    def cuda_version(self):
        """Gets the cuda_version of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The cuda_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._cuda_version

    @cuda_version.setter
    def cuda_version(self, cuda_version):
        """Sets the cuda_version of this ContainerImagesResponseContainerImages.


        :param cuda_version: The cuda_version of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """

        self._cuda_version = cuda_version

    @property
    def environment_type(self):
        """Gets the environment_type of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The environment_type of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._environment_type

    @environment_type.setter
    def environment_type(self, environment_type):
        """Sets the environment_type of this ContainerImagesResponseContainerImages.


        :param environment_type: The environment_type of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """
        if environment_type is None:
            raise ValueError("Invalid value for `environment_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BUILDTIME", "RUNTIME"]  # noqa: E501
        if environment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `environment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(environment_type, allowed_values)
            )

        self._environment_type = environment_type

    @property
    def package_extract_document_id(self):
        """Gets the package_extract_document_id of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The package_extract_document_id of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._package_extract_document_id

    @package_extract_document_id.setter
    def package_extract_document_id(self, package_extract_document_id):
        """Sets the package_extract_document_id of this ContainerImagesResponseContainerImages.


        :param package_extract_document_id: The package_extract_document_id of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """
        if package_extract_document_id is None:
            raise ValueError("Invalid value for `package_extract_document_id`, must not be `None`")  # noqa: E501

        self._package_extract_document_id = package_extract_document_id

    @property
    def _datetime(self):
        """Gets the _datetime of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The _datetime of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this ContainerImagesResponseContainerImages.


        :param _datetime: The _datetime of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """
        if _datetime is None:
            raise ValueError("Invalid value for `_datetime`, must not be `None`")  # noqa: E501

        self.__datetime = _datetime

    @property
    def quay_repo_url(self):
        """Gets the quay_repo_url of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The quay_repo_url of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._quay_repo_url

    @quay_repo_url.setter
    def quay_repo_url(self, quay_repo_url):
        """Sets the quay_repo_url of this ContainerImagesResponseContainerImages.


        :param quay_repo_url: The quay_repo_url of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """
        if quay_repo_url is None:
            raise ValueError("Invalid value for `quay_repo_url`, must not be `None`")  # noqa: E501

        self._quay_repo_url = quay_repo_url

    @property
    def image_analysis_url(self):
        """Gets the image_analysis_url of this ContainerImagesResponseContainerImages.  # noqa: E501


        :return: The image_analysis_url of this ContainerImagesResponseContainerImages.  # noqa: E501
        :rtype: str
        """
        return self._image_analysis_url

    @image_analysis_url.setter
    def image_analysis_url(self, image_analysis_url):
        """Sets the image_analysis_url of this ContainerImagesResponseContainerImages.


        :param image_analysis_url: The image_analysis_url of this ContainerImagesResponseContainerImages.  # noqa: E501
        :type: str
        """
        if image_analysis_url is None:
            raise ValueError("Invalid value for `image_analysis_url`, must not be `None`")  # noqa: E501

        self._image_analysis_url = image_analysis_url

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
        if issubclass(ContainerImagesResponseContainerImages, dict):
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
        if not isinstance(other, ContainerImagesResponseContainerImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
