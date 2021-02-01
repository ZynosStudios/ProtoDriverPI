import unittest
import os

from protodriverpi.app import app


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

