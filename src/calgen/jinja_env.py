import os

from jinja2 import Environment, FileSystemLoader


def get_jinja_env():
    """Restituisce un ambiente Jinja2 configurato per LaTeX."""
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
    return Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=False,
        block_start_string='((*',
        block_end_string='*))',
        variable_start_string='(((',
        variable_end_string=')))',
        comment_start_string='((#',
        comment_end_string='#))'
    )