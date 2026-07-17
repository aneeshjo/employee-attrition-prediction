from employee_attrition.constants import(
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH
)

from employee_attrition.utils.common import (
    read_yaml,
    create_directories
)

from employee_attrition.entity.config_entity import(
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
from pathlib import Path

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH):
        
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        self.schema=read_yaml(schema_file_path)

        create_directories([Path(self.config.artifacts_root)])

    def get_data_ingestion_config(
            self,
            ) -> DataIngestionConfig:
        
        config = self.config.data_ingestion

        params = self.params.data_ingestion

        create_directories(
            [Path(config.root_dir)]
        )
        data_ingestion_config =DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=Path(config.local_data_file),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            test_size=params.test_size,
            random_state=params.random_state
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        schema = self.schema.COLUMNS

        create_directories([Path(config.root_dir)])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            validation_status=Path(config.validation_status),
            all_schema=schema
        )

        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:

        config = self.config.data_transformation
        params=self.params.TARGET_COLUMN

        create_directories([config.root_dir])

        data_transformation_config= DataTransformationConfig(

            root_dir=Path(config.root_dir),

            train_data_path=Path(config.train_data_path),

            test_data_path=Path(config.test_data_path),

            preprocessor_obj_file_path=Path(
                config.preprocessor_obj_file_path
            )

            target_column=params.TARGET_COLUMN
        )

        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerConfig:

        config = self.config.model_trainer

        params = self.params.model_trainer

        create_directories([config.root_dir])

        return ModelTrainerConfig(

            root_dir=Path(config.root_dir),

            trained_model_file_path=Path(config.trained_model_file_path),

            metrics_file_name=Path(config.metrics_file_name),

            C=params.C,

            kernel=params.kernel,

            gamma=params.gamma,

            class_weight=params.class_weight,

            probability=params.probability,

            random_state=params.random_state
        )