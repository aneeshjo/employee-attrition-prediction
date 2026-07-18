from pathlib import Path

from employee_attrition.constants import (
    CONFIG_FILE_PATH,
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH
)

from employee_attrition.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    PredictionConfig
)

from employee_attrition.utils.common import (
    read_yaml,
    create_directories
)


class ConfigurationManager:
    """
    Reads all YAML configuration files and creates
    configuration objects for each pipeline stage.
    """

    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
        schema_file_path=SCHEMA_FILE_PATH
    ):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories(
            [Path(self.config.artifacts_root)]
        )

    # ==========================================================
    # Data Ingestion
    # ==========================================================

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        params = self.params.data_ingestion

        create_directories(
            [Path(config.root_dir)]
        )

        return DataIngestionConfig(

            root_dir=Path(config.root_dir),

            source_file=Path(config.source_file),

            local_data_file=Path(config.local_data_file),

            train_data_path=Path(config.train_data_path),

            test_data_path=Path(config.test_data_path),

            test_size=params.test_size,

            random_state=params.random_state,

            target_column=self.params.target_column
        )

    # ==========================================================
    # Data Validation
    # ==========================================================

    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        create_directories(
            [Path(config.root_dir)]
        )

        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            validation_status=Path(config.validation_status),
            schema=self.schema.columns,
            columns_count=self.schema.columns_count,
            target_column=self.params.target_column
        )

    # ==========================================================
    # Data Transformation
    # ==========================================================

    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories(
            [Path(config.root_dir)]
        )

        return DataTransformationConfig(
        root_dir=Path(config.root_dir),
        train_data_path=Path(config.train_data_path),
        test_data_path=Path(config.test_data_path),
        preprocessor_path=Path(config.preprocessor_path),
        target_column=self.params.target_column
    )

    # ==========================================================
    # Model Trainer
    # ==========================================================

    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_trainer
        params = self.params.model_trainer

        create_directories(
            [Path(config.root_dir)]
        )

        return ModelTrainerConfig(
    root_dir=Path(config.root_dir),
    model_path=Path(config.model_path),
    metrics_file_path=Path(config.metrics_file_path),

    C=params.C,
    kernel=params.kernel,
    gamma=params.gamma,
    class_weight=params.class_weight,
    probability=params.probability,
    random_state=params.random_state,
)

    # ==========================================================
    # Prediction
    # ==========================================================

    def get_prediction_config(self) -> PredictionConfig:

        model_trainer_config = self.config.model_trainer
        data_transformation_config = self.config.data_transformation
        prediction_config = self.config.prediction
        huggingface_config = self.config.huggingface

        return PredictionConfig(

            # Local paths
            model_path=Path(model_trainer_config.model_path),
            preprocessor_path=Path(data_transformation_config.preprocessor_path),
            metrics_file_path=Path(model_trainer_config.metrics_file_path),

            # Hugging Face
            repo_id=huggingface_config.repo_id,
            model_filename=prediction_config.model_filename,
            preprocessor_filename=prediction_config.preprocessor_filename,
            metrics_filename=prediction_config.metrics_filename,
        )