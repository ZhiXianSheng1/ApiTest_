import pytest
from common.code.case import case_assert_result
from common.yaml_common.yaml_util import YamlReader


@pytest.mark.parametrize('case_data', YamlReader().read_case('data.yaml'))
def test_main(case_data: dict):
    print(case_assert_result(case_data))
