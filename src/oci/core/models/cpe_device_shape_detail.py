# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CpeDeviceShapeDetail(object):
    """
    The detailed information about a particular CPE device type. Compare with
    :class:`CpeDeviceShapeSummary`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CpeDeviceShapeDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpe_device_shape_id:
            The value to assign to the cpe_device_shape_id property of this CpeDeviceShapeDetail.
        :type cpe_device_shape_id: str

        :param cpe_device_info:
            The value to assign to the cpe_device_info property of this CpeDeviceShapeDetail.
        :type cpe_device_info: CpeDeviceInfo

        :param parameters:
            The value to assign to the parameters property of this CpeDeviceShapeDetail.
        :type parameters: list[CpeDeviceConfigQuestion]

        :param template:
            The value to assign to the template property of this CpeDeviceShapeDetail.
        :type template: str

        """
        self.swagger_types = {
            'cpe_device_shape_id': 'str',
            'cpe_device_info': 'CpeDeviceInfo',
            'parameters': 'list[CpeDeviceConfigQuestion]',
            'template': 'str'
        }

        self.attribute_map = {
            'cpe_device_shape_id': 'cpeDeviceShapeId',
            'cpe_device_info': 'cpeDeviceInfo',
            'parameters': 'parameters',
            'template': 'template'
        }

        self._cpe_device_shape_id = None
        self._cpe_device_info = None
        self._parameters = None
        self._template = None

    @property
    def cpe_device_shape_id(self):
        """
        Gets the cpe_device_shape_id of this CpeDeviceShapeDetail.
        The `OCID`__ of the CPE device shape.
        This value uniquely identifies the type of CPE device.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cpe_device_shape_id of this CpeDeviceShapeDetail.
        :rtype: str
        """
        return self._cpe_device_shape_id

    @cpe_device_shape_id.setter
    def cpe_device_shape_id(self, cpe_device_shape_id):
        """
        Sets the cpe_device_shape_id of this CpeDeviceShapeDetail.
        The `OCID`__ of the CPE device shape.
        This value uniquely identifies the type of CPE device.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cpe_device_shape_id: The cpe_device_shape_id of this CpeDeviceShapeDetail.
        :type: str
        """
        self._cpe_device_shape_id = cpe_device_shape_id

    @property
    def cpe_device_info(self):
        """
        Gets the cpe_device_info of this CpeDeviceShapeDetail.
        Basic information about this particular CPE device type.


        :return: The cpe_device_info of this CpeDeviceShapeDetail.
        :rtype: CpeDeviceInfo
        """
        return self._cpe_device_info

    @cpe_device_info.setter
    def cpe_device_info(self, cpe_device_info):
        """
        Sets the cpe_device_info of this CpeDeviceShapeDetail.
        Basic information about this particular CPE device type.


        :param cpe_device_info: The cpe_device_info of this CpeDeviceShapeDetail.
        :type: CpeDeviceInfo
        """
        self._cpe_device_info = cpe_device_info

    @property
    def parameters(self):
        """
        Gets the parameters of this CpeDeviceShapeDetail.
        For certain CPE devices types, the customer can provide answers to
        questions that are specific to the device type. This attribute contains
        a list of those questions. The Networking service merges the answers with
        other information and renders a set of CPE configuration content. To
        provide the answers, use
        :func:`update_tunnel_cpe_device_config`.


        :return: The parameters of this CpeDeviceShapeDetail.
        :rtype: list[CpeDeviceConfigQuestion]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CpeDeviceShapeDetail.
        For certain CPE devices types, the customer can provide answers to
        questions that are specific to the device type. This attribute contains
        a list of those questions. The Networking service merges the answers with
        other information and renders a set of CPE configuration content. To
        provide the answers, use
        :func:`update_tunnel_cpe_device_config`.


        :param parameters: The parameters of this CpeDeviceShapeDetail.
        :type: list[CpeDeviceConfigQuestion]
        """
        self._parameters = parameters

    @property
    def template(self):
        """
        Gets the template of this CpeDeviceShapeDetail.
        A template of CPE device configuration information that will be merged with the customer's
        answers to the questions to render the final CPE device configuration content. Also see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`


        :return: The template of this CpeDeviceShapeDetail.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CpeDeviceShapeDetail.
        A template of CPE device configuration information that will be merged with the customer's
        answers to the questions to render the final CPE device configuration content. Also see:

          * :func:`get_cpe_device_config_content`
          * :func:`get_ipsec_cpe_device_config_content`
          * :func:`get_tunnel_cpe_device_config_content`


        :param template: The template of this CpeDeviceShapeDetail.
        :type: str
        """
        self._template = template

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
