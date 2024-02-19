import unittest
from redirect import Redirect


class TestRedirect(unittest.TestCase):
    @staticmethod
    def _redirect_to_files():
        print('Hello stdout in test')
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        print('Hello stdout in test again')
        stdout_file.close()
        stderr_file.close()

    def test_redirect_to_files(self):
        self._redirect_to_files()
        with self.assertRaises(RuntimeError):
            raise RuntimeError('Hello stderr in test')

        with (
            open('stdout.txt') as stdout_file,
            open('stderr.txt') as stderr_file
        ):
            out, err = stdout_file.read(), stderr_file.read()
            self.assertNotIn('Hello stdout in test', out)
            self.assertIn('Hello stdout.txt', out)
            self.assertNotIn('Hello stdout again', out)
            self.assertNotIn('Hello stderr in test', err)
            self.assertIn('Hello stderr.txt', err)


if __name__ == '__main__':
    unittest.main()
