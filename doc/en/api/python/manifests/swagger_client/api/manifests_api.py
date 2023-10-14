# coding: utf-8

"""
    GeoServer Manifests API

    GeoServer provides a REST service to expose a listing of all loaded JARs and resources on the running instance. This is useful for bug reports and to keep track of extensions deployed into the application.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ManifestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def about_status_get(self, **kwargs):  # noqa: E501
        """about_status_get  # noqa: E501

        This endpoint shows the status details of all installed and configured modules. Status details always include human readable name, and module name. Optional details include version, availability, status message, and links to documentation.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.about_status_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.about_status_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.about_status_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def about_status_get_with_http_info(self, **kwargs):  # noqa: E501
        """about_status_get  # noqa: E501

        This endpoint shows the status details of all installed and configured modules. Status details always include human readable name, and module name. Optional details include version, availability, status message, and links to documentation.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.about_status_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manifest', 'key', 'value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method about_status_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'manifest' in params:
            query_params.append(('manifest', params['manifest']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'value' in params:
            query_params.append(('value', params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/about/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Status',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def about_version_get(self, **kwargs):  # noqa: E501
        """about_version_get  # noqa: E501

        'This endpoint shows only the details for the high-level components: GeoServer, GeoTools, and GeoWebCache.'  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.about_version_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.about_version_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.about_version_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def about_version_get_with_http_info(self, **kwargs):  # noqa: E501
        """about_version_get  # noqa: E501

        'This endpoint shows only the details for the high-level components: GeoServer, GeoTools, and GeoWebCache.'  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).'   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.about_version_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manifest', 'key', 'value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method about_version_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'manifest' in params:
            query_params.append(('manifest', params['manifest']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'value' in params:
            query_params.append(('value', params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/about/version', 'GET',
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

    def get_manifest(self, **kwargs):  # noqa: E501
        """get_manifest  # noqa: E501

        This endpoint retrieves details on all loaded JARs. All the GeoServer manifest JARs are marked with the property GeoServerModule and classified by type, so you can use filtering capabilities to search for a set of manifests using regular expressions (see the manifest parameter) or a type category (see the key and value parameter).  The available types are core, extension, or community. To filter modules by a particular type, append a request with key=GeoServerModule&value={type}  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).  The model is very simple and is shared between the version and the resource requests to parse both requests. You can customize the results adding a properties file called manifest.properties into the root of the data directory.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manifest(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: Manifest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_manifest_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_manifest_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_manifest_with_http_info(self, **kwargs):  # noqa: E501
        """get_manifest  # noqa: E501

        This endpoint retrieves details on all loaded JARs. All the GeoServer manifest JARs are marked with the property GeoServerModule and classified by type, so you can use filtering capabilities to search for a set of manifests using regular expressions (see the manifest parameter) or a type category (see the key and value parameter).  The available types are core, extension, or community. To filter modules by a particular type, append a request with key=GeoServerModule&value={type}  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/about/manifest.xml\" for XML).  The model is very simple and is shared between the version and the resource requests to parse both requests. You can customize the results adding a properties file called manifest.properties into the root of the data directory.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manifest_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str manifest: The manifest parameter is used to filter over resulting resource (manifest) names attribute using Java regular expressions. 
        :param str key: Only return manifest entries with this key in their properties. It can be optionally combined with the value parameter.  
        :param str value: Only return manifest entries that have this value for the provided key parameter.           
        :return: Manifest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['manifest', 'key', 'value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manifest" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'manifest' in params:
            query_params.append(('manifest', params['manifest']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
        if 'value' in params:
            query_params.append(('value', params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/about/manifest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Manifest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
