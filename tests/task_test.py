import unittest
from src.task import *
from src.task_decider import *

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash Dishes", 30)

    def test_has_description(self):
        self.assertEqual("Wash Dishes", self.task1.description)

    def test_has_duration(self):
        self.assertEqual(30, self.task1.duration)