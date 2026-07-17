from pathlib import Path
from typing import Any

import yaml
import joblib
from box import ConfigBox
from ensure import ensure_annotations

from employee_attrition.logger import logger
from employee_attrition.exception import CustomException
import sys


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns it as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: YAML content accessible using dot notation.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

        logger.info(f"YAML file loaded successfully: {path_to_yaml}")

        return ConfigBox(content)

    except Exception as e:
        logger.exception("Failed to read YAML file.")
        raise CustomException(e, sys)
    

def create_directories(
    paths: list[Path],
    verbose: bool = True,
) -> None:
    """
    Create multiple directories.

    Args:
        paths (list[Path]): List of directories.
        verbose (bool): Log directory creation.
    """

    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

        if verbose:
            logger.info(f"Created directory: {path}")

def save_object(file_path,obj):

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(obj,file_path)

def load_object(file_path):

    """
    Loads a saved Joblib object.
    """

    return joblib.load(file_path)

