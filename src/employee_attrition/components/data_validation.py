import os
import sys
import pandas as pd

from employee_attrition.logger import logger
from employee_attrition.exception import CustomException
from employee_attrition.entity.config_entity import DataValidationConfig

class DataValidation:
    """
    Validate the integrity of the training and testing datasets.
    """
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_all_columns(self) -> bool:
        """
        Validate column names and data types.
        """
        try:
            logger.info("Starting Data Validation...")
            train_df=pd.read_csv(self.config.train_data_path)
            test_df=pd.read_csv(self.config.test_data_path)

            valiadtion_status=True
            report=[]

            # ===========================
            # Column Validation
            # ===========================

            expected_columns=self.config.all_schema

            train_columns = list(train_df.columns)
            test_columns = list(test_df.columns)

            if list(expected_columns.keys()) != train_columns:
                validation_status = False
                report.append("Train dataset columns do not match schema.")

            if list(expected_columns.keys()) != test_columns:
                validation_status = False
                report.append("Test dataset columns do not match schema.")

            # ===========================
            # Data Type Validation
            # ===========================

            for column, expected_dtype in expected_columns.items():
                train_dtype = str(train_df[column].dtype)
                test_dtype = str(test_df[column].dtype)

                if train_dtype != expected_dtype:
                    validation_status = False
                    report.append(
                        f"Train -> {column}: Expected {expected_dtype}, Found {train_dtype}"
                    )

                if test_dtype != expected_dtype:
                    validation_status = False
                    report.append(
                        f"Test -> {column}: Expected {expected_dtype}, Found {test_dtype}"
                    )

            # ===========================
            # Target Column Check
            # ===========================

            if "Attrition" not in train_df.columns:
                validation_status = False
                report.append("Target column 'Attrition' missing in train dataset.")

            if "Attrition" not in test_df.columns:
                validation_status = False
                report.append("Target column 'Attrition' missing in test dataset.")

            # ===========================
            # Duplicate Check
            # ===========================

            train_duplicates = train_df.duplicated().sum()
            test_duplicates = test_df.duplicated().sum()

            report.append(f"Train Shape : {train_df.shape}")
            report.append(f"Test Shape : {test_df.shape}")
            report.append(f"Train Duplicate Rows : {train_duplicates}")
            report.append(f"Test Duplicate Rows : {test_duplicates}")

            # ===========================
            # Save Validation Report
            # ===========================

            with open(self.config.validation_status, "w") as f:

                f.write(f"Validation Status : {validation_status}\n\n")

                for line in report:
                    f.write(line + "\n")

            logger.info("Data Validation Completed.")

            return validation_status



        except Exception as e:
            raise CustomException(e,sys)