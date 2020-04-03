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
        for file in Path('./css').iterdir():
            with open(file) as inf:
                out.write(inf.read())


if __name__ == '__main__':
    main()
