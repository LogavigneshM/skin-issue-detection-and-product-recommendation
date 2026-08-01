"""
=========================================================
AI Skin Analyzer
Model Evaluation
=========================================================
Author : Loga Vignesh
=========================================================
"""

from ultralytics import YOLO
from src import config


def load_model():
    """Load trained model."""

    print("Loading trained model...")

    return YOLO(str(config.BEST_MODEL))


def evaluate_model(model):
    """Evaluate model on validation dataset."""

    print("\nEvaluating model...\n")

    metrics = model.val(
        data=str(config.DATA_YAML),
        imgsz=config.IMAGE_SIZE,
        batch=config.BATCH_SIZE,
        device=config.DEVICE,
        split="test",
    )

    return metrics


def print_metrics(metrics):
    """Display evaluation metrics."""

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(f"Precision : {metrics.box.mp:.4f}")
    print(f"Recall    : {metrics.box.mr:.4f}")
    print(f"mAP@50    : {metrics.box.map50:.4f}")
    print(f"mAP50-95  : {metrics.box.map:.4f}")

    print("=" * 60)


def main():

    model = load_model()

    metrics = evaluate_model(model)

    print_metrics(metrics)


if __name__ == "__main__":
    main()