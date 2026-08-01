"""
=========================================================
AI Skin Analyzer
Utility Functions
=========================================================
"""

from pathlib import Path
import os
import torch
from . import config


def print_project_info():
    """
    Display project information.
    """

    print("=" * 60)
    print(f"Project : {config.PROJECT_NAME}")
    print(f"Version : {config.PROJECT_VERSION}")
    print(f"Author  : {config.AUTHOR}")
    print(f"Device  : {config.DEVICE}")
    print("=" * 60)


def create_project_directories():
    """
    Create required project folders if they do not exist.
    """

    directories = [
        config.MODELS_DIR,
        config.RUNS_DIR,
        config.SCREENSHOTS_DIR,
        config.DOCS_DIR
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

    print("✅ Project directories verified.")


def verify_dataset():
    """
    Check whether the dataset exists.
    """

    if not config.DATA_YAML.exists():
        raise FileNotFoundError(
            f"\n❌ data.yaml not found:\n{config.DATA_YAML}"
        )

    print("✅ Dataset found.")
    print(config.DATA_YAML)


def get_device():
    """
    Return training device.
    """

    if torch.cuda.is_available():
        return "cuda"

    return "cpu"


def print_training_configuration():
    """
    Display training configuration.
    """

    print("\nTraining Configuration")
    print("-" * 40)

    print(f"Model       : {config.MODEL_NAME}")
    print(f"Image Size  : {config.IMAGE_SIZE}")
    print(f"Epochs      : {config.EPOCHS}")
    print(f"Batch Size  : {config.BATCH_SIZE}")
    print(f"Workers     : {config.WORKERS}")
    print(f"Device      : {config.DEVICE}")

    print("-" * 40)