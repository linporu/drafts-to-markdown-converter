import pytest
from helper import *


@pytest.mark.parametrize("valid_input, expected", [

("1234-11-02T22:56:59Z", "341102"),

])
def test_clean_ts_YYMMDD_expected(valid_input, expected):

	assert clean_ts_YYMMDD(valid_input) == expected