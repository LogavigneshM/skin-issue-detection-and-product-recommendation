"""
=========================================================
AI Skin Analyzer
YOLOv11 Training Script
=========================================================
Author : Loga Vignesh
=========================================================
"""

from ultralytics import YOLO
from src import config


def print_configuration():
    """Display project configuration."""

    print("=" * 60)
    print(config.PROJECT_NAME)
    print("=" * 60)

    print(f"Dataset      : {config.DATA_YAML}")
    print(f"Model        : {config.MODEL_NAME}")
    print(f"Device       : {config.DEVICE}")
    print(f"Epochs       : {config.EPOCHS}")
    print(f"Image Size   : {config.IMAGE_SIZE}")
    print(f"Batch Size   : {config.BATCH_SIZE}")
    print(f"Workers      : {config.WORKERS}")

    print("=" * 60)


def verify_dataset():
    """Verify dataset exists."""

    if not config.DATA_YAML.exists():
        raise FileNotFoundError(
            f"\nDataset not found:\n{config.DATA_YAML}"
        )

    print("✅ Dataset Found")


def load_model():
    """Load YOLO model."""

    print("\nLoading YOLOv11 model...\n")

    return YOLO(config.MODEL_NAME)


def train_model(model):
    """Train YOLO model."""

    print("Training Started...\n")

    model.train(
        data=str(config.DATA_YAML),
        epochs=config.EPOCHS,
        imgsz=config.IMAGE_SIZE,
        batch=config.BATCH_SIZE,
        workers=config.WORKERS,
        device=config.DEVICE,
        project=str(config.PROJECT_DIR),
        name=config.RUN_NAME,
        exist_ok=True,
        patience=config.PATIENCE,
        save=config.SAVE,
        plots=True,
        verbose=config.VERBOSE,
    )


def main():

    print_configuration()

    verify_dataset()

    model = load_model()

    train_model(model)

    print("\n" + "=" * 60)
    print("Training Completed Successfully!")
    print("=" * 60)

    print(f"\nBest Model : {config.BEST_MODEL}")

    print(f"Last Model : {config.LAST_MODEL}")


if __name__ == "__main__":
    main()