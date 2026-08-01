"""
=========================================================
AI Skin Analyzer
Streamlit Web Application
=========================================================
Author : Loga Vignesh
=========================================================
"""

import sys
import tempfile
from pathlib import Path

import streamlit as st
from PIL import Image
from ultralytics import YOLO

# =========================================================
# PROJECT PATH
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

# =========================================================
# IMPORT PROJECT MODULES
# =========================================================

from src import config
from src.recommendation import get_recommendation

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Skin Analyzer",
    page_icon="🩺",
    layout="wide",
)
# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* Main Page Padding */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

/* Center Title */
h1{
    text-align:center;
    color:#00D4AA;
}

/* Center Subtitle */
h2,h3{
    color:#00D4AA;
}

/* Metric Cards */
[data-testid="stMetric"]{
    border:1px solid #31333F;
    border-radius:12px;
    padding:15px;
    background-color:#161B22;
    text-align:center;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:10px;
}

/* Download Button */
.stDownloadButton>button{
    width:100%;
    border-radius:10px;
}

/* Expander */
.streamlit-expanderHeader{
    font-size:18px;
    font-weight:bold;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#161B22;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

st.title("🩺 AI Skin Analyzer")

st.markdown("""
## AI-powered Skin Disease Detection & Personalized Skincare Recommendations

Upload a facial image and let our **YOLOv11 Deep Learning Model**
identify common skin conditions and suggest suitable skincare routines.

Supported Skin Conditions:

- ✅ Acne
- ✅ Rosacea
- ✅ Pigmentation
- ✅ Black Heads
- ✅ Flakiness
- ✅ Eczema

---
""")

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🩺 AI Skin Analyzer")

    st.success("✅ YOLOv11 Model Loaded")

    st.divider()

    st.subheader("📌 Model Information")

    st.write(f"**Model :** {config.MODEL_NAME}")
    st.write(f"**Image Size :** {config.IMAGE_SIZE}")
    st.write(f"**Device :** {config.DEVICE}")

    st.divider()

    st.subheader("🦠 Supported Skin Conditions")

    st.markdown("""
✅ Acne

✅ Rosacea

✅ Pigmentation

✅ Black Heads

✅ Flakiness

✅ Eczema
""")

    st.divider()

    st.subheader("👨‍💻 Developer")

    st.write("**Loga Vignesh**")

    st.caption("AI & Machine Learning Engineer")

    st.divider()

    st.info(
        "⚠ This application is intended for educational and research purposes only."
    )

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    if not config.BEST_MODEL.exists():

        st.error(
            f"Model not found:\n{config.BEST_MODEL}"
        )

        st.stop()

    return YOLO(str(config.BEST_MODEL))


model = load_model()

# =========================================================
# IMAGE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(

    "📤 Upload Skin Image",

    type=[
        "jpg",
        "jpeg",
        "png"
    ]

)

# =========================================================
# IF IMAGE IS UPLOADED
# =========================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    # =========================================================
# IMAGE DISPLAY
# =========================================================

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("📷 Original Image")

        st.image(
            image,
            use_container_width=True
        )

  
    # -----------------------------------------------------

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    image.save(temp_file.name)

    st.success("✅ Image uploaded successfully.")
        # =========================================================
    # RUN YOLO PREDICTION
    # =========================================================

    with st.spinner("🔍 Analyzing skin image..."):

        results = model.predict(
            source=temp_file.name,
            imgsz=config.IMAGE_SIZE,
            conf=0.25,
            verbose=False
        )

    result = results[0]

    # =========================================================
    # DISPLAY PREDICTED IMAGE
    # =========================================================

    with col2:
        with st.container(border=True):
            st.subheader("🧠 AI Prediction")

            annotated_image = result.plot()

            st.image(
                annotated_image,
                channels="BGR",
                use_container_width=True
            )

    # =========================================================
    # DETECTION RESULTS
    # =========================================================

    st.divider()

    st.header("🔍 Detection Results")
    # =========================================================
