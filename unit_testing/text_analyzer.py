import unittest
import os


def analyze_text(filename):
    """
    Calculate the number of lines and characters in a file.

    :param filename: The name of the file to analyze.

    Raises:
        IOError: If 'filename' does not exist or can't be read.

    Returns:
        The number of lines in the file.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """
    Tests for the 'analyze_text()' function.
    """

    # Function that runs before each test method
    def setUp(self):
        """
        Fixture that creates a file for the text methods to use.
        """
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Testing file.\n'
                    'For unit testing\n'
                    'We need few lines to test different methods.\n'
                    'To check that everything is ok.')

    # tearDown run after each test method
    def tearDown(self):
        """
        Fixture that deletes the files used by the test methods.
        """
        try:
            os.remove(self.filename)
        except:
            # Предполагаем, что любой сбой приемлимый, чтобы лишний раз не бросать искоючения
            pass

    def test_function_runs(self):
        """
        Basic smoke test: does the function run.
        """
        analyze_text(self.filename)

    def test_line_count(self):
        """
        Check that the line count is correct.
        """
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 107)

    def test_no_such_file(self):
        """
        Check the proper exception is thrown for a missing file.
        """
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        """
        Check that the function doesn't delete the input file.
        """
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()