from rfdetr import RFDETRBase
from pathlib import Path
import torch
import os
from datetime import datetime  # awj cr s 2025-11-12 (for timestamp logging)
# awj cr

if __name__ == "__main__":
    # ---------------------------------------------------------------------
    # AUTO-DETECT BASE DIRECTORY (where this script is located)
    BASE_DIR = Path(__file__).resolve().parent

    # ✅ Use absolute paths (safer)
    dataset_dir = BASE_DIR / "dataset"           # assuming dataset is /data/shreyas25/dataset
    output_dir = BASE_DIR / "Output"
    checkpoint_path = output_dir / "checkpoint.pth"

    # ✅ Check dataset sanity
    train_json = dataset_dir / "train" / "_annotations.coco.json"
    if not train_json.exists():
        raise FileNotFoundError(f"❌ Could not find training annotations at: {train_json}\n"
                                f"→ Check your dataset path and correct it in model.py")

    output_dir.mkdir(parents=True, exist_ok=True)
    model = RFDETRBase()

    resume_training = checkpoint_path.exists()

    if torch.is_inference_mode_enabled():
        torch.set_inference_mode(False)
    torch.set_grad_enabled(True)

    # awj cr s 2025-11-12
    # 🧠 Ensure optimizer/scaler restoration happens if model supports it
    if resume_training:
        print(f"[{datetime.now()}] 🔁 Resuming from checkpoint: {checkpoint_path}")
        try:
            ckpt = torch.load(checkpoint_path, map_location="cuda" if torch.cuda.is_available() else "cpu")
            if hasattr(model, "optimizer") and "optimizer" in ckpt:
                model.optimizer.load_state_dict(ckpt["optimizer"])
                print("✅ Optimizer state restored.")
            if "scaler" in ckpt and hasattr(model, "scaler"):
                model.scaler.load_state_dict(ckpt["scaler"])
                print("✅ AMP scaler state restored.")
            if "scheduler" in ckpt and hasattr(model, "scheduler"):
                model.scheduler.load_state_dict(ckpt["scheduler"])
                print("✅ Scheduler state restored.")
        except Exception as e:
            print(f"⚠️ Warning: Could not restore optimizer/scaler/scheduler state: {e}")
            print("→ Proceeding with model weights only.")

        # 🧩 Lower LR on resume to stabilize
        model.base_lr = 1e-6  # reduce LR
        print(f"⚙️  Learning rate reduced for stability: {model.base_lr}")
    # awj cr

    # ✅ TRAINING
    model.train(
        dataset_dir=str(dataset_dir),
        epochs=70,                 # train up to 75 epochs
        batch_size=1,
        grad_accum_steps=8,
        #awj cr s
        lr=5e-6,  # initially kept it on 5e-5 till 100 epochs. Changed it for training from best ema point for 20 more epochs
        lr_backbone=5e-7,  # initially kept it on 2e-6 till 100 epochs. Changed it for training from best ema point for 20 more epochs
        #continuing training from 49th epoch -- changing the hyperparameters
        # lr = 1e-6,
        # lr_backbone = 1e-7,
        #awj cr
        weight_decay=1e-4,
        scheduler="cosine",
        #awj cr s
        #changing this while training from 49th epoch
        # warmup_steps=1000,
        warmup_steps=200,
        #awj cr
        output_dir=str(output_dir),
        num_workers=0,
        amp=False,
        resume=str(checkpoint_path) if resume_training else None,
        eval_interval=5,
        save_interval=1,
        clip_grad_norm = 1.0, #added while continuing 32 batch training from 49th epoch
        optimizer = "AdamW",
        device = "cuda"
    )

    # awj cr s 2025-11-12
    # 🧩 Optional: Gradient clipping patch inside model.train() if supported
    if hasattr(model, "clip_grad_norm"):
        model.clip_grad_norm = 1.0
        print("✅ Gradient clipping enabled (max norm=1.0)")
    # awj cr

    test_dir = Path("data/shreyas25/dataset/test")
    image_paths = list(test_dir.glob("*.jpg")) + list(test_dir.glob("*.png")) + list(test_dir.glob("*.jpeg"))

    print(f"Found {len(image_paths)} test images.")

    model.predict(
        dataset_dir=str(dataset_dir),
        images=image_paths,       # ✅ pass list of image file paths
        output_dir=str(output_dir),
        batch_size=1,
        num_workers=0,
        amp=False,
        device = "cuda",
        eval_interval=5
    )

    print(f"\n✅ Prediction completed! Results saved in: {output_dir}")
