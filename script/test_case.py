import pytest
from common.code.case import Case_result
from common.yaml_common.yaml_util import YamlReader
@pytest.mark.parametrize('case_data', YamlReader().read_case('data.yaml'))
def test_main(case_data: dict):
    print(Case_result.case_assert_result(case_data))
