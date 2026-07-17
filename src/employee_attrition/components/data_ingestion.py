from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from employee_attrition.entity.config_entity import DataIngestionConfig
from employee_attrition.logger import logger
from employee_attrition.exception import CustomException

import sys

class DataIngestion:
    def __init__(
        self,
        config: DataIngestionConfig
    ):
        self.config = config

    def load_dataset(self):
        """
        Load dataset from source path.
        """

        try:

            logger.info("Loading dataset...")

            df = pd.read_csv(
                self.config.source_url
            )

            logger.info(
                f"Dataset loaded successfully with shape {df.shape}"
            )

            return df

        except Exception as e:
            raise CustomException(e, sys)
        
    def save_raw_data(
    self,
    df
    ):
        """
        Save raw dataset inside artifacts.
        """

        try:

            df.to_csv(
                self.config.local_data_file,
                index=False
            )

            logger.info("Raw dataset saved.")

        except Exception as e:
            raise CustomException(e, sys)
        
    def split_data(
        self,
        df
    ):
        """
        Split dataset into train and test sets.
        """

        try:

            train_df, test_df = train_test_split(
                df,
                test_size=self.config.test_size,
                random_state=self.config.random_state,
                stratify=df["Attrition"]
            )

            logger.info(
                "Train-Test split completed."
            )

            return train_df, test_df

        except Exception as e:
            raise CustomException(e, sys)
        
    def save_train_test(
        self,
        train_df,
        test_df
    ):

        try:

            train_df.to_csv(
                self.config.train_data_path,
                index=False
            )

            test_df.to_csv(
                self.config.test_data_path,
                index=False
            )

            logger.info(
                "Train and Test datasets saved."
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_ingestion(self):

        logger.info(
            "Started Data Ingestion"
        )

        df = self.load_dataset()

        self.save_raw_data(df)

        train_df, test_df = self.split_data(df)

        self.save_train_test(
            train_df,
            test_df
        )

        logger.info(
            "Data Ingestion Completed"
        )

        return (
            self.config.train_data_path,
            self.config.test_data_path
        )