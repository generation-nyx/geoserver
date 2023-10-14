# coding: utf-8

"""
    GeoServer Importer Extension - Tasks

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The tasks endpoint controls individual tasks within an import job. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.importer_tasks_api import ImporterTasksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestImporterTasksApi(unittest.TestCase):
    """ImporterTasksApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.importer_tasks_api.ImporterTasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_task(self):
        """Test case for delete_task

        Remove task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_get_task(self):
        """Test case for get_task

        Retrieve task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_get_task_layer(self):
        """Test case for get_task_layer

        Retrieve the layer of a task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_get_task_progress(self):
        """Test case for get_task_progress

        Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_get_task_target(self):
        """Test case for get_task_target

        Retrieve the store of a task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_get_tasks(self):
        """Test case for get_tasks

        Retrieve all tasks for import with id {importId}  # noqa: E501
        """
        pass

    def test_post_task(self):
        """Test case for post_task

        Create a new task  # noqa: E501
        """
        pass

    def test_put_task(self):
        """Test case for put_task

        Modify task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_put_task_file(self):
        """Test case for put_task_file

        Create a new task  # noqa: E501
        """
        pass

    def test_put_task_layer(self):
        """Test case for put_task_layer

        Modify the target layer for a task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass

    def test_put_task_target(self):
        """Test case for put_task_target

        Modify the target store for a task with id {taskId} within import with id {importId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
