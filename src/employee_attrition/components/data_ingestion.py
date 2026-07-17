import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from employee_attrition.entity.config_entity import DataIngestionConfig
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


class DataIngestion:
    """
    Handles loading the dataset, saving the raw data,
    splitting it into train/test sets, and saving the
    processed datasets.
    """

    def __init__(
        self,
        config: DataIngestionConfig
    ):
        self.config = config

    def load_dataset(self) -> pd.DataFrame:
        """
        Load the dataset from the source file.

        Returns:
            pd.DataFrame: Loaded dataset.
        """

        try:

            logger.info("Loading dataset...")

            df = pd.read_csv(
                self.config.source_file
            )

            logger.info(
                f"Dataset loaded successfully with shape: {df.shape}"
            )

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def save_raw_data(
        self,
        df: pd.DataFrame
    ) -> None:
        """
        Save the raw dataset into the artifacts folder.
        """

        try:

            df.to_csv(
                self.config.local_data_file,
                index=False
            )

            logger.info(
                f"Raw dataset saved to: {self.config.local_data_file}"
            )

        except Exception as e:
            raise CustomException(e, sys)

    def split_data(
        self,
        df: pd.DataFrame
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Split the dataset into train and test sets.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame]
        """

        try:

            train_df, test_df = train_test_split(

                df,

                test_size=self.config.test_size,

                random_state=self.config.random_state,

                stratify=df[self.config.target_column]

            )

            logger.info(
                f"Train-Test split completed."
            )

            logger.info(
                f"Train Shape : {train_df.shape}"
            )

            logger.info(
                f"Test Shape : {test_df.shape}"
            )

            return train_df, test_df

        except Exception as e:
            raise CustomException(e, sys)

    def save_train_test(
        self,
        train_df: pd.DataFrame,
        test_df: pd.DataFrame
    ) -> None:
        """
        Save the train and test datasets.
        """

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
                f"Train dataset saved to: {self.config.train_data_path}"
            )

            logger.info(
                f"Test dataset saved to: {self.config.test_data_path}"
            )

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self):
        """
        Execute the complete Data Ingestion pipeline.
        """

        logger.info(
            "========== Data Ingestion Started =========="
        )

        df = self.load_dataset()

        self.save_raw_data(df)

        train_df, test_df = self.split_data(df)

        self.save_train_test(
            train_df,
            test_df
        )

        logger.info(
            "========== Data Ingestion Completed =========="
        )

        return (
            self.config.train_data_path,
            self.config.test_data_path
        )