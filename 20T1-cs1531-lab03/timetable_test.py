from timetable import timetable
from datetime import date, time, datetime
import pytest

def test_timetable_one():
    dates = [date(2019,9,27)]
    times = [time(14,10)]
    assert timetable(dates, times) == [datetime(2019,9,27,14,10)]

def test_timetable_two():
    dates = [date(2019,9,27), date(2019,9,30)]
    times = [time(10,30), time(14,10)]
    assert timetable(dates, times) == [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]

def test_empty():
    dates = []
    times = []
    assert timetable(dates, times) == []