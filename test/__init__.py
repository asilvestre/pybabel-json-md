from subprocess import PIPE, Popen
import re
import os
import unittest


class TestExtraction(unittest.TestCase):
    def setUp(self):
        global dirname
        dirname = os.path.dirname(os.path.abspath(__file__))

    dirname = None

    def test_number_of_occurences(self):
        stderr = None if 'PYBABEL_JSON_MD_DEBUG' in os.environ else PIPE
        global dirname
        cfg = os.path.join(dirname, 'babel.cfg')
        pot_file = os.path.join(dirname, 'messages.pot')
        self.found_transes = Popen(['pybabel', '-v', 'extract',
                                    '-F', cfg, '-o', pot_file, '.'],
                                   stdout=PIPE, stderr=stderr).stdout.read()
        with open(pot_file, 'r') as output:
            self.output = output.read()

        self.assertEqual(len(re.findall(r'msgid "', self.output)), 1+19,
                         "Wrong number of found translations")
        self.assertEqual(len(re.findall(r'msgid_plural', self.output)), 0,
                         "Wrong number of plural translations")
        os.remove(pot_file)

    def test_number_of_occurences_2(self):
        global dirname
        stderr = None if 'PYBABEL_JSON_MD_DEBUG' in os.environ else PIPE
        cfg = os.path.join(dirname, 'babel2.cfg')
        pot_file = os.path.join(dirname, 'messages2.pot')
        self.found_transes = Popen(['pybabel', '-v', 'extract',
                                    '-F', cfg, '-o', pot_file, '.'],
                                   stdout=PIPE, stderr=stderr).stdout.read()
        with open(pot_file, 'r') as output:
            self.output = output.read()

        self.assertEqual(len(re.findall(r'msgid "', self.output)), 1+30,
                         "Wrong number of found translations")
        self.assertEqual(len(re.findall(r'msgid_plural', self.output)), 0,
                         "Wrong number of plural translations")
        os.remove(pot_file)

if __name__ == '__main__':
    unittest.main()