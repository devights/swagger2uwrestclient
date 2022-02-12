"""
Contains UW {{ client }} name DAO implementations.
"""
from restclients_core.dao import DAO
from os.path import abspath, dirname
import os


class {{client}}_DAO(DAO):
    def service_name(self):
        return '{{client}}'

    def service_mock_paths(self):
        path = [abspath(os.path.join(dirname(__file__), "resources"))]
        return path