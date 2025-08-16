'''
Name: Shan Meng
Date: August 15, 2025
Class: CS6620
Notes: Final Project
'''



def suggest_items(destination, duration, weather="mild", with_kids=False, with_pet=False):
    items = {
        "hygiene": ["toothbrush", "toothpaste", "deodorant"],
        "clothes": ["shirt"] * duration + ["underwear"] * (duration // 2 + 1),
        "electronics": ["phone charger"] + (["adapter"] if destination.lower() not in ["usa", "canada"] else []),
        "extras": []
    }

    # Weather condition
    if weather.lower() == "cold":
        items["clothes"].extend(["jacket", "gloves", "beanie"])
    elif weather.lower() == "rain":
        items["extras"].append("umbrella")
    elif weather.lower() == "hot":
        items["extras"].extend(["hat", "sunscreen"])

    # Kids items
    if with_kids:
        items["kids"] = [
            "diapers (1 pack/day)",
            "baby wipes",
            "formula/bottles",
            "kid's food/snacks",
            "kid's clothes",
            "kid's toy",
            "kid's medicine",
            "stroller/carrier"
        ]

    # Pet items
    if with_pet:
        items["pet"] = [
            "pet food",
            "leash/harness",
            "poop bags",
            "pet's medication",
            "portable water bottle",
            "carrier/crate",
            "pet's toy"
        ]

    return items
