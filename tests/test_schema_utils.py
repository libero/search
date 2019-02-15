from pathlib import Path

import pytest
from lxml import etree

from tests.schema_utils import (MultipleFilesFound, SchemasDirectoryNotFound,
                                get_schema_file_path, get_schemas_base_path)


def test_get_schemas_base_path_raises_exception() -> None:
    with pytest.raises(SchemasDirectoryNotFound):
        get_schemas_base_path('non-existent-schemas-lib')


def test_get_schema_file_path_returns_file_path() -> None:
    """
    Checks that the schemas are installed, a file path is returned and can
    be parsed by lxml.
    """
    path = get_schema_file_path('item-list.rng')
    etree.parse(path)


def test_get_schema_file_path_raises_multiple_files_found_exception(mocker) -> None:
    mocker.patch('tests.schema_utils.get_schemas_base_path', new=lambda: '/path/to/schemas/')
    mocker.patch.object(Path,
                        'glob',
                        new=lambda self, arg: ['/path/to/schemas/test-file',
                                               '/path/to/schemas/folder/test-file'])
    with pytest.raises(MultipleFilesFound):
        get_schema_file_path('test-file')


def test_get_schema_file_path_raises_file_not_found_exception(mocker) -> None:
    mocker.patch('tests.schema_utils.get_schemas_base_path', new=lambda: '/path/to/schemas/')
    with pytest.raises(FileNotFoundError):
        get_schema_file_path('test-file')
