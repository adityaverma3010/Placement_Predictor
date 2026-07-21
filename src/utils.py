"""
Utility Functions
Project : Student Placement Prediction System
"""

import os
import pickle
import logging

import src.logger

from pathlib import Path


def create_directory(directory_path):
    """
    Create directory if it doesn't exist.
    """

    try:

        Path(directory_path).mkdir(
            parents=True,
            exist_ok=True
        )

        logging.info(f"Directory Created : {directory_path}")

    except Exception as e:

        logging.error(e)

        raise


def save_object(file_path, obj):
    """
    Save Python object using pickle.
    """

    try:

        directory = os.path.dirname(file_path)

        create_directory(directory)

        with open(file_path, "wb") as file:

            pickle.dump(obj, file)

        logging.info(f"Object Saved Successfully : {file_path}")

    except Exception as e:

        logging.error(e)

        raise


def load_object(file_path):
    """
    Load Pickle Object.
    """

    try:

        with open(file_path, "rb") as file:

            obj = pickle.load(file)

        logging.info(f"Object Loaded Successfully : {file_path}")

        return obj

    except Exception as e:

        logging.error(e)

        raise