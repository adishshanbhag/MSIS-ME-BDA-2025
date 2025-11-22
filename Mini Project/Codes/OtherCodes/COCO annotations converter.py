import os
import json
from PIL import Image


dataset_root = r"E:\251100670036\Test Folder\Dataset"
train_root = os.path.join(dataset_root, "Train")
gt_root = os.path.join(dataset_root, "mitoses_ground_truth")

coco = {
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "mitosis", "supercategory": "none"}]  # Added supercategory
}

img_id = 1
ann_id = 1

# Loop through numbered folders inside Training
for folder in sorted(os.listdir(train_root)):
    folder_path = os.path.join(train_root, folder)
    if not os.path.isdir(folder_path):
        continue

    # Loop through images inside that folder
    for fname in sorted(os.listdir(folder_path)):
        if not fname.lower().endswith((".tif", ".png", ".jpg", ".jpeg")):
            continue

        img_path = os.path.join(folder_path, fname)
        with Image.open(img_path) as img:
            w, h = img.size

        coco["images"].append({
            "id": img_id,
            "file_name": f"Training/{folder}/{fname}",  # relative path
            "width": w,
            "height": h
        })

        # Get corresponding ground truth file
        gt_folder = os.path.join(gt_root, folder)
        gt_file = os.path.join(gt_folder, os.path.splitext(fname)[0] + ".csv")

        if os.path.exists(gt_file):
            with open(gt_file, "r") as f:
                for line in f:
                    x, y = map(int, line.strip().split(","))
                    coco["annotations"].append({
                        "id": ann_id,
                        "image_id": img_id,
                        "category_id": 1,
                        "bbox": [x, y, 32, 32],  # adjust bbox size as needed
                        "area": 32*32,
                        "iscrowd": 0
                    })
                    ann_id += 1

        img_id += 1

# Save COCO JSON
output_file = os.path.join(dataset_root, "mitosis_coco.json")
with open(output_file, "w") as f:
    json.dump(coco, f, indent=2)

print(f"COCO JSON saved to {output_file} with {img_id-1} images and {ann_id-1} annotations.")


