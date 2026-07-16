from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the Data Ingestion stage.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    train_data_path: Path
    test_data_path: Path
    test_size: float
    random_state: int
