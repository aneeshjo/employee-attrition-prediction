from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the Data Ingestion stage.
    """
    root_dir: Path
    source_url: str
    local_data_file: Path
    train_data_path: Path
    test_data_path: Path
    test_size: float
    random_state: int

@dataclass(frozen=True)
class DataValidationConfig:
    """
    Configuration for Data Validation.
    """

    root_dir: Path

    train_data_path: Path

    test_data_path: Path

    validation_status: Path

    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:

    root_dir: Path

    train_data_path: Path

    test_data_path: Path

    preprocessor_obj_file_path: Path

    target_column:str
