#!/Users/christo/.pyenv/versions/3.9.16/envs/b2b-infrastructure/bin/python

import re
import sys
from poetry.console.application import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())

"""
import os
import sys

if { k for k in os.environ.keys() if 'PYCHARM' in k }:
    import pathlib

    RELATIVE_SOURCE_PATHS = [
        #'../../github.com/python-poetry/poetry-core',
        #'../../github.com/python-poetry/poetry',
        '..',
        '',
    ]
    RELATIVE_SOURCE_PATHS.reverse()
    here = pathlib.PosixPath(__file__)
    project = here.parent

    for rel_path in RELATIVE_SOURCE_PATHS:
        path = project / rel_path
        path_s = os.path.realpath(str(path))
        if not path.is_dir():
            raise Exception(f'From {project} -> {path_s}')
        sys.path.insert(0, path_s)

if __name__ == "__main__":
    from poetry.console.application import main

    sys.exit(main())
"""