import unittest
from eventhandler.eventhandler import EventHandler, Dictionary


class TestEventHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Dictionary()

    def setUp(self):
        self.handler = EventHandler()

    def tearDown(self):
        del self.handler
        Dictionary.clear()

    def test_new_group(self):
        pass


if __name__ == '__main__':
    unittest.main()
