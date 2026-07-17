import sys

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from employee_attrition.entity.config_entity import DataTransformationConfig
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger
from employee_attrition.utils.common import save_object


class DataTransformation:
    """
    Handles feature preprocessing and transformation of the
    training and testing datasets.
    """

    def __init__(
        self,
        config: DataTransformationConfig
    ):
        self.config = config

    def get_data_transformer_object(
        self,
        X_train: pd.DataFrame
    ) -> ColumnTransformer:
        """
        Create the preprocessing pipeline.

        Args:
            X_train (pd.DataFrame): Training features.

        Returns:
            ColumnTransformer: Configured preprocessing object.
        """

        try:

            numerical_features = X_train.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            categorical_features = X_train.select_dtypes(
                include=["object"]
            ).columns.tolist()

            logger.info(
                f"Numerical Columns : {numerical_features}"
            )

            logger.info(
                f"Categorical Columns : {categorical_features}"
            )

            numerical_pipeline = Pipeline(
                steps=[
                    (
                        "scaler",
                        StandardScaler()
                    )
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False
                        )
                    )
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "numerical",
                        numerical_pipeline,
                        numerical_features
                    ),
                    (
                        "categorical",
                        categorical_pipeline,
                        categorical_features
                    )
                ]
            )

            logger.info(
                "Preprocessor created successfully."
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(
        self
    ) -> tuple[np.ndarray, np.ndarray, str]:
        """
        Execute the complete data transformation pipeline.

        Returns:
            tuple:
                - Train array
                - Test array
                - Saved preprocessor path
        """

        try:

            logger.info(
                "========== Data Transformation Started =========="
            )

            # ==========================================
            # Check File Existence
            # ==========================================

            if not self.config.train_data_path.exists():
                raise FileNotFoundError(
                    f"Train dataset not found: {self.config.train_data_path}"
                )

            if not self.config.test_data_path.exists():
                raise FileNotFoundError(
                    f"Test dataset not found: {self.config.test_data_path}"
                )

            # ==========================================
            # Load Datasets
            # ==========================================

            train_df = pd.read_csv(
                self.config.train_data_path
            )

            test_df = pd.read_csv(
                self.config.test_data_path
            )

            logger.info(
                f"Train Shape : {train_df.shape}"
            )

            logger.info(
                f"Test Shape : {test_df.shape}"
            )

            # ==========================================
            # Split Features and Target
            # ==========================================

            target_column = self.config.target_column

            target_mapping = {
                "No": 0,
                "Yes": 1
            }

            y_train = (
                train_df[self.config.target_column]
                .map(target_mapping)
                .astype(int)
            )

            y_test = (
                test_df[self.config.target_column]
                .map(target_mapping)
                .astype(int)
            )

            X_train = train_df.drop(
                columns=[target_column]
            )

            # y_train = train_df[target_column]

            X_test = test_df.drop(
                columns=[target_column]
            )

            # y_test = test_df[target_column]

            # ==========================================
            # Create Preprocessor
            # ==========================================

            logger.info(
                "Creating preprocessing pipeline..."
            )

            preprocessor = self.get_data_transformer_object(
                X_train=X_train
            )

            # ==========================================
            # Transform Data
            # ==========================================

            logger.info(
                "Fitting preprocessor on training data..."
            )

            X_train = preprocessor.fit_transform(
                X_train
            )

            X_test = preprocessor.transform(
                X_test
            )

            logger.info(
                f"Transformed Train Shape : {X_train.shape}"
            )

            logger.info(
                f"Transformed Test Shape : {X_test.shape}"
            )

            # ==========================================
            # Combine Features and Target
            # ==========================================

            train_arr = np.c_[
                X_train,
                y_train
            ]

            test_arr = np.c_[
                X_test,
                y_test
            ]

            # ==========================================
            # Save Preprocessor
            # ==========================================

            save_object(
                file_path=self.config.preprocessor_path,
                obj=preprocessor
            )

            logger.info(
                f"Preprocessor saved to: {self.config.preprocessor_path}"
            )

            logger.info(
                "========== Data Transformation Completed =========="
            )

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_path
            )

        except Exception as e:
            raise CustomException(e, sys)