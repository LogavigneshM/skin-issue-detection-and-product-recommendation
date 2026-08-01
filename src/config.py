"""
=========================================================
AI Skin Analyzer
Project Configuration
=========================================================
Author : Loga Vignesh
=========================================================
"""

from pathlib import Path
import torch

# =========================================================
# PROJECT INFORMATION
# =========================================================

PROJECT_NAME = "AI Skin Analyzer"
PROJECT_VERSION = "1.0.0"
AUTHOR = "Loga Vignesh"

# =========================================================
# PROJECT PATHS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset
DATASET_DIR = PROJECT_ROOT / "dataset"
DATA_YAML = DATASET_DIR / "data.yaml"

# Models
MODELS_DIR = PROJECT_ROOT / "models"

BEST_MODEL = MODELS_DIR / "weights" / "best.pt"
LAST_MODEL = MODELS_DIR / "weights" / "last.pt"

# Outputs
RUNS_DIR = PROJECT_ROOT / "runs"
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
DOCS_DIR = PROJECT_ROOT / "docs"

# Input / Output Images
INPUT_IMAGES_DIR = PROJECT_ROOT / "input_images"
OUTPUT_IMAGES_DIR = PROJECT_ROOT / "output_images"

# =========================================================
# MODEL CONFIGURATION
# =========================================================

MODEL_NAME = "yolo11n.pt"

IMAGE_SIZE = 640

NUM_CLASSES = 6

CLASS_NAMES = [
    "Acne",
    "Black Heads",
    "Eczema",
    "Rosacea",
    "Flakiness",
    "Pigmentation"
]

# =========================================================
# TRAINING CONFIGURATION
# =========================================================

EPOCHS = 100

BATCH_SIZE = 4

WORKERS = 2

LEARNING_RATE = 0.01

PATIENCE = 30

SAVE = True

VERBOSE = True

# =========================================================
# DEVICE
# =========================================================

DEVICE = 0 if torch.cuda.is_available() else "cpu"

# =========================================================
# RANDOM SEED
# =========================================================

SEED = 42

# =========================================================
# RUN CONFIGURATION
# =========================================================

PROJECT_DIR = RUNS_DIR

RUN_NAME = "skin_detection"

# =========================================================
# STREAMLIT CONFIGURATION
# =========================================================

APP_TITLE = "AI Skin Analyzer"

MAX_UPLOAD_SIZE_MB = 10