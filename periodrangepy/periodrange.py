# -*- coding: utf-8 -*-
import datetime as datetime_
from datetime import datetime, timedelta

from dateutil import relativedelta


def _to_pydatetime(dt):
    """Преобразование в datetime."""
    try:
        if isinstance(dt, str):
            raise TypeError("Дата не должна быть в формате строки")

        if isinstance(dt, datetime_.date):
            # Если тип date.
            dt = datetime.combine(dt, datetime.min.time())

        if isinstance(dt, float):
            # Если тип timestamp.
            dt = datetime.fromtimestamp(dt)

    except Exception as e:
        raise TypeError(
            "Ошибка при преобразовании входных значений даты и времени в pydatetime."
            "Попробуйте сами привести их в формат pydatetime\n"
            + str(e)
        )

    return dt


def to_start_of_minute(dt):
    return dt.replace(second=0, microsecond=0)


def to_end_of_minute(dt):
    return dt.replace(second=59, microsecond=0)


def to_start_of_hour(dt):
    return dt.replace(minute=0, second=0, microsecond=0)


def to_end_of_hour(dt):
    return dt.replace(minute=59, second=59, microsecond=0)


def to_start_of_day(dt):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def to_end_of_day(dt):
    return to_start_of_day(dt) + timedelta(1) - timedelta(seconds=1)


def to_start_of_week(dt):
    return to_start_of_day(dt - timedelta(dt.isoweekday() - 1))


def to_end_of_week(dt):
    return to_start_of_day(dt + timedelta(7 - dt.isoweekday()))


def to_start_of_month(dt):
    return to_start_of_day(dt - timedelta(dt.day - 1))


def to_end_of_month(dt):
    start_next_month = to_start_of_month(dt + relativedelta.relativedelta(months=+1))
    return to_start_of_day(start_next_month - timedelta(1))


def to_start_of_quarter(dt):
    quarter_num = (dt.month - 1) // 3 + 1
    month_num_start_quarter = quarter_num * 3 - 2
    return to_start_of_day(dt.replace(month=month_num_start_quarter, day=1))


def to_end_of_quarter(dt):
    start_next_quarter = to_start_of_quarter(dt) + relativedelta.relativedelta(months=+3)
    return to_start_of_day(start_next_quarter - timedelta(1))


def to_start_of_year(dt):
    return to_start_of_day(datetime(dt.year, 1, 1))


def to_end_of_year(dt):
    return to_start_of_day(datetime(dt.year, 12, 31))


def get_start_period(dt, frequency):
    frequencies = {
        "dayly": lambda dt: dt,
        "date": lambda dt: dt,
        "day": lambda dt: dt,
        "d": lambda dt: dt,
        "w": to_start_of_week,
        "weekly": to_start_of_week,
        "week": to_start_of_week,
        "monthly": to_start_of_month,
        "month": to_start_of_month,
        "m": to_start_of_month,
        "quarter": to_start_of_quarter,
        "quarterly": to_start_of_quarter,
        "q": to_start_of_quarter,
        "year": to_start_of_year,
        "y": to_start_of_year,
    }
    try:
        f = frequencies[frequency]
    except KeyError:
        raise
    else:
        return f(dt)


def get_end_period(dt, frequency):
    frequencies = {
        "dayly": lambda dt: dt + timedelta(1),
        "date": lambda dt: dt + timedelta(1),
        "day": lambda dt: dt + timedelta(1),
        "d": lambda dt: dt + timedelta(1),
        "w": to_end_of_week,
        "weekly": to_end_of_week,
        "week": to_end_of_week,
        "monthly": to_end_of_month,
        "month": to_end_of_month,
        "m": to_end_of_month,
        "quarter": to_end_of_quarter,
        "quarterly": to_end_of_quarter,
        "q": to_end_of_quarter,
        "year": to_end_of_year,
        "y": to_end_of_year,
    }
    try:
        f = frequencies[frequency]
    except KeyError:
        raise
    else:
        return f(dt)


