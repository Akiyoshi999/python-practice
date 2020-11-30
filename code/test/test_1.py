import unittest
import Cal


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = Cal.Cal()
        self.assertEqual(cal.add_num_and_doble(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
