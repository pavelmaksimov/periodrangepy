# -*- coding: utf-8 -*-
import datetime as datetime_
from datetime import datetime

import pendulum
import pytest

from periodrangepy import *


@pytest.mark.parametrize(
    "start_date,end_date,"
    "delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        ("2017-01-01", "2017-01-01", 1, False, False, "2017-01-01", "2017-01-01", 1),
        ("2017-01-01", "2017-01-03", 1, False, False, "2017-01-01", "2017-01-01", 3),
        ("2017-01-01", "2017-01-01", 2, False, False, "2017-01-01", "2017-01-01", 1),
        ("2017-01-01", "2017-01-10", 30, False, False, "2017-01-01", "2017-01-10", 1),
        ("2017-01-01", "2017-01-10", 5, False, False, "2017-01-01", "2017-01-05", 2),
    ],
)
def test_period_day_range(
    start_date,
    end_date,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="day",
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "num,delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        ("2017-01-01", None, 0, 1, False, False, "2017-01-01", "2017-01-01", 1),
        ("2017-01-01", None, 1, 1, False, False, "2017-01-01", "2017-01-01", 2),
        ("2017-01-01", None, 1, 2, False, False, "2017-01-01", "2017-01-02", 1),
        ("2017-01-01", None, 2, 2, False, False, "2017-01-01", "2017-01-02", 2),
    ],
)
def test_period_day_without_end_date_range(
    start_date,
    end_date,
    num,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="day",
        num=num,
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "num,delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        (
            "2017-01-02",
            "2017-01-08",
            None,
            1,
            False,
            False,
            "2017-01-02",
            "2017-01-08",
            1,
        ),
        (
            "2017-01-03",
            "2017-01-07",
            None,
            1,
            False,
            False,
            "2017-01-03",
            "2017-01-07",
            1,
        ),
        (
            "2017-01-03",
            "2017-01-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-01-14",
            1,
        ),
        (
            "2017-01-03",
            "2017-01-20",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-01-15",
            2,
        ),
        (
            "2017-01-03",
            "2017-01-14",
            None,
            1,
            False,
            False,
            "2017-01-03",
            "2017-01-08",
            2,
        ),
    ],
)
def test_period_week_range(
    start_date,
    end_date,
    num,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="week",
        num=num,
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "num,delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        (
            "2017-01-02",
            "2017-01-08",
            None,
            1,
            False,
            False,
            "2017-01-02",
            "2017-01-08",
            1,
        ),
        (
            "2017-01-03",
            "2017-02-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-02-14",
            1,
        ),
        (
            "2017-01-03",
            "2017-02-14",
            None,
            1,
            False,
            False,
            "2017-01-03",
            "2017-01-31",
            2,
        ),
        (
            "2017-01-03",
            "2017-03-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-02-28",
            2,
        ),
    ],
)
def test_period_month_range(
    start_date,
    end_date,
    num,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="month",
        num=num,
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "num,delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        (
            "2017-01-02",
            "2017-01-08",
            None,
            1,
            False,
            False,
            "2017-01-02",
            "2017-01-08",
            1,
        ),
        (
            "2017-01-03",
            "2017-02-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-02-14",
            1,
        ),
        (
            "2017-01-03",
            "2017-04-14",
            None,
            1,
            False,
            False,
            "2017-01-03",
            "2017-03-31",
            2,
        ),
        (
            "2017-01-03",
            "2017-07-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-06-30",
            2,
        ),
    ],
)
def test_period_quarter_range(
    start_date,
    end_date,
    num,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="quarter",
        num=num,
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "num,delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency,"
    "result_date1,result_date2,"
    "lenght",
    [
        (
            "2017-01-02",
            "2017-01-08",
            None,
            1,
            False,
            False,
            "2017-01-02",
            "2017-01-08",
            1,
        ),
        (
            "2017-01-03",
            "2017-02-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2017-02-14",
            1,
        ),
        (
            "2017-01-03",
            "2018-04-14",
            None,
            1,
            False,
            False,
            "2017-01-03",
            "2017-12-31",
            2,
        ),
        (
            "2017-01-03",
            "2019-07-14",
            None,
            2,
            False,
            False,
            "2017-01-03",
            "2018-12-31",
            2,
        ),
    ],
)
def test_period_year_range(
    start_date,
    end_date,
    num,
    delta,
    result_date1,
    result_date2,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
    lenght,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="year",
        num=num,
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)
    assert result[0]["date1_str"] == result_date1
    assert result[0]["date2_str"] == result_date2
    assert len(result) == lenght


@pytest.mark.parametrize(
    "start_date,end_date,"
    "delta,"
    "adjustment_start_date_by_frequency,"
    "adjustment_end_date_by_frequency",
    [
        (
            datetime(2016, 1, 1).date(),
            datetime(2019, 1, 16, 1, 1, 1, 1),
            366,
            True,
            False,
        )
    ],
)
def test_period_year_range_custom(
    start_date,
    end_date,
    delta,
    adjustment_start_date_by_frequency,
    adjustment_end_date_by_frequency,
):
    result = period_range(
        start_date=start_date,
        end_date=end_date,
        frequency="year",
        delta=delta,
        as_dict=True,
        string_format="%Y-%m-%d",
    )
    print(result)


@pytest.mark.parametrize(
    "dt",
    [
        datetime(2016, 1, 1),
        datetime(2016, 1, 1).date(),
        datetime.timestamp(datetime(2016, 1, 1)),
        pendulum.now(),
        pendulum.now().date(),
    ],
)
def test_to_pydatetime(dt):
    isinstance(dt, datetime_.datetime)


def test_to_start_of_week():
    r = to_start_of_week(datetime(2019, 8, 26))
    assert r == datetime(2019, 8, 26)
    r2 = to_start_of_week(datetime(2019, 8, 27))
    assert r2 == datetime(2019, 8, 26)


def test_to_end_week():
    r = to_end_week(datetime(2019, 9, 1))
    assert r == datetime(2019, 9, 1)
    r2 = to_end_week(datetime(2019, 8, 27))
    assert r2 == datetime(2019, 9, 1)


def test_to_start_of_month():
    r = to_start_of_month(datetime(2019, 8, 1))
    assert r == datetime(2019, 8, 1)
    r2 = to_start_of_month(datetime(2019, 8, 2))
    assert r2 == datetime(2019, 8, 1)


def test_to_end_month():
    r = to_end_month(datetime(2019, 8, 31))
    assert r == datetime(2019, 8, 31)
    r2 = to_end_month(datetime(2019, 8, 27))
    assert r2 == datetime(2019, 8, 31)


def test_to_start_of_quarter():
    r = to_start_of_quarter(datetime(2019, 1, 1))
    assert r == datetime(2019, 1, 1)
    r2 = to_start_of_quarter(datetime(2019, 1, 2))
    assert r2 == datetime(2019, 1, 1)


def test_to_end_quarter():
    r = to_end_quarter(datetime(2019, 3, 31))
    assert r == datetime(2019, 3, 31)
    r2 = to_end_quarter(datetime(2019, 3, 27))
    assert r2 == datetime(2019, 3, 31)


def test_to_start_of_year():
    r = to_start_of_year(datetime(2019, 1, 1))
    assert r == datetime(2019, 1, 1)
    r2 = to_start_of_year(datetime(2019, 1, 2))
    assert r2 == datetime(2019, 1, 1)


def test_to_end_year():
    r = to_end_year(datetime(2019, 12, 31))
    assert r == datetime(2019, 12, 31)
    r2 = to_end_year(datetime(2019, 12, 27))
    assert r2 == datetime(2019, 12, 31)
