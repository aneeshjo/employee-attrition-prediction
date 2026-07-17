import sys

from employee_attrition.components.data_transformation import DataTransformation
from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


STAGE_NAME = "DATA TRANSFORMATION STAGE"


if __name__ == "__main__":

    try:

        logger.info(f">>>>>> {STAGE_NAME} STARTED <<<<<<")

        config = ConfigurationManager()

        data_transformation_config = (
            config.get_data_transformation_config()
        )

        data_transformation = DataTransformation(
            config=data_transformation_config
        )

        train_arr, test_arr, preprocessor_path = (
            data_transformation.initiate_data_transformation()
        )

        logger.info(
            f"Train Array Shape : {train_arr.shape}"
        )

        logger.info(
            f"Test Array Shape : {test_arr.shape}"
        )

        logger.info(
            f"Preprocessor Saved At : {preprocessor_path}"
        )

        logger.info(
            f">>>>>> {STAGE_NAME} COMPLETED <<<<<<\n"
        )

    except Exception as e:

        logger.exception(e)

        raise CustomException(e, sys)