from datetime import datetime
from pathlib import Path
from textwrap import dedent

try:
    from csscompressor import compress
except ImportError:
    def compress(*__, **_):
        return __[0]

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
    to_write = compress(to_write, preserve_exclamation_comments=False)
    copy(to_write)
    with open(OUTPUT_FILE_NAME, 'w') as out:
        out.write(
            dedent(
                f'''\
            /* ==UserStyle==
            @name         Google - Clean Dark Extended
            @namespace    _GCDE_
            @homepageURL  https://github.com/Mattwmaster58/google-clean-darkx
            @version      1.0.0
            @license      CC-NC-SA
            @description  Theme everything google
            @author       Mattwmaster58 et al.
            ==/UserStyle== */
            /*
            Built on {datetime.utcnow()}
            DO NOT MODIFY THIS FILE DIRECTLY! Instead, modify the appropriate CSS file in the ./css directory
            */\n\n'''
            )
        )
        out.write(to_write)


if __name__ == '__main__':
    main()
