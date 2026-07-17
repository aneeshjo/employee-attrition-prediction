import sys

from employee_attrition.components.data_ingestion import DataIngestion
from employee_attrition.components.data_validation import DataValidation
from employee_attrition.components.data_transformation import DataTransformation
from employee_attrition.components.model_trainer import ModelTrainer

from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


STAGE_NAME = "EMPLOYEE ATTRITION TRAINING PIPELINE"


def main():

    logger.info("=" * 70)
    logger.info(f"{STAGE_NAME} STARTED")
    logger.info("=" * 70)

    config = ConfigurationManager()

    # ==========================================
    # Stage 1 : Data Ingestion
    # ==========================================

    logger.info("Running Data Ingestion Stage...")

    ingestion = DataIngestion(
        config.get_data_ingestion_config()
    )

    train_path, test_path = (
        ingestion.initiate_data_ingestion()
    )

    # ==========================================
    # Stage 2 : Data Validation
    # ==========================================

    logger.info("Running Data Validation Stage...")

    validation = DataValidation(
        config.get_data_validation_config()
    )

    validation_status = (
        validation.validate_all_columns()
    )

    if not validation_status:
        raise ValueError(
            "Data Validation Failed."
        )

    # ==========================================
    # Stage 3 : Data Transformation
    # ==========================================

    logger.info("Running Data Transformation Stage...")

    transformation = DataTransformation(
        config.get_data_transformation_config()
    )

    train_arr, test_arr, _ = (
        transformation.initiate_data_transformation()
    )

    # ==========================================
    # Stage 4 : Model Training
    # ==========================================

    logger.info("Running Model Training Stage...")

    trainer = ModelTrainer(
        config.get_model_trainer_config()
    )

    metrics = trainer.initiate_model_training(
        train_arr,
        test_arr
    )

    logger.info(f"Final Metrics : {metrics}")

    logger.info("=" * 70)
    logger.info("PIPELINE COMPLETED SUCCESSFULLY")
    logger.info("=" * 70)


if __name__ == "__main__":

    try:

        main()

    except Exception as e:

        logger.exception(e)

        raise CustomException(e, sys)