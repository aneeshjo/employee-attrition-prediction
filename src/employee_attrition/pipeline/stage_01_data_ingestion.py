from employee_attrition.components.data_ingestion import DataIngestion
from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.logger import logger


STAGE_NAME = "DATA INGESTION"


class DataIngestionPipeline:
    """
    Pipeline for executing the Data Ingestion stage.
    """

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(
            config=data_ingestion_config
        )

        train_path, test_path = data_ingestion.initiate_data_ingestion()

        logger.info(f"Train Data Path : {train_path}")
        logger.info(f"Test Data Path  : {test_path}")


if __name__ == "__main__":

    try:

        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")

        obj = DataIngestionPipeline()

        obj.main()

        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\n")

    except Exception as e:

        logger.exception(e)

        raise e