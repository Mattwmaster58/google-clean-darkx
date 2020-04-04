from datetime import datetime
from pathlib import Path
from textwrap import dedent

"""
For building main theme
"""

OUTPUT_FILE_NAME = 'google-clean-darkx.user.css'


def main():
    with open(OUTPUT_FILE_NAME, 'w') as out:
        out.write(dedent(f'''\
        /*
        Built on {datetime.utcnow()}
        DO NOT MODIFY THIS FILE DIRECTLY! Instead, modify the appropriate CSS file in the ./css directory
        */\n\n'''))
        # we want main and global styles to be overridden not the other way around
        for file in sorted(Path('./css').iterdir(), key=lambda f: 'main' in f.name or 'global' in f.name):
            with open(file) as inf:
                out.write(inf.read())


if __name__ == '__main__':
    main()
