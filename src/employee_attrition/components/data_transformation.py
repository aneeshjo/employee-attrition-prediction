import os
import sys
import pandas as pd
import numpy as np

from employee_attrition.logger import logger
from employee_attrition.exception import CustomException
from employee_attrition.entity.config_entity import DataTransformationConfig
from employee_attrition.utils.common import save_object

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class DataTransformation:

    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def get_data_transformer_object(self,X_train):
        try:
            numerical_features=X_train.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            categorical_features = X_train.select_dtypes(
                include="object"
            ).columns.tolist()

            logger.info(f"Numerical Columns: {numerical_features}")
            logger.info(f"Categorical Columns: {categorical_features}")

            numerical_pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler())
            ]
            )

            categorical_pipeline=Pipeline(
                steps=[
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        sparse_output=False
                    )
                ]
            )

            preprocessor=ColumnTransformer(
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

            logger.info("Preprocessor Created Successfully")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self):
        try:
            logger.info("Reading Train and Test Data")

            train_df=pd.read_csv(
                self.config.train_data_path
            )

            test_df=pd.read_csv(
                self.config.test_data_path
            )

            target_column=self.config.target_column

            X_train = train_df.drop(columns=[target_column])

            y_train = train_df[target_column]

            X_test = test_df.drop(columns=[target_column])

            y_test = test_df[target_column]

            logger.info("Obtaining Preprocessor")

            preprocessor=self.get_data_transformer_object(X_train=X_train)
            logger.info("Fitting Preprocessor")

            X_train = preprocessor.fit_transform(
                X_train
            )

            X_test = preprocessor.transform(
                X_test
            )

            train_arr = np.c_[X_train, y_train]

            test_arr = np.c_[X_test, y_test]

            save_object(
                file_path=self.config.preprocessor_obj_file_path,
                obj=preprocessor
            )

            logger.info("Preprocessor Saved Successfully")

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)


