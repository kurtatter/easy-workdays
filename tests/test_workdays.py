import unittest
from easy_workdays import WorkCalendar
from datetime import date


class TestWorkCalendar(unittest.TestCase):
    def test_work_day_number(self):
        calendar = WorkCalendar(2024)
        calendar.set_holidays([date(2024, 1, 1)])
        self.assertEqual(calendar.get_work_day_number(date(2024, 1, 2)), 1)


if __name__ == "__main__":
    unittest.main()
