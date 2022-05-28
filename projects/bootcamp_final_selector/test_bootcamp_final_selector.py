import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import bootcamp_final_selector

class TestBootcampFinalSelector(unittest.TestCase):
    @patch("sys.stdin", StringIO("StudentA\n"))
    def test_user_name(self):
        output = StringIO()
        sys.stdout = output

        bootcamp_final_selector.user_name()
        self.assertEqual(output.getValue(), '''Enter username: ''')


    def test_file_exists(self):
        boolean = os.path.isfile("./student_results.txt")
        self.assertEqual(boolean, True)


    def test_read_file(self):
        pass


    def test_calculate_exam_av(self):
        pass


    def test_calculate_group_project_av(self):
        pass


    def test_calculate_daily_exercise(self):
        pass


    def test_first_class_or_av_pass(self):
        pass


    def test_user_status(self):
        pass

if __name__ == '__main__':
    unittest.main()
