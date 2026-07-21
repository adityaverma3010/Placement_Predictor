"""
Prediction Module
Project : Student Placement Prediction System
"""

import sys
import logging
import pandas as pd

import src.logger

from src.exception import CustomException


class PredictionPipeline:

    def __init__(self, pipeline):

        self.pipeline = pipeline

        logging.info("Prediction Pipeline Initialized")

    def predict(self, input_data):

        try:

            logging.info("=" * 60)
            logging.info("PREDICTION STARTED")
            logging.info("=" * 60)

            input_df = pd.DataFrame([input_data])

            prediction = self.pipeline.predict(input_df)[0]

            probability = self.pipeline.predict_proba(input_df)[0]

            logging.info("Prediction Completed Successfully")

            logging.info("=" * 60)
            logging.info("PREDICTION COMPLETED")
            logging.info("=" * 60)

            return prediction, probability

        except Exception as e:

            logging.error(str(e))

            raise CustomException(e, sys)