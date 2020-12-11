# coding: utf-8

"""
    sbml4j API

    This is the api for the SBML4j Service   # noqa: E501

    OpenAPI spec version: 1.1.4
    Contact: thorsten.tiede@uni-tuebingen.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pysbml4j
from pysbml4j.api.warehouse_api import WarehouseApi  # noqa: E501
from pysbml4j.rest import ApiException


class TestWarehouseApi(unittest.TestCase):
    """WarehouseApi unit test stubs"""

    def setUp(self):
        self.api = WarehouseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_database_uuid(self):
        """Test case for get_database_uuid

        Get the uuid of the databasenode for source with version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
