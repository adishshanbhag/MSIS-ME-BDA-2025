import os
import json
from PIL import Image

dataset_root = r"E:/251100670036/TestFolder/Dataset"
test_root = os.path.join(dataset_root, "test")  # Folder containing your test images

coco_test = {
    "images": [],
    "annotations": [],  # empty because no ground truth
    "categories": [{"id": 1, "name": "mitosis", "supercategory": "none"}]
}

img_id = 1

for folder in sorted(os.listdir(test_root)):
    folder_path = os.path.join(test_root, folder)
    if not os.path.isdir(folder_path):
        continue

    for fname in sorted(os.listdir(folder_path)):
        if not fname.lower().endswith((".tif", ".png", ".jpg", ".jpeg")):
            continue

        img_path = os.path.join(folder_path, fname)
        with Image.open(img_path) as img:
            w, h = img.size

        coco_test["images"].append({
            "id": img_id,
            "file_name": f"Test/{folder}/{fname}",  # relative path
            "width": w,
            "height": h
        })

        img_id += 1

# Save test JSON
output_file = os.path.join(dataset_root, "test_coco.json")
with open(output_file, "w") as f:
    json.dump(coco_test, f, indent=2)

print(f"Test COCO JSON saved to {output_file} with {img_id-1} images and 0 annotations.")
