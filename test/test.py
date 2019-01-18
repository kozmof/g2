import sys
sys.path.append("..")

import os
from os import environ
import g2_lib
import unittest


class TestG2(unittest.TestCase):
    def test_load_path(self):
        expected_path_list = [(0, '0'), (1, '1'), (2, '2')]
        with open("test.txt", "w") as f:
            f.write("0\n")
            f.write("1\n")
            f.write("2\n")

        path_list =  g2_lib.load_path("test.txt")
        self.assertEqual(path_list, expected_path_list)

    def test_write_path(self):
        with open("test.txt", "w") as f:
            f.write("")

        g2_lib.write_path("test.txt") 

        with open("test.txt", "r") as f:
            line = f.read()
            self.assertEqual(line, os.getcwd() + "\n")

    def test_write_path_with_pos(self):
        with open("test.txt", "w") as f:
            f.write("")

        g2_lib.write_path_with_pos("test_dir1", "test.txt") 
        g2_lib.write_path_with_pos("test_dir2", "test.txt") 

        with open("test.txt", "r") as f:
            line = f.readlines()
            expected_result1 = os.path.realpath("test_dir1") + '\n'
            expected_result2 = os.path.realpath("test_dir2") + '\n'
            self.assertEqual(line[0], expected_result1)
            self.assertEqual(line[1], expected_result2)

    def test_write_path_to_top(self):
        with open("test.txt", "w") as f:
            f.write("test\n")

        g2_lib.write_path_to_top("test.txt")

        with open("test.txt", "r") as f:
            line = f.readlines()
            self.assertEqual(line[0], os.getcwd() + "\n")
            self.assertEqual(line[1], "test\n")

    def test_write_path_with_pos_to_top(self):
        with open("test.txt", "w") as f:
            f.write("")

        g2_lib.write_path_with_pos_to_top("test_dir1", "test.txt") 
        g2_lib.write_path_with_pos_to_top("test_dir2", "test.txt") 

        with open("test.txt", "r") as f:
            line = f.readlines()
            expected_result1 = os.path.realpath("test_dir2") + '\n'
            expected_result2 = os.path.realpath("test_dir1") + '\n'
            self.assertEqual(line[0], expected_result1)
            self.assertEqual(line[1], expected_result2)

    def test_delete_path(self):
        with open("test.txt", "w") as f:
            f.write("test")

        g2_lib.delete_path(0, "test.txt")

        with open("test.txt", "r") as f:
            lines = f.read()
            self.assertEqual(lines, "")

    def test_range_delete(self):
        with open("test.txt", "w") as f:
            f.write("test1\n")
            f.write("test2\n")
            f.write("test3\n")

        g2_lib.range_delete(0, 1, "test.txt")

        with open("test.txt", "r") as f:
            lines = f.read()
            self.assertEqual(lines, "test3\n")

    def test_swap_order(self):
        with open("test.txt", "w") as f:
            f.write("0" + "\n")
            f.write("1" + "\n")
            f.write("2" + "\n")

        g2_lib.swap_order(0, 2, "test.txt")

        with open("test.txt", "r") as f:
            lines = f.read()
            self.assertEqual(lines, "2\n1\n0\n")

    def test_reverse(self):
        with open("test.txt", "w") as f:
            f.write("0" + "\n")
            f.write("1" + "\n")

        g2_lib.reverse("test.txt")

        with open("test.txt", "r") as f:
            lines = f.read()
            self.assertEqual(lines, "1\n0\n")

    @unittest.skip("This test moves a current directry")
    def test_jump(self):
        with open("test.txt", "w") as f:
            f.write("/" + "\n")

        g2_lib.jump(0, "test.txt")
        self.assertEqual(os.getcwd(), "/")

if __name__ == "__main__":
    unittest.main()
