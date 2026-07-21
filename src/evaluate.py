"""
Model Evaluation Module
Project : Student Placement Prediction System
"""

import sys
import logging

import src.logger

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from src.exception import CustomException


class ModelEvaluator:
    """
    Evaluate Machine Learning Model
    """

    def __init__(self):

        logging.info("ModelEvaluator Initialized")

    def evaluate(self, model, X_test, y_test):
        """
        Evaluate trained model.
        """

        try:

            logging.info("=" * 60)
            logging.info("MODEL EVALUATION STARTED")
            logging.info("=" * 60)

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)

            precision = precision_score(y_test, y_pred)

            recall = recall_score(y_test, y_pred)

            f1 = f1_score(y_test, y_pred)

            cm = confusion_matrix(y_test, y_pred)

            report = classification_report(y_test, y_pred)

            logging.info(f"Accuracy : {accuracy:.4f}")
            logging.info(f"Precision : {precision:.4f}")
            logging.info(f"Recall : {recall:.4f}")
            logging.info(f"F1 Score : {f1:.4f}")

            logging.info("=" * 60)
            logging.info("MODEL EVALUATION COMPLETED")
            logging.info("=" * 60)

            return {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "confusion_matrix": cm,
                "classification_report": report
            }

        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)