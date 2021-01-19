# coding: utf-8

"""
    sbml4j API

    This is the api for the SBML4j Service   # noqa: E501

    OpenAPI spec version: 1.1.5
    Contact: thorsten.tiede@uni-tuebingen.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pysbml4j.api_client import ApiClient


class SbmlApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def upload_sbml(self, files, user, organism, source, version, **kwargs):  # noqa: E501
        """Upload SBML Model to create a Pathway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_sbml(files, user, organism, source, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] files: (required)
        :param str user: The user which requests the creation (required)
        :param str organism: The three-letter organism code (required)
        :param str source: The name of the source this SBML originates from (required)
        :param str version: The version of the source this SBML originates from (required)
        :return: list[InlineResponse201]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_sbml_with_http_info(files, user, organism, source, version, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_sbml_with_http_info(files, user, organism, source, version, **kwargs)  # noqa: E501
            return data

    def upload_sbml_with_http_info(self, files, user, organism, source, version, **kwargs):  # noqa: E501
        """Upload SBML Model to create a Pathway  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_sbml_with_http_info(files, user, organism, source, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] files: (required)
        :param str user: The user which requests the creation (required)
        :param str organism: The three-letter organism code (required)
        :param str source: The name of the source this SBML originates from (required)
        :param str version: The version of the source this SBML originates from (required)
        :return: list[InlineResponse201]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['files', 'user', 'organism', 'source', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_sbml" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'files' is set
        if ('files' not in params or
                params['files'] is None):
            raise ValueError("Missing the required parameter `files` when calling `upload_sbml`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `upload_sbml`")  # noqa: E501
        # verify the required parameter 'organism' is set
        if ('organism' not in params or
                params['organism'] is None):
            raise ValueError("Missing the required parameter `organism` when calling `upload_sbml`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `upload_sbml`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `upload_sbml`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organism' in params:
            query_params.append(('organism', params['organism']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}
        if 'user' in params:
            header_params['user'] = params['user']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'files' in params:
            form_params.append(('files', params['files']))  # noqa: E501
            collection_formats['files'] = 'multi'  # noqa: E501
            for localfilename in params['files']:
                local_var_files[localfilename.split('/')[-1]] = localfilename

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sbml', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse201]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
