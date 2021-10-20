import unittest

from python_repos_visual import api_call

class VisualTestMethods(unittest.TestCase):
    """Tests for 'python_repos_visual.py'"""

    def test_status_code(self):
        """Does the status code equal 200?"""
        url = f'https://api.github.com/search/repositories?q=language:python&sort=stars'
        status_code = api_call('python', url).status_code
        self.assertEqual(200, status_code) 

if __name__ == '__main__':
    unittest.main()