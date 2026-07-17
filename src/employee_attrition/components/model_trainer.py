import json
import sys

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.svm import SVC

from employee_attrition.entity.config_entity import ModelTrainerConfig
from employee_attrition.exception import CustomException
from employee_attrition.logger import logger
from employee_attrition.utils.common import save_object


class ModelTrainer:
    """
    Train, evaluate, and save the machine learning model.
    """

    def __init__(
        self,
        config: ModelTrainerConfig
    ):
        self.config = config

    def evaluate_model(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_prob: np.ndarray
    ) -> dict:
        """
        Evaluate model performance.

        Returns:
            dict: Evaluation metrics.
        """

        metrics = {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred),
            "recall": recall_score(y_true, y_pred),
            "f1_score": f1_score(y_true, y_pred),
            "roc_auc": roc_auc_score(y_true, y_prob),
        }

        return metrics

    def initiate_model_training(
        self,
        train_arr: np.ndarray,
        test_arr: np.ndarray
    ) -> dict:
        """
        Train, evaluate, and save the final model.

        Returns:
            dict: Model evaluation metrics.
        """

        try:

            logger.info(
                "========== Model Training Started =========="
            )

            # ==========================================
            # Split Features and Target
            # ==========================================

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info(
                f"Training Samples : {X_train.shape[0]}"
            )

            logger.info(
                f"Testing Samples : {X_test.shape[0]}"
            )

            # ==========================================
            # Initialize Model
            # ==========================================

            logger.info("Initializing SVM model...")

            model = SVC(
                C=self.config.C,
                kernel=self.config.kernel,
                gamma=self.config.gamma,
                class_weight=self.config.class_weight,
                probability=self.config.probability,
                random_state=self.config.random_state,
            )

            # ==========================================
            # Train Model
            # ==========================================

            logger.info("Training model...")

            model.fit(
                X_train,
                y_train
            )

            logger.info("Model training completed.")

            # ==========================================
            # Prediction
            # ==========================================

            logger.info("Generating predictions...")

            y_pred = model.predict(X_test)

            y_prob = model.predict_proba(X_test)[:, 1]

            # ==========================================
            # Evaluation
            # ==========================================

            metrics = self.evaluate_model(
                y_true=y_test,
                y_pred=y_pred,
                y_prob=y_prob,
            )

            logger.info(f"Model Metrics : {metrics}")

            # ==========================================
            # Save Model
            # ==========================================

            save_object(
                file_path=self.config.model_path,
                obj=model,
            )

            logger.info(
                f"Model saved to : {self.config.model_path}"
            )

            # ==========================================
            # Save Metrics
            # ==========================================

            with open(
                self.config.metrics_file_path,
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    metrics,
                    file,
                    indent=4,
                )

            logger.info(
                f"Metrics saved to : {self.config.metrics_file_path}"
            )

            logger.info(
                "========== Model Training Completed =========="
            )

            return metrics

        except Exception as e:
            raise CustomException(e, sys)