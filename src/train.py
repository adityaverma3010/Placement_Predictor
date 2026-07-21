"""
Model Training Module
Project : Student Placement Prediction System
"""

import sys
import logging

import src.logger

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from src.exception import CustomException


class ModelTrainer:
    """
    Train Machine Learning Model
    """

    def __init__(self):

        self.pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("classifier", LogisticRegression(random_state=42))
            ]
        )

    def train(self, X_train, y_train):
        """
        Train Pipeline
        """

        try:

            logging.info("=" * 60)
            logging.info("MODEL TRAINING STARTED")
            logging.info("=" * 60)

            self.pipeline.fit(X_train, y_train)

            logging.info("Pipeline Trained Successfully")

            logging.info("=" * 60)
            logging.info("MODEL TRAINING COMPLETED")
            logging.info("=" * 60)

            return self.pipeline

        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)