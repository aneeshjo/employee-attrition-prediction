from pathlib import Path

from employee_attrition.entity.config_entity import DataIngestionConfig


config = DataIngestionConfig(
    root_dir=Path("artifacts"),
    source_URL="sample.csv",
    local_data_file=Path("dataset.csv"),
    train_data_path=Path("train.csv"),
    test_data_path=Path("test.csv"),
    test_size=0.2,
    random_state=42,
)

print(config)