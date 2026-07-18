import sys

import pandas as pd

from employee_attrition.entity.config_entity import DataValidationConfig
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger


class DataValidation:
    """
    Validate the integrity of the training and testing datasets.
    """

    def __init__(
        self,
        config: DataValidationConfig
    ):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validate dataset columns, data types, target column,
        duplicate rows, and generate a validation report.

        Returns:
            bool: Validation status.
        """

        try:

            logger.info("========== Data Validation Started ==========")

            # ===========================
            # Check File Existence
            # ===========================

            if not self.config.train_data_path.exists():
                raise FileNotFoundError(
                    f"Train dataset not found: {self.config.train_data_path}"
                )

            if not self.config.test_data_path.exists():
                raise FileNotFoundError(
                    f"Test dataset not found: {self.config.test_data_path}"
                )

            # ===========================
            # Load Datasets
            # ===========================

            train_df = pd.read_csv(
                self.config.train_data_path
            )

            test_df = pd.read_csv(
                self.config.test_data_path
            )

            validation_status = True

            report = []

            expected_columns = self.config.schema

            # ===========================
            # Column Count Validation
            # ===========================

            if len(train_df.columns) != self.config.columns_count:
                validation_status = False
                report.append(
                    "Train dataset column count does not match schema."
                )

            if len(test_df.columns) != self.config.columns_count:
                validation_status = False
                report.append(
                    "Test dataset column count does not match schema."
                )

            # ===========================
            # Column Name Validation
            # ===========================

            train_columns = list(train_df.columns)
            test_columns = list(test_df.columns)

            if list(expected_columns.keys()) != train_columns:
                validation_status = False
                report.append(
                    "Train dataset columns do not match schema."
                )

            if list(expected_columns.keys()) != test_columns:
                validation_status = False
                report.append(
                    "Test dataset columns do not match schema."
                )

            # ===========================
            # Data Type Validation
            # ===========================

            for column, expected_dtype in expected_columns.items():

                train_dtype = str(train_df[column].dtype).lower()
                test_dtype = str(test_df[column].dtype).lower()
                expected_dtype = str(expected_dtype).lower()

                # Treat Pandas "str" and "object" as equivalent
                if expected_dtype == "object":
                    valid_types = ["object", "str", "string"]
                else:
                    valid_types = [expected_dtype]

                if train_dtype not in valid_types:

                    validation_status = False

                    report.append(
                        f"Train -> {column}: Expected {expected_dtype}, Found {train_dtype}"
                    )

                if test_dtype not in valid_types:

                    validation_status = False

                    report.append(
                        f"Test -> {column}: Expected {expected_dtype}, Found {test_dtype}"
                    )
            # ===========================
            # Target Column Validation
            # ===========================

            if self.config.target_column not in train_df.columns:

                validation_status = False

                report.append(
                    f"Target column '{self.config.target_column}' missing in Train dataset."
                )

            if self.config.target_column not in test_df.columns:

                validation_status = False

                report.append(
                    f"Target column '{self.config.target_column}' missing in Test dataset."
                )

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

            with open(
                self.config.validation_status,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    "=" * 50 + "\n"
                )

                file.write(
                    "DATA VALIDATION REPORT\n"
                )

                file.write(
                    "=" * 50 + "\n\n"
                )

                file.write(
                    f"Validation Status : {validation_status}\n\n"
                )

                for line in report:
                    file.write(line + "\n")

            logger.info(
                f"Validation Status : {validation_status}"
            )

            logger.info(
                "========== Data Validation Completed =========="
            )

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)