from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the Data Ingestion stage.
    """

    root_dir: Path
    source_file: Path
    local_data_file: Path
    train_data_path: Path
    test_data_path: Path
    test_size: float
    random_state: int
    target_column: str


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    validation_status: Path
    schema: dict
    columns_count: int
    target_column: str


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    preprocessor_path: Path
    target_column: str


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    metrics_file_path: Path

    C: float
    kernel: str
    gamma: str
    class_weight: str
    probability: bool
    random_state: int


@dataclass(frozen=True)
class PredictionConfig:
    """
    Configuration for the Prediction Pipeline.
    """

    model_path: Path
    preprocessor_path: Path