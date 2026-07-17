import sys
from pathlib import Path

import joblib
import yaml
from box import ConfigBox
from ensure import ensure_annotations

from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns it as a ConfigBox.
    """

    try:

        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:

            content = yaml.safe_load(yaml_file)

        logger.info(f"Loaded YAML file: {path_to_yaml}")

        return ConfigBox(content)

    except Exception as e:

        logger.exception(f"Failed to read YAML file: {path_to_yaml}")

        raise CustomException(e, sys)


def create_directories(
    paths: list[Path],
    verbose: bool = True
) -> None:
    """
    Creates directories if they do not already exist.
    """

    for path in paths:

        path.mkdir(
            parents=True,
            exist_ok=True
        )

        if verbose:
            logger.info(f"Created directory: {path}")


def save_object(
    file_path: Path,
    obj: object
) -> None:
    """
    Saves a Python object using Joblib.
    """

    try:

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        joblib.dump(obj, file_path)

        logger.info(f"Saved object: {file_path}")

    except Exception as e:

        raise CustomException(e, sys)


def load_object(
    file_path: Path
):
    """
    Loads a Joblib object.
    """

    try:

        obj = joblib.load(file_path)

        logger.info(f"Loaded object: {file_path}")

        return obj

    except Exception as e:

        raise CustomException(e, sys)