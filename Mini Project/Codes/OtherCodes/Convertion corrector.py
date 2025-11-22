# import json

# with open(r"E:\251100670036\TestFolder\Dataset\test\_annotations.coco.json", "r") as f:
#     data = json.load(f)

# for img in data["images"]:
#     if img["file_name"].startswith("test/"):
#         img["file_name"] = img["file_name"][len("test/"):]  # remove prefix

# with open(r"E:\251100670036\TestFolder\Dataset\test\_annotations.coco.json", "w") as f:
#     json.dump(data, f, indent=2)

# print("Fixed file_name paths saved to mitosis_coco_fixed.json")
import json
from pathlib import Path

# --- CONFIGURE THESE PATHS ---
dataset_root = Path(r"E:/251100670036/TestFolder/Dataset")
splits = ["train", "valid", "test"]  # subfolders

for split in splits:
    ann_file = dataset_root / split / "_annotations.coco.json"
    
    if not ann_file.exists():
        print(f"Skipping {ann_file}, file not found")
        continue

    with open(ann_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add info if missing
    if "info" not in data:
        data["info"] = {
            "description": "Mitosis Dataset",
            "version": "1.0",
            "year": 2025,
            "contributor": "Adish Shanbhag",
            "date_created": "2025-09-25"
        }

    # Add licenses if missing
    if "licenses" not in data:
        data["licenses"] = [
            {"id": 1, "name": "Unknown", "url": ""}
        ]

    # Fix file_name to be relative to folder
    for img in data.get("images", []):
        fn = Path(img["file_name"])
        # Keep only relative path inside the split folder
        if fn.parts[0] == split:
            img["file_name"] = str(Path(*fn.parts[1:]))
        else:
            img["file_name"] = str(fn)

    # Save back
    with open(ann_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated {ann_file}")
