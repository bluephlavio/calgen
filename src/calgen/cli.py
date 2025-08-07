# src/cli.py

from datetime import date

import typer

from .calendar import generate_calendar


def main(
    start: str = typer.Argument(..., help="Start date (YYYY-MM-DD)"),
    end: str = typer.Argument(..., help="End date (YYYY-MM-DD)"),
    template: str = typer.Option("basic", help="Template name to use (default: basic)"),
    out: str = typer.Option(
        ".", "--out",
        help="Output folder for the tex file (default: current directory)"
    ),
    locale: str = typer.Option(
        "en", "--locale",
        help="Locale for month and weekday names (e.g., 'en', 'it')"
    )
):
    """Generate a calendar between two dates."""
    try:
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
    except ValueError:
        typer.echo("Invalid date format. Use YYYY-MM-DD.")
        raise typer.Exit(code=1) from None
    generate_calendar(start_date, end_date, template, out, locale)


def app():
    typer.run(main)

if __name__ == "__main__":
    app()
