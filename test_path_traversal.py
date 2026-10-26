import os
import unittest
from sandbox import ResearchSandbox, ResearchObject

class TestPathTraversal(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.getcwd()
        self.sandbox = ResearchSandbox(objects=[])
        self.valid_filename = "test_valid.json"

        # Ensure cleanup from any previous runs
        if os.path.exists(self.valid_filename):
            os.remove(self.valid_filename)

    def tearDown(self):
        if os.path.exists(self.valid_filename):
            os.remove(self.valid_filename)

    def test_valid_path(self):
        # Should not raise exception
        self.sandbox.to_json(self.valid_filename, base_dir=self.base_dir)
        self.assertTrue(os.path.exists(self.valid_filename))

        read_sandbox = ResearchSandbox.from_json(self.valid_filename, base_dir=self.base_dir)
        self.assertIsInstance(read_sandbox, ResearchSandbox)

    def test_invalid_path_to_json(self):
        # Should raise ValueError
        with self.assertRaises(ValueError):
            self.sandbox.to_json("../test_invalid.json", base_dir=self.base_dir)

        with self.assertRaises(ValueError):
            self.sandbox.to_json("/etc/passwd", base_dir=self.base_dir)

    def test_invalid_path_from_json(self):
        # Should raise ValueError
        with self.assertRaises(ValueError):
            ResearchSandbox.from_json("../test_invalid.json", base_dir=self.base_dir)

        with self.assertRaises(ValueError):
            ResearchSandbox.from_json("/etc/passwd", base_dir=self.base_dir)

if __name__ == '__main__':
    unittest.main()
