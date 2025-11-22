from rfdetr import RFDETRBase
from pathlib import Path
from PIL import Image
import torch
import supervision as sv  # used for visualization
import numpy as np
import os

# Paths
dataset_dir = Path("/data/shreyas25/dataset")
output_dir  = Path("/data/shreyas25/Output")
checkpoint  = output_dir / "checkpoint_best_ema.pth"
test_dir    = dataset_dir / "test"
save_dir    = output_dir / "inference_results"

# Create output folder
save_dir.mkdir(parents=True, exist_ok=True)

# Load model
print("Loading pretrained weights...")
model = RFDETRBase()
print("✅ Loaded RF-DETR model")

# Optional: make inference faster
# model.optimize_for_inference()

# Collect all images recursively
image_files = [f for f in test_dir.rglob("*") if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".tif"]]
print(f"🔍 Found {len(image_files)} images in {test_dir.resolve()}")

if not image_files:
    raise FileNotFoundError("❌ No image files found in test directory or subfolders.")

# Lower confidence threshold (in case it’s too strict)
model.confidence_threshold = 0.001

# Run predictions one by one (so we can save results manually)
for i, img_path in enumerate(image_files):
    try:
        preds = model.predict(images=[str(img_path)], output_dir=None, amp=True)
        
        # preds is a list of dicts (one per image)
        if not preds or "detections" not in preds[0]:
            print(f"⚠️ No detections for {img_path.name}")
            continue

        det = preds[0]["detections"]

        # Visualize using supervision (same as Roboflow's visualizer)
        image = np.array(Image.open(img_path).convert("RGB"))
        annotator = sv.Detections.from_inference(preds[0])
        annotated_image = sv.draw_detections(image, annotator)

        # Save result
        save_path = save_dir / img_path.name
        Image.fromarray(annotated_image).save(save_path)
        print(f"✅ Saved: {save_path.name}")

    except Exception as e:
        print(f"❌ Error processing {img_path.name}: {e}")

print(f"\n✅ All done. Saved results in: {save_dir}")
