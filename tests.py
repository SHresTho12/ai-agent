from functions.get_files_info import get_files_info , get_file_content
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
        
class TestGetFileContent(unittest.TestCase):
    # def test_get_file_content_no_file(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     print(result[-100:])
    def test_get_file_content_valid_file(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)  
        self.assertTrue(len(result) > 0)
    def test_get_file_content_pkg_file(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertIsInstance(result, str)  
        self.assertTrue(len(result) > 0)
    def test_get_file_content_invalid_file(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertTrue(result.startswith('Error: Cannot access'))

if __name__ == "__main__":
    unittest.main()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGetFilesInfo)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

