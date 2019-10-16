import datetime
import unittest
from more_fun_with_collections import date_time


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.date(2020, 1, 1)
        later_half_birthday = datetime.date(2020, 7, )
        self.assertEqual(date_time.half_birthday(birthday), later_half_birthday )


if __name__ == '__main__':
    unittest.main()
