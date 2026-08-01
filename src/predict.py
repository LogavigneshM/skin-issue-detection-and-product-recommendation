"""
=========================================================
AI Skin Analyzer
Prediction Module
=========================================================
Author : Loga Vignesh
=========================================================
"""

from pathlib import Path
from ultralytics import YOLO

from src import config
from src.recommendation import display_recommendation


# =========================================================
# LOAD MODEL
# =========================================================

def load_model():
    """
    Load the trained YOLO model.
    """

    if not config.BEST_MODEL.exists():
        raise FileNotFoundError(
            f"\n❌ Model not found:\n{config.BEST_MODEL}"
        )

    print("✅ Model Loaded Successfully")

    return YOLO(str(config.BEST_MODEL))


# =========================================================
# RUN PREDICTION
# =========================================================

def predict_images():
    """
    Run prediction on images.
    """

    model = load_model()

    image_folder = config.INPUT_IMAGES_DIR / "images"

    if not image_folder.exists():
        raise FileNotFoundError(
            f"\n❌ Input image folder not found:\n{image_folder}"
        )

    print("\n" + "=" * 60)
    print("Running Predictions")
    print("=" * 60)

    print(f"Input Folder : {image_folder}")

    results = model.predict(
        source=str(image_folder),
        imgsz=config.IMAGE_SIZE,
        conf=0.25,
        save=True,
        project=str(config.OUTPUT_IMAGES_DIR),
        name="predictions",
        exist_ok=True,
        verbose=False,
    )

    print("\n✅ Prediction Completed Successfully!")

    return results


# =========================================================
# DISPLAY RESULTS
# =========================================================

def display_results(results):
    """
    Display prediction results and recommendations.
    """

    print("\n" + "=" * 60)
    print("Detected Skin Issues")
    print("=" * 60)

    detected_issues = set()

    total_detections = 0

    for result in results:

        image_name = Path(result.path).name

        print(f"\n📷 Image : {image_name}")

        if len(result.boxes) == 0:
            print("No skin issue detected.")
            continue

        # Sort by confidence
        boxes = sorted(
            result.boxes,
            key=lambda x: float(x.conf[0]),
            reverse=True
        )

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            class_name = config.CLASS_NAMES[class_id]

            detected_issues.add(class_name)

            print(
                f"• {class_name:<15} {confidence:.2%}"
            )

            total_detections += 1

    print("\n" + "=" * 60)
    print(f"Total Detections : {total_detections}")
    print("=" * 60)

    # =====================================================
    # DISPLAY RECOMMENDATIONS
    # =====================================================

    if detected_issues:

        print("\n" + "=" * 60)
        print("SKINCARE RECOMMENDATIONS")
        print("=" * 60)

        for issue in sorted(detected_issues):

            display_recommendation(issue)

    else:

        print("\nNo recommendations available.")


# =========================================================
# OUTPUT LOCATION
# =========================================================

def show_output_location():

    output_folder = (
        config.OUTPUT_IMAGES_DIR /
        "predictions"
    )

    print("\nAnnotated Images Saved To:")

    print(output_folder)


# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print(config.PROJECT_NAME)
    print("=" * 60)

    print(f"Model        : {config.BEST_MODEL}")
    print(f"Device       : {config.DEVICE}")
    print(f"Image Size   : {config.IMAGE_SIZE}")

    results = predict_images()

    display_results(results)

    show_output_location()

    print("\n✅ Prediction Process Completed Successfully!")


if __name__ == "__main__":
    main()