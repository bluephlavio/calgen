import calendar
from datetime import date

from calgen.jinja_env import get_jinja_env
from calgen.localization import get_localized_names


def build_month(year, month, month_names, weekday_names):
    _, last_day = calendar.monthrange(year, month)
    days = []
    for day in range(1, last_day + 1):
        d = date(year, month, day)
        dow = d.weekday()
        days.append({
            "number": day,
            "name": weekday_names[dow],
            "is_sunday": (dow == SUNDAY),
            "note": ""
        })
    return {
        "month_name": month_names[month - 1],
        "year": year,
        "days": days
    }


def generate_calendar_tex(
    start: date,
    end: date,
    output_path: str = "calendario.tex",
    template_name: str = "basic.tex.j2",
    locale: str = "en"
):
    env = get_jinja_env()
    template = env.get_template(template_name)
    month_names, weekday_names = get_localized_names(locale)
    months = []
    current = start
    while current <= end:
        year = current.year
        month = current.month
        months.append(build_month(year, month, month_names, weekday_names))
        # advance to next month
        current = (
            date(year + 1, 1, 1)
            if month == DECEMBER
            else date(year, month + 1, 1)
        )
    calendar_tex = template.render(months=months)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(calendar_tex)


SUNDAY = 6
DECEMBER = 12
