"""
Data Preprocessing Module
Project : Student Placement Prediction System
"""

import logging
import pandas as pd

import src.logger


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate records.
    """

    logging.info("Removing Duplicate Records")

    df = df.drop_duplicates()

    logging.info(f"Dataset Shape : {df.shape}")

    return df


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical columns.
    """

    logging.info("Encoding Categorical Features")

    df = df.copy()

    # Encode Internship Experience
    df["Internship_Experience"] = (
    pd.to_numeric(
        df["Internship_Experience"].replace({"Yes": 1, "No": 0}),
        errors="raise"
    )
    .astype("int64")
)

    # Encode Placement
    df["Placement"] = (
    pd.to_numeric(
        df["Placement"].replace({"Yes": 1, "No": 0}),
        errors="raise"
    )
    .astype("int64")
)

    logging.info("Categorical Encoding Completed")

    return df


def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop unnecessary columns.
    """

    logging.info("Dropping Unnecessary Columns")

    if "College_ID" in df.columns:
        df = df.drop(columns=["College_ID"])

    return df


def split_features_target(df: pd.DataFrame):
    """
    Split dataset into Features and Target.
    """

    logging.info("Separating Features and Target")

    X = df.drop(columns=["Placement"])

    y = df["Placement"]

    logging.info(f"Feature Shape : {X.shape}")
    logging.info(f"Target Shape : {y.shape}")

    return X, y


def preprocess_data(df):

    logging.info("=" * 60)
    logging.info("DATA PREPROCESSING STARTED")
    logging.info("=" * 60)

    df = remove_duplicates(df)

    df = encode_features(df)

    df = drop_columns(df)      # <-- This must execute

    X, y = split_features_target(df)

    logging.info("=" * 60)
    logging.info("DATA PREPROCESSING COMPLETED")
    logging.info("=" * 60)

    return X, y