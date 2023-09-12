import pytest

from common.Requests_util import Request
from common.yaml_util import YamlReader
# from config.Conf import get_datayaml_file, ConfigYaml
from common import ParameterPool
from common.FilePath_util import FilePath

fp = FilePath()
param_pool = ParameterPool(fp.params_filepath())

