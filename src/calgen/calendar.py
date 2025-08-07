import os
from datetime import date

from .generator import generate_calendar_tex


def generate_calendar(
    start: date,
    end: date,
    template: str = "basic",
    out: str = ".",
    locale: str = "en"
):
    """Generate a LaTeX calendar between two dates and save it to calendar.tex."""
    template_name = f"{template}.tex.j2"
    output_path = os.path.join(out, "calendar.tex")
    generate_calendar_tex(start, end, output_path, template_name, locale)
