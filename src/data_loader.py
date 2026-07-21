"""
Data Loader Module
Project : Student Placement Prediction System
"""

import sys
import logging
import pandas as pd

import src.logger

from pathlib import Path
from src.exception import CustomException


class DataLoader:
    """
    Class for loading the dataset.
    """

    def __init__(self, data_path):
        """
        Initialize DataLoader.

        Parameters
        ----------
        data_path : str or Path
            Path to the dataset.
        """
        self.data_path = Path(data_path)

    def load_data(self):
        """
        Load dataset from CSV file.

        Returns
        -------
        pandas.DataFrame
        """

        try:

            logging.info("=" * 60)
            logging.info("DATA LOADING STARTED")
            logging.info("=" * 60)

            # Check if file exists
            if not self.data_path.exists():

                raise FileNotFoundError(
                    f"Dataset not found: {self.data_path}"
                )

            logging.info("Dataset Found")

            # Check if file is empty
            if self.data_path.stat().st_size == 0:

                raise ValueError(
                    "Dataset file is empty."
                )

            logging.info("Dataset is not empty")

            # Load dataset
            df = pd.read_csv(self.data_path)

            logging.info("Dataset Loaded Successfully")

            logging.info(f"Dataset Shape : {df.shape}")

            logging.info(f"Columns : {list(df.columns)}")

            logging.info("=" * 60)
            logging.info("DATA LOADING COMPLETED")
            logging.info("=" * 60)

            return df

        except Exception as e:

            logging.error(str(e))

            raise CustomException(e, sys)