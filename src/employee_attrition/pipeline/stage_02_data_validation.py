import sys

from employee_attrition.components.data_validation import DataValidation
from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


STAGE_NAME = "DATA VALIDATION STAGE"


if __name__ == "__main__":

    try:

        logger.info(f">>>>>> {STAGE_NAME} STARTED <<<<<<")

        config = ConfigurationManager()

        data_validation_config = (
            config.get_data_validation_config()
        )

        data_validation = DataValidation(
            config=data_validation_config
        )

        validation_status = (
            data_validation.validate_all_columns()
        )

        logger.info(
            f"Validation Status : {validation_status}"
        )

        logger.info(f">>>>>> {STAGE_NAME} COMPLETED <<<<<<\n")

    except Exception as e:

        logger.exception(e)

        raise CustomException(e, sys)