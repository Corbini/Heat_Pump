import unittest
from eventhandler.objecthandle import Dictionary, Identity


class TestDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Dictionary()

    def tearDown(self):
        Dictionary.clear()

    def test_add(self):
        Dictionary.add("test", 1)

        with self.assertRaises(Exception):
            Dictionary.add("test2", -1)

        with self.assertRaises(Exception):
            Dictionary.add("test3", 1)

    def test_get(self):
        Dictionary.add("test", 5)
        Dictionary.get(5)

        with self.assertRaises(KeyError):
            Dictionary.get(-1)

    def test_find_slot(self):
        identity = Dictionary.find_slot()

        for identity in range(0, 10000):
            Dictionary.add(f"object{identity}", identity)

        identity = Dictionary.find_slot()
        self.assertEqual(identity, None)

    def test_remove(self):
        with self.assertRaises(Exception):
            Dictionary.add("test1", 1)
            Dictionary.remove(1)
            Dictionary.get(1)

        with self.assertRaises(Exception):
            Dictionary.remove(1)


if __name__ == '__main__':
    unittest.main()
