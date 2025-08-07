from babel.dates import get_day_names, get_month_names


def get_localized_names(locale="en"):
    months = list(get_month_names('wide', locale=locale).values())
    weekdays = list(get_day_names('wide', locale=locale).values())
    return months, weekdays
