import unittest
from src.task import Task
from src.task_decider import *


class Testtask_decider(unittest.TestCase):
    def setUp(self):
        self.task_dishes = Task("Wash Dishes", 30)
        self.task_dinner = Task("Cook Dinner", 60)
        self.task_windows = Task("Clean Windows", 90)

    def test_get_preferred_option(self):
        self.assertEqual("Wash Dishes", get_preferred_option(
            self.task_dishes, self.task_dinner))
