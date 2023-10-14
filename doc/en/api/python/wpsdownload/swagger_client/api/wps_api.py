# coding: utf-8

"""
    WPS download configuration

    The WPS download module allows to perform large data, map and animation downloads sing asynchronous requests  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WPSApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_download_service_configuration(self, **kwargs):  # noqa: E501
        """get_download_service_configuration  # noqa: E501

        Retrieves the WPS Download configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_download_service_configuration(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DownloadServiceConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_download_service_configuration_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_download_service_configuration_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_download_service_configuration_with_http_info(self, **kwargs):  # noqa: E501
        """get_download_service_configuration  # noqa: E501

        Retrieves the WPS Download configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_download_service_configuration_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DownloadServiceConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_download_service_configuration" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/wps/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DownloadServiceConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_download_service_configuration_0(self, get_download_service_configuration_body, **kwargs):  # noqa: E501
        """get_download_service_configuration_0  # noqa: E501

        Retrieves the WPS Download configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_download_service_configuration_0(get_download_service_configuration_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadServiceConfiguration get_download_service_configuration_body: Body of the WPS download configuration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_download_service_configuration_0_with_http_info(get_download_service_configuration_body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_download_service_configuration_0_with_http_info(get_download_service_configuration_body, **kwargs)  # noqa: E501
            return data

    def get_download_service_configuration_0_with_http_info(self, get_download_service_configuration_body, **kwargs):  # noqa: E501
        """get_download_service_configuration_0  # noqa: E501

        Retrieves the WPS Download configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_download_service_configuration_0_with_http_info(get_download_service_configuration_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DownloadServiceConfiguration get_download_service_configuration_body: Body of the WPS download configuration (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_download_service_configuration_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_download_service_configuration_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_download_service_configuration_body' is set
        if self.api_client.client_side_validation and ('get_download_service_configuration_body' not in params or
                                                       params['get_download_service_configuration_body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `get_download_service_configuration_body` when calling `get_download_service_configuration_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_download_service_configuration_body' in params:
            body_params = params['get_download_service_configuration_body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/services/wps/download', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
