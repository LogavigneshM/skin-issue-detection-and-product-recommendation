"""
=========================================================
AI Skin Analyzer
Recommendation Engine
=========================================================
Author : Loga Vignesh
=========================================================
"""

# =========================================================
# SKINCARE RECOMMENDATION DATABASE
# =========================================================

SKINCARE_DATABASE = {

    "Acne": {

        "description":
        "Acne is a common skin condition caused by clogged pores, excess oil production, bacteria, and inflammation.",

        "ingredients": [
            "Salicylic Acid",
            "Niacinamide",
            "Benzoyl Peroxide"
        ],

        "products": [
            "CeraVe Acne Control Cleanser",
            "Minimalist 2% Salicylic Acid Serum",
            "The Ordinary Niacinamide 10%"
        ],

        "morning": [
            "Gentle Cleanser",
            "Niacinamide Serum",
            "Oil-Free Moisturizer",
            "Broad Spectrum Sunscreen (SPF 50)"
        ],

        "night": [
            "Gentle Cleanser",
            "Salicylic Acid Serum",
            "Moisturizer"
        ],

        "avoid": [
            "Picking pimples",
            "Harsh scrubs",
            "Sleeping with makeup"
        ]
    },

    "Black Heads": {

        "description":
        "Blackheads are open clogged pores caused by excess oil and dead skin cells.",

        "ingredients": [
            "Salicylic Acid",
            "Retinol",
            "Niacinamide"
        ],

        "products": [
            "COSRX BHA Blackhead Power Liquid",
            "Minimalist Salicylic Acid Serum",
            "CeraVe Foaming Facial Cleanser"
        ],

        "morning": [
            "Foaming Cleanser",
            "Niacinamide Serum",
            "Oil-Free Moisturizer",
            "Broad Spectrum Sunscreen"
        ],

        "night": [
            "Cleanser",
            "BHA Exfoliant",
            "Moisturizer"
        ],

        "avoid": [
            "Over washing",
            "Squeezing blackheads",
            "Using pore strips frequently"
        ]
    },

    "Eczema": {

        "description":
        "Eczema is a chronic condition that causes dry, itchy, and inflamed skin.",

        "ingredients": [
            "Ceramides",
            "Colloidal Oatmeal",
            "Hyaluronic Acid"
        ],

        "products": [
            "CeraVe Moisturizing Cream",
            "Aveeno Eczema Therapy",
            "Cetaphil Moisturizing Lotion"
        ],

        "morning": [
            "Gentle Cleanser",
            "Moisturizer",
            "Mineral Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Thick Moisturizer"
        ],

        "avoid": [
            "Hot showers",
            "Harsh soaps",
            "Scratching the skin"
        ]
    },

    "Rosacea": {

        "description":
        "Rosacea causes redness, flushing, and visible blood vessels on the face.",

        "ingredients": [
            "Azelaic Acid",
            "Niacinamide",
            "Ceramides"
        ],

        "products": [
            "The Ordinary Azelaic Acid",
            "La Roche-Posay Toleriane",
            "CeraVe Moisturizing Lotion"
        ],

        "morning": [
            "Gentle Cleanser",
            "Azelaic Acid",
            "Moisturizer",
            "Broad Spectrum Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Moisturizer"
        ],

        "avoid": [
            "Alcohol",
            "Spicy food",
            "Extreme temperatures"
        ]
    },

    "Flakiness": {

        "description":
        "Flaky skin is usually caused by dryness, irritation, or a damaged skin barrier.",

        "ingredients": [
            "Ceramides",
            "Glycerin",
            "Hyaluronic Acid"
        ],

        "products": [
            "Cetaphil Moisturizer",
            "CeraVe Moisturizing Cream",
            "Vaseline Intensive Care Lotion"
        ],

        "morning": [
            "Hydrating Cleanser",
            "Moisturizer",
            "Broad Spectrum Sunscreen"
        ],

        "night": [
            "Hydrating Cleanser",
            "Moisturizer"
        ],

        "avoid": [
            "Hot water",
            "Harsh cleansers",
            "Over exfoliation"
        ]
    },

    "Pigmentation": {

        "description":
        "Pigmentation occurs due to excess melanin production and uneven skin tone.",

        "ingredients": [
            "Vitamin C",
            "Niacinamide",
            "Alpha Arbutin"
        ],

        "products": [
            "Minimalist Vitamin C Serum",
            "The Ordinary Alpha Arbutin",
            "Minimalist Niacinamide Serum"
        ],

        "morning": [
            "Gentle Cleanser",
            "Vitamin C Serum",
            "Moisturizer",
            "Broad Spectrum Sunscreen"
        ],

        "night": [
            "Gentle Cleanser",
            "Alpha Arbutin Serum",
            "Moisturizer"
        ],

        "avoid": [
            "Sun Exposure",
            "Skipping Sunscreen"
        ]
    }
}


# =========================================================
# GET RECOMMENDATION
# =========================================================

def get_recommendation(issue):
    """
    Return recommendation dictionary.
    Accepts input in any letter case.
    """

    issue = issue.strip().lower()

    for skin_issue, details in SKINCARE_DATABASE.items():

        if skin_issue.lower() == issue:
            return skin_issue, details

    return None, None


# =========================================================
# DISPLAY RECOMMENDATION
# =========================================================

def display_recommendation(issue):
    """
    Display skincare recommendation.
    """

    skin_issue, recommendation = get_recommendation(issue)

    if recommendation is None:
        print(f"\n❌ No recommendation available for '{issue}'.")
        return

    print("\n" + "=" * 60)
    print(f"Skin Issue : {skin_issue}")
    print("=" * 60)

    print("\nDescription")
    print("-" * 60)
    print(recommendation["description"])

    print("\nRecommended Ingredients")
    print("-" * 60)
    for ingredient in recommendation["ingredients"]:
        print(f"• {ingredient}")

    print("\nRecommended Products")
    print("-" * 60)
    for product in recommendation["products"]:
        print(f"• {product}")

    print("\n🌞 Morning Routine")
    print("-" * 60)
    for step in recommendation["morning"]:
       print(f"• {step}")

    print("\n🌙 Night Routine")
    print("-" * 60)
    for step in recommendation["night"]:
       print(f"• {step}")

    print("\n⚠️ Things to Avoid")
    print("-" * 60)
    for item in recommendation["avoid"]:
       print(f"• {item}")
       
    return recommendation

# =========================================================
# MAIN
# =========================================================

def main():

    print("=" * 60)
    print("AI Skin Analyzer - Recommendation Engine")
    print("=" * 60)

    issue = input(
        "\nEnter Skin Issue\n"
        "(Acne, Black Heads, Eczema, Rosacea, Flakiness, Pigmentation): "
    )

    display_recommendation(issue)


if __name__ == "__main__":
    main()