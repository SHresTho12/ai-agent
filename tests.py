from functions.get_files_info import get_files_info , get_file_content, write_file
from functions.run_python import run_python_file
import unittest
import os

# class TestGetFilesInfo(unittest.TestCase):
#     def test_get_files_info_valid_directory(self):
#         result = get_files_info("calculator", ".")
#         print(result)
#         self.assertIsNone(result)  
#     def test_get_files_info_pkg_directory(self):
#         result = get_files_info("calculator", "pkg")
#         print(result)
#         self.assertIsNone(result)  
#     def test_get_files_info_invalid_directory(self):    
#         result = get_files_info("calculator", "/bin")
#         print(result)
#         self.assertTrue(result.startswith('Error: Cannot list'))  
#     def test_get_files_info_outside_directory(self):
#         result = get_files_info("calculator", "../")
#         print(result)
#         self.assertTrue(result.startswith('Error: Cannot list'))  
        
# class TestGetFileContent(unittest.TestCase):
#     # def test_get_file_content_no_file(self):
#     #     result = get_file_content("calculator", "lorem.txt")
#     #     print(result[-100:])
#     def test_get_file_content_valid_file(self):
#         result = get_file_content("calculator", "main.py")
#         print(result)
#         self.assertIsInstance(result, str)  
#         self.assertTrue(len(result) > 0)
#     def test_get_file_content_pkg_file(self):
#         result = get_file_content("calculator", "pkg/calculator.py")
#         print(result)
#         self.assertIsInstance(result, str)  
#         self.assertTrue(len(result) > 0)
#     def test_get_file_content_invalid_file(self):
#         result = get_file_content("calculator", "/bin/cat")
#         print(result)
#         self.assertTrue(result.startswith('Error: Cannot access'))
#

class TestWriteFileContent(unittest.TestCase):

    def test_lorem_txt(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_pkg_morelorem_txt(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_disallowed_temp_txt(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)


class TestPythonFileRun(unittest.TestCase):

    def test_calc_usage_instructions(self):
        result = run_python_file("calculator", "main.py")
        print("\nTest: calculator/main.py (usage instructions)\n", result)
        self.assertIsInstance(result, str)

    def test_calc_with_expression(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print("\nTest: calculator/main.py with args ['3 + 5']\n", result)
        self.assertIsInstance(result, str)

    def test_run_tests_py(self):
        result = run_python_file("calculator", "tests.py")
        print("\nTest: calculator/tests.py\n", result)
        self.assertIsInstance(result, str)

    def test_outside_directory(self):
        result = run_python_file("calculator", "../main.py")
        print("\nTest: calculator/../main.py (outside directory)\n", result)
        self.assertIn("outside the permitted working directory", result)

    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print("\nTest: calculator/nonexistent.py (not found)\n", result)
        self.assertIn("not found", result)

    
 

if __name__ == "__main__":
    unittest.main()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestWriteFileContent)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