# AI DIAGNOSIS SUMMARY
# =========================================================

diagnosis_container = st.container(border=True)


if len(result.boxes) == 0:

        st.warning("No skin issue detected.")

else:

        detected_issues = set()

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

            st.metric(
                label=class_name,
                value=f"{confidence:.2%}"
            )
                # =========================================================
    # SKINCARE RECOMMENDATIONS
    # =========================================================

if len(result.boxes) > 0:

        st.divider()

        st.header("🩺 Skincare Recommendations")

        for issue in sorted(detected_issues):

            skin_issue, recommendation = get_recommendation(issue)

            if recommendation is None:
                continue

            with st.expander(
                f"📌 {skin_issue}",
                expanded=True
            ):

                # ------------------------------------------------

                st.subheader("📖 Description")

                st.write(
                    recommendation["description"]
                )

                st.divider()

                # ------------------------------------------------

                st.subheader(
                    "🧪 Recommended Ingredients"
                )

                for ingredient in recommendation["ingredients"]:

                    st.markdown(
                        f"✅ {ingredient}"
                    )

                st.divider()

                # ------------------------------------------------

                st.subheader(
                    "🧴 Recommended Products"
                )

                for product in recommendation["products"]:

                    st.markdown(
                        f"• {product}"
                    )

                st.divider()

                # ------------------------------------------------

                morning_col, night_col = st.columns(2)

                with morning_col:

                    st.subheader(
                        "🌞 Morning Routine"
                    )

                    for step in recommendation["morning"]:

                        st.markdown(
                            f"✔ {step}"
                        )

                with night_col:

                    st.subheader(
                        "🌙 Night Routine"
                    )

                    for step in recommendation["night"]:

                        st.markdown(
                            f"✔ {step}"
                        )

                st.divider()

                # ------------------------------------------------

                st.subheader(
                    "⚠️ Things to Avoid"
                )

                for item in recommendation["avoid"]:

                    st.markdown(
                        f"❌ {item}"
                    )
                        # =========================================================
    # PREDICTION STATISTICS
    # =========================================================

if len(result.boxes) > 0:

        st.divider()

        st.header("📊 Prediction Statistics")

        total_detections = len(result.boxes)

        highest_confidence = max(
            float(box.conf[0])
            for box in result.boxes
        )

        average_confidence = (
            sum(
                float(box.conf[0])
                for box in result.boxes
            )
            / total_detections
        )

        stat1, stat2, stat3 = st.columns(3)

        with stat1:

            st.metric(
                "Detected Issues",
                total_detections
            )

        with stat2:

            st.metric(
                "Highest Confidence",
                f"{highest_confidence:.2%}"
            )

        with stat3:

            st.metric(
                "Average Confidence",
                f"{average_confidence:.2%}"
            )

    # =========================================================
    # DOWNLOAD IMAGE
    # =========================================================

    st.divider()

    st.header("📥 Download Prediction")

    prediction_image = Image.fromarray(
        annotated_image
    )

    buffer = tempfile.NamedTemporaryFile(
        suffix=".png",
        delete=False
    )

    prediction_image.save(buffer.name)

    with open(buffer.name, "rb") as file:

        st.download_button(

            label="⬇ Download Annotated Image",

            data=file,

            file_name="prediction.png",

            mime="image/png"

        )

# =========================================================
# NO IMAGE UPLOADED
# =========================================================
if uploaded_file is None:

    st.info(
        "👆 Upload a skin image to begin analysis."
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
"""
---
### 🩺 AI Skin Analyzer

Developed by **Loga Vignesh**

### 🚀 Technology Stack

- YOLOv11
- Python
- Streamlit
- OpenCV
- Ultralytics
- Deep Learning

### ⚠ Disclaimer

This application is intended for educational
and research purposes only.

It is **not** a substitute for professional
medical diagnosis.

Always consult a qualified dermatologist
for medical advice.
"""
)
