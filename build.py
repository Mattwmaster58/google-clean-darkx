import re
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from textwrap import dedent

try:
    from csscompressor import compress
except ImportError:

    print('warning: csscompressor not installed')

    def compress(*__, **_):
        return __[0]


OUTPUT_FILE_NAME = Path('google-clean-darkx.min.user.css')
METADATA_FILE = Path('metadata.inf')


def main(version_bump):
    metadata_content = METADATA_FILE.read_text()
    version = dict(
        zip(['major', 'minor', 'patch'], re.search(r'@version\s*(\d+)\.(\d+)\.(\d+)', metadata_content).groups(),)
    )
    if version_bump:
        print(f'bumping {version_bump} component of version string ({version[version_bump]}+1)')
        version[version_bump] = str(int(version[version_bump]) + 1)
        metadata_content = re.sub(
            r'@version(?P<whitespace>\s*)(\d+)\.(\d+)\.(\d+)',
            fr'@version\g<whitespace>{".".join(version.values())}',
            metadata_content,
            re.MULTILINE,
        )
        with open(METADATA_FILE, 'w') as new_meta:
            new_meta.write(metadata_content)
    else:
        print(f'not bumping version, maintaining v{".".join(version.values())}')
    to_write = metadata_content
    to_write += dedent(f'''\
            /*
            Built on {datetime.utcnow()}
            DO NOT MODIFY THIS FILE DIRECTLY! Instead, modify the appropriate CSS file in the ./css directory
            */\n\n''')
    css_main = ''
    # we want main and global styles to be overridden not the other way around
    for file in sorted(Path('./css').iterdir(), key=lambda f: 'main' in f.name or 'global' in f.name):
        with open(file) as inf:
            css_main += inf.read()
    to_write += compress(css_main, preserve_exclamation_comments=False)
    with open(OUTPUT_FILE_NAME, 'w') as out:
        out.write(to_write)


if __name__ == '__main__':
    parser = ArgumentParser('build')
    parser.add_argument('--bump', '-b', type=str, choices=['major', 'minor', 'patch'], default=None)
    parsed = parser.parse_args()
    main(version_bump=parsed.bump)
