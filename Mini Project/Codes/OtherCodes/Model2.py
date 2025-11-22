from rfdetr import RFDETRBase
from pathlib import Path
import torch
import os

def freeze_backbone(model):
    """Freeze the backbone parameters (no gradient updates)."""
    target = None
    # progressively search deeper until backbone is found
    if hasattr(model, "backbone"):
        target = model.backbone
    elif hasattr(model, "model"):
        if hasattr(model.model, "backbone"):
            target = model.model.backbone
        elif hasattr(model.model, "model") and hasattr(model.model.model, "backbone"):
            target = model.model.model.backbone

    if target is not None:
        target.eval()
        for param in target.parameters():
            param.requires_grad = False
        print("🧊 Backbone frozen successfully.")
    else:
        print("⚠️ No backbone found (even in nested models).")

def unfreeze_backbone(model):
    """Unfreeze the backbone parameters (enable fine-tuning)."""
    target = None
    if hasattr(model, "backbone"):
        target = model.backbone
    elif hasattr(model, "model"):
        if hasattr(model.model, "backbone"):
            target = model.model.backbone
        elif hasattr(model.model, "model") and hasattr(model.model.model, "backbone"):
            target = model.model.model.backbone

    if target is not None:
        target.train()
        for param in target.parameters():
            param.requires_grad = True
        print("🔥 Backbone unfrozen for fine-tuning.")
    else:
        print("⚠️ No backbone found (even in nested models).")


if __name__ == "__main__":
    model = RFDETRBase()

    # Define paths
    dataset_dir = Path(r"E:/251100670036/TestFolder/Dataset")
    output_dir = Path(r"E:/251100670036/TestFolder/Outputs")
    checkpoint_path = output_dir / "checkpoint_best_ema.pth"

    # Check if checkpoint exists for resuming
    resume_training = checkpoint_path.exists()

    # Torch mode for CPU
    if torch.is_inference_mode_enabled():
        torch.set_inference_mode(False)
    torch.set_grad_enabled(True)

    # ------------------ FREEZE PHASE ------------------
    # Freeze backbone for first N epochs
    print("Model attributes:")
    for name, module in model.__dict__.items():
        if not name.startswith("_"):
            print("model.model." + name, "→", type(module))



    freeze_epochs = 15
    freeze_backbone(model)

    # Train for the freeze phase
    model.train(
        dataset_dir=str(dataset_dir),
        epochs=freeze_epochs,
        batch_size=1,
        grad_accum_steps=8,
        lr=1e-4,
        scheduler="cosine",
        output_dir=str(output_dir),
        num_workers=0,
        device="cpu",
        amp=False,
        resume=str(checkpoint_path) if resume_training else None,
        eval_interval=1
    )

    # ------------------ UNFREEZE PHASE ------------------
    unfreeze_backbone(model)

    # Continue training for remaining epochs
    total_epochs = 30
    remaining_epochs = total_epochs - freeze_epochs

    model.train(
        dataset_dir=str(dataset_dir),
        epochs=remaining_epochs,
        batch_size=1,
        grad_accum_steps=8,
        lr=1e-5,  # lower LR for fine-tuning
        scheduler="cosine",
        output_dir=str(output_dir),
        num_workers=0,
        device="cpu",
        amp=False,
        resume=str(checkpoint_path) if (checkpoint_path.exists()) else None,
        eval_interval=5
    )

    # ------------------ PREDICTION ------------------
    model.predict(
        dataset_dir=str(dataset_dir),
        images=Path(r"E:/251100670036/TestFolder/Dataset/test"),
        output_dir=str(output_dir),
        batch_size=1,
        num_workers=0,
        device="cpu",
        amp=False,
        eval_interval=0
    )

    print(f"\n✅ Prediction completed! Results saved in: {output_dir}")
