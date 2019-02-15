import sys
from pathlib import Path


class SchemasDirectoryNotFound(Exception):
    pass


class MultipleFilesFound(Exception):
    pass


def get_schemas_base_path(lib_name: str = 'libero-schemas') -> str:
    for path in sys.path:
        if lib_name in path:
            return path
    raise SchemasDirectoryNotFound(
        f'Unable to find {lib_name} directory. {lib_name} not in sys.path')


def get_schema_file_path(name: str) -> str:
    path = Path(get_schemas_base_path())
    matches = [match for match in path.glob('**/%s' % name)]
    if len(matches) > 1:
        message = 'Multiple files found: ' + ' '.join([str(m) for m in matches])
        raise MultipleFilesFound(message)
    elif matches:
        return str(matches[0])
    raise FileNotFoundError(f'Unable to find {name}')
