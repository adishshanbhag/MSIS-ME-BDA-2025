from pycocotools.coco import COCO

coco = COCO(r"E:\251100670036\TestFolder\Dataset\test\_annotations.coco.json")
print("Number of images:", len(coco.getImgIds()))
print("Number of annotations:", len(coco.getAnnIds()))