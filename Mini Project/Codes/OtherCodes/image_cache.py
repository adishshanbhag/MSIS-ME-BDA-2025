from pathlib import Path
import cv2, numpy as np
import albumentations as A

# Define paths
src = Path(r"E:\251100670036\TestFolder\Dataset\train")
dst = Path(r"E:\251100670036\TestFolder\Dataset\train_cached")
dst.mkdir(exist_ok=True)

# Resize + normalize ahead of time
transform = A.Compose([
    A.Resize(512, 512),
    A.Normalize(mean=(0.5,), std=(0.5,))
])

for img_path in src.glob("*.tif"):
    img = cv2.imread(str(img_path))
    img = transform(image=img)["image"]
    np.save(dst / (img_path.stem + ".npy"), img)

print("✅ Cached images saved to:", dst)
