from pathlib import Path

from employee_attrition.utils.common import (
    read_yaml,
    create_directories,
)

config = read_yaml(Path("config/config.yaml"))

print(config)

create_directories([
    Path("sample_folder"),
    Path("another_folder"),
])