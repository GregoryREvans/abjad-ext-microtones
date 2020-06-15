import pytest

import abjad
import abjadext


@pytest.fixture(autouse=True)
def add_libraries(doctest_namespace):
    print(abjad, abjad.__version__)
    doctest_namespace["abjad"] = abjad
    doctest_namespace["abjadext"] = abjadext
    doctest_namespace["microtones"] = abjadext.microtones
