from employee_attrition.config.configuration import ConfigurationManager
from employee_attrition.components.data_ingestion import DataIngestion
config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(
    data_ingestion_config
)

train_path, test_path = data_ingestion.initiate_data_ingestion()