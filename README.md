# calgen

A Python CLI tool to generate LaTeX calendars for custom date ranges using Jinja2 templates.

## Features
- Generate monthly calendars between any two dates
- Customizable LaTeX templates (default: `basic`)
- Easy CLI usage via [Typer](https://typer.tiangolo.com/)

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd calgen
   ```
2. Create and activate a virtual environment (recommended):
   ```sh
   python3 -m venv activate
   source activate/bin/activate
   ```
3. Install dependencies and calgen in editable mode:
   ```sh
   uv pip install -e .
   ```

## Usage

Generate a calendar from September 2025 to June 2026:
```sh
calgen 2025-09-01 2026-06-30 --template basic
```

- `start`: Start date (YYYY-MM-DD)
- `end`: End date (YYYY-MM-DD)
- `--template`: Template name (default: basic)
- `--out`: Output folder (default: current directory)

The generated LaTeX file will be saved as `calendar.tex` in the specified output folder.

## Project Structure
```
calgen/
├── src/
│   └── calgen/
│       ├── cli.py
│       ├── calendar.py
│       ├── generator.py
│       ├── jinja_env.py
│       ├── constants.py
│       └── templates/
│           └── basic.tex.j2
├── pyproject.toml
├── README.md
```

## License
MIT
