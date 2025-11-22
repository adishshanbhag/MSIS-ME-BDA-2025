from pathlib import Path

test_dir = Path(r"E:/251100670036/TestFolder/Dataset/test")
images = [str(p) for p in test_dir.iterdir() if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.tif')]

print("Number of test images:", len(images))
print(images[:5])