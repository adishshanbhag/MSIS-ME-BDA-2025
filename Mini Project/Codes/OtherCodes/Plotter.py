import json
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score

LOG_FILE = r"E:\251100670036\TestFolder\Outputs\log.txt"

# --- 1️⃣ Parse Log File ---
epochs = []
train_ce, train_bbox, train_giou = [], [], []
val_ce, val_bbox, val_giou = [], [], []
lrs = []

base_map50, base_map5095, base_precision, base_recall = [], [], [], []
ema_map50, ema_map5095, ema_precision, ema_recall = [], [], [], []

with open(LOG_FILE, 'r') as f:
    for line in f:
        data = json.loads(line)
        ep = data["epoch"]
        epochs.append(ep)
        
        # Losses
        train_ce.append(data["train_loss_ce"])
        train_bbox.append(data["train_loss_bbox"])
        train_giou.append(data["train_loss_giou"])

        val_ce.append(data["test_loss_ce"])
        val_bbox.append(data["test_loss_bbox"])
        val_giou.append(data["test_loss_giou"])

        lrs.append(data["train_lr"])

        # Base model metrics
        base_map50.append(data["test_results_json"]["map"])
        base_map5095.append(data["test_coco_eval_bbox"][0])
        base_precision.append(data["test_results_json"]["precision"])
        base_recall.append(data["test_results_json"]["recall"])

        # EMA model metrics
        ema_map50.append(data["ema_test_results_json"]["map"])
        ema_map5095.append(data["ema_test_coco_eval_bbox"][0])
        ema_precision.append(data["ema_test_results_json"]["precision"])
        ema_recall.append(data["ema_test_results_json"]["recall"])


# --- 2️⃣ Per-Component Loss Curves ---
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(epochs, train_ce, label='Train CE')
plt.plot(epochs, val_ce, label='Val CE')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.title('Classification Loss (CE)')
plt.legend(); plt.grid(True)

plt.subplot(1,3,2)
plt.plot(epochs, train_bbox, label='Train BBox')
plt.plot(epochs, val_bbox, label='Val BBox')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.title('Bounding Box Loss')
plt.legend(); plt.grid(True)

plt.subplot(1,3,3)
plt.plot(epochs, train_giou, label='Train GIoU')
plt.plot(epochs, val_giou, label='Val GIoU')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.title('GIoU Loss')
plt.legend(); plt.grid(True)

plt.tight_layout()
plt.show()


# --- 3️⃣ Learning Rate Schedule ---
plt.figure(figsize=(7,4))
plt.plot(epochs, lrs, marker='o')
plt.xlabel('Epoch'); plt.ylabel('Learning Rate')
plt.title('Learning Rate Schedule')
plt.grid(True)
plt.show()


# --- 4️⃣ Best Epoch Summary Table ---
# Criteria: Highest mAP@50:95 (EMA model)
best_ep = epochs[np.argmax(ema_map5095)]
print(f"📌 Best Epoch (EMA) based on mAP@50:95: {best_ep}\n")

idx = epochs.index(best_ep)
print(f"{'Metric':<20}{'Base Model':<15}{'EMA Model':<15}")
print("-"*50)
print(f"{'Epoch':<20}{epochs[idx]:<15}{epochs[idx]:<15}")
print(f"{'mAP@0.50':<20}{base_map50[idx]:<15.3f}{ema_map50[idx]:<15.3f}")
print(f"{'mAP@0.50:0.95':<20}{base_map5095[idx]:<15.3f}{ema_map5095[idx]:<15.3f}")
print(f"{'Precision':<20}{base_precision[idx]:<15.3f}{ema_precision[idx]:<15.3f}")
print(f"{'Recall':<20}{base_recall[idx]:<15.3f}{ema_recall[idx]:<15.3f}")


# --- 5️⃣ Precision–Recall Curve (For Best Epoch) ---
# NOTE: This requires per-sample scores & labels. 
# If you don't have them stored, this is a synthetic example.

# Example synthetic PR curve for demonstration:
# y_true = np.random.randint(0, 2, 100)  # Replace with actual ground truth labels for val set
# y_scores = np.random.rand(100)         # Replace with model confidence scores
# precision, recall, _ = precision_recall_curve(y_true, y_scores)
# ap = average_precision_score(y_true, y_scores)

# plt.figure(figsize=(6,6))
# plt.plot(recall, precision, label=f'Best Epoch {best_ep} (AP={ap:.3f})')
# plt.xlabel('Recall'); plt.ylabel('Precision')
# plt.title('Precision–Recall Curve (Example)')
# plt.legend(); plt.grid(True)
# plt.show()


# --- 6️⃣ (Optional) Confusion Matrix ---
# If you have predictions and GTs for the best epoch:
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# y_true_cls = [...]
# y_pred_cls = [...]
# cm = confusion_matrix(y_true_cls, y_pred_cls)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Non-mitosis','Mitosis'])
# disp.plot(cmap='Blues'); plt.title(f'Confusion Matrix - Epoch {best_ep}')
# plt.show()
