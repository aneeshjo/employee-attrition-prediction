import os
import sys
import json
import joblib
import numpy as np

from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from employee_attrition.logger import logger
from employee_attrition.exception import CustomException
from employee_attrition.utils.common import save_object
from employee_attrition.entity.config_entity import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def evaluate_model(self, y_true, y_pred, y_prob):
        """
        Evaluate model performance.
        """

        metrics = {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred),
            "recall": recall_score(y_true, y_pred),
            "f1_score": f1_score(y_true, y_pred),
            "roc_auc": roc_auc_score(y_true, y_prob)
        }

        return metrics

    def initiate_model_training(self, train_arr, test_arr):
        """
        Train and save the final model.
        """

        try:

            logger.info("Splitting training and testing arrays")

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info("Initializing SVM model")

            model = SVC(
                C=self.config.C,
                kernel=self.config.kernel,
                gamma=self.config.gamma,
                class_weight=self.config.class_weight,
                probability=self.config.probability,
                random_state=self.config.random_state
            )

            logger.info("Training model")

            model.fit(X_train, y_train)

            logger.info("Making predictions")

            y_pred = model.predict(X_test)
            y_prob = model.predict_proba(X_test)[:, 1]

            metrics = self.evaluate_model(
                y_test,
                y_pred,
                y_prob
            )

            logger.info(f"Metrics : {metrics}")

            logger.info("Saving trained model")

            save_object(
                file_path=self.config.trained_model_file_path,
                obj=model
            )
            

            with open(
                self.config.metrics_file_name,
                "w"
            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4
                )

            logger.info("Model and metrics saved successfully")

            return metrics

        except Exception as e:
            raise CustomException(e, sys)