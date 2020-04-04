from datetime import datetime
from pathlib import Path
from textwrap import dedent

try:
    from css_html_js_minify import css_minify
except ImportError:

    def css_minify(inp, *__, **_):
        return inp


try:
    from pyperclip import copy
except ImportError:

    def copy(_):
        pass


"""
For building main theme
"""

OUTPUT_FILE_NAME = 'google-clean-darkx.min.user.css'


def main():
    to_write = ''
    # we want main and global styles to be overridden not the other way around
    for file in sorted(Path('./css').iterdir(), key=lambda f: 'main' in f.name or 'global' in f.name):
        with open(file) as inf:
            to_write += inf.read()
    to_write = css_minify(to_write, sort=True)
    copy(to_write)
    with open(OUTPUT_FILE_NAME, 'w') as out:
        out.write(
            dedent(
                f'''\
            /*
            Built on {datetime.utcnow()}
            DO NOT MODIFY THIS FILE DIRECTLY! Instead, modify the appropriate CSS file in the ./css directory
            */\n\n'''
            )
        )
        out.write(to_write)


if __name__ == '__main__':
    main()