def date_range(start_date,
               end_date=None,
               num=None,
               delta=None,
               return_string_format=False,
               string_format='%Y-%m-%d',
               reverse_sort=False):
    """

    :param start_date: datetime or str (От даты)
    :param end_date: datetime or str (До даты)
    :param delta: int (интервал кол-во дней, между датами)
    :param return_string_format: bool (вернуть в даты в виду строки)
    :param string_format: str (формат выводимых дат в виде строки)
    :param mandatory_end_date: bool (сделать end_date конечной датой, если заданный интервал превысит её)
    :return: list
    """
    if type(delta) is int:
        delta = timedelta(delta)
    else:
        raise TypeError("num должен быть в формате int")

    if not delta:
        return []
    if end_date and start_date > end_date:
        raise ValueError("start_date needs to be before end_date")
    if end_date and num:
        raise ValueError("Either specify end_date OR num")
    if not end_date and not num:
        end_date = datetime.now().date()

    l = []
    if end_date:
        while start_date <= end_date:
            l.append(start_date)
            start_date += delta
        if end_date > l[-1]:
            # Если с выбранным delta интервалом крайняя дата получается больше,
            # чем end_date, она не добавляеся, поэтому добавляется end_date.
            l.append(end_date)
    else:
        for i in range(abs(num)):
            l.append(start_date)
            if num >= 0:
                start_date += delta
            else:
                start_date -= delta

    l.sort(reverse=reverse_sort)

    if return_string_format:
        l = [i.strftime(string_format) for i in l]

    return l


def period_range(
    start_date,
    end_date=None,
    num=None,
    frequency="day",
    delta=1,
    as_dict=False,
    add_date_as_string=True,
    string_format="%Y-%m-%d",
):
    """
    :param start_date: date, datetime, pendulum, timestamp : дата начала периода
    :param end_date: None, date, datetime, pendulum, timestamp : дата конца периода
    :param num: None, int : вместо end_date можно указать здесь кол-во периодов для генерации
    :param frequency: str :
        d|date|day|daily|
        w|week|weekly|
        m|month|monthly|
        q|quarter|quarterly|
        y|yearly|year :
        частота периода, день, неделя, месяц, квартал или год
    :param delta: int : кол-во интервалов
    :param as_dict: bool : вернуть как словарь, по дефолту список списков
    :param add_date_as_string: bool :
        Если as_dict=True, то в словарь можно добавить дату в формате стрингов.
    :param string_format: str : Если add_date_as_string=True, то можно задать формат строки даты
    :return: list(dict), list(list) :
        Если as_dict=False:
        [[dt, dt], [dt, dt]]
        Если as_dict=True:
        [{"date1": dt, "date2": dt}]
        Если as_dict=True и add_date_as_string=True:
        [
            {
                "date1": dt,
                "date2": dt,
                "date1_str": str,
                "date2_str": str
            }
        ]

    """
    start_date = _to_pydatetime(start_date)

    if end_date is None:
        relative_dict = {
            "daily": timedelta(num),
            "date": timedelta(num),
            "day": timedelta(num),
            "d": timedelta(num),
            "weekly": timedelta(weeks=num),
            "week": timedelta(weeks=num),
            "w": timedelta(weeks=num),
            "monthly": timedelta(),
            "month": relativedelta.relativedelta(months=num),
            "m": relativedelta.relativedelta(months=num),
            "quarter": relativedelta.relativedelta(months=3 * num),
            "quarterly": relativedelta.relativedelta(months=3 * num),
            "q": relativedelta.relativedelta(months=3 * num),
            "yearly": relativedelta.relativedelta(years=num),
            "year": relativedelta.relativedelta(years=num),
            "y": relativedelta.relativedelta(years=num),
        }
        end_date = start_date + relative_dict[frequency]
    else:
        end_date = _to_pydatetime(end_date)

    if delta < 1:
        raise Exception

    frequency = frequency.lower()

    d = {"days": +delta}
    w = {"days": +7 * delta}
    m = {"months": +delta}
    q = {"months": +3 * delta}
    y = {"years": +delta}

    frequencies = {
        "daily": d,
        "date": d,
        "day": d,
        "d": d,
        "weekly": w,
        "week": w,
        "w": w,
        "monthly": m,
        "month": m,
        "m": m,
        "quarter": q,
        "quarterly": q,
        "q": q,
        "yearly": y,
        "year": y,
        "y": y,
    }

    start_period = get_start_period(start_date, frequency)
    end_period = get_end_period(end_date, frequency)

    start_periods = []
    end_periods = []
    iter_start_period = start_period
    while iter_start_period < end_period:
        start_periods.append(iter_start_period)
        iter_start_period += relativedelta.relativedelta(**frequencies[frequency])
        end_periods.append(iter_start_period - timedelta(1))

    periods = [[dt1, dt2] for dt1, dt2 in zip(start_periods, end_periods)]

    periods[0][0] = start_date
    periods[-1][1] = end_date

    if as_dict:
        periods_dict = []
        for i in periods:
            date_ = dict(date1=i[0], date2=i[1])
            if add_date_as_string:
                date_.update(
                    date1_str=i[0].strftime(string_format),
                    date2_str=i[1].strftime(string_format),
                )
            periods_dict.append(date_)

        return periods_dict
    else:
        return periods
