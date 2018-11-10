import pytest
from . import test_data_path, test_files

import pandasdmx
from pandasdmx.writer.structure2pd import Writer


@pytest.fixture
def dsd_common():
    return pandasdmx.open_file(test_data_path / 'common' / 'common.xml')


@pytest.mark.xfail(reason='writer.structure2pd needs refactor')
def test_writer(dsd_common):
    Writer(None).write(dsd_common)


@pytest.mark.parametrize('path', **test_files(kind='structure'))
def test_writer_many(path):
    msg = pandasdmx.open_file(path)
    Writer(None).write(msg)
