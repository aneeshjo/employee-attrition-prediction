import sys

from employee_attrition.components.model_trainer import ModelTrainer
from employee_attrition.components.data_transformation import DataTransformation
from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


STAGE_NAME = "MODEL TRAINING STAGE"


if __name__ == "__main__":

    try:

        logger.info(f">>>>>> {STAGE_NAME} STARTED <<<<<<")

        # ==========================================
        # Configuration
        # ==========================================

        config = ConfigurationManager()

        data_transformation_config = (
            config.get_data_transformation_config()
        )

        model_trainer_config = (
            config.get_model_trainer_config()
        )

        # ==========================================
        # Data Transformation
        # ==========================================

        data_transformation = DataTransformation(
            config=data_transformation_config
        )

        train_arr, test_arr, _ = (
            data_transformation.initiate_data_transformation()
        )

        # ==========================================
        # Model Training
        # ==========================================

        model_trainer = ModelTrainer(
            config=model_trainer_config
        )

        metrics = model_trainer.initiate_model_training(
            train_arr=train_arr,
            test_arr=test_arr
        )

        logger.info(f"Training Metrics : {metrics}")

        logger.info(
            f">>>>>> {STAGE_NAME} COMPLETED <<<<<<\n"
        )

    except Exception as e:

        logger.exception(e)

        raise CustomException(e, sys)