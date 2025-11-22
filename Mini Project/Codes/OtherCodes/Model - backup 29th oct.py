
from rfdetr import RFDETRBase
from pathlib import Path
import torch
import os

def get_image_paths(path):
    """Return a list of image paths if folder, or a single-item list if file."""
    path = Path(path)
    if path.is_dir():
        return [
            str(p) for p in path.iterdir()
            if p.suffix.lower() in ('.png', '.jpg', '.jpeg', '.tif')
        ]
    elif path.is_file():
        return [str(path)]
    else:
        raise FileNotFoundError(f"No such file or directory: {path}")

if __name__ == "__main__":
    model = RFDETRBase()

    # Define paths
    dataset_dir = Path(r"E:/251100670036/TestFolder/Dataset")
    output_dir = Path(r"E:/251100670036/TestFolder/Outputs")
    checkpoint_path = output_dir / "checkpoint_best_ema.pth"

    # Check if checkpoint exists for resuming
    resume_training = checkpoint_path.exists()

    # Ensure proper torch mode for CPU training
    if torch.is_inference_mode_enabled():
        torch.set_inference_mode(False)
    torch.set_grad_enabled(True)

    # TRAINING ON CPU
    model.train(
        dataset_dir=str(dataset_dir),
        epochs=90,
        batch_size=1,       # small for CPU
        grad_accum_steps=8,
        lr=5e-4,
        scheduler="cosine",
        output_dir=str(output_dir),
        num_workers=0,
        device="cpu",       # force CPU
        amp=False,          # disable automatic mixed precision
        resume=str(checkpoint_path) if resume_training else None,
        eval_interval=5
    )

    # Get list of image paths from test folder
    test_images = get_image_paths(dataset_dir / "test")

    print(f"Found {len(test_images)} test images.")
    print(test_images[:5])  # show a few name

    # PREDICTION ON CPU
    model.predict(
        dataset_dir=str(dataset_dir),
        images=test_images,     # ✅ list of images, not folder
        output_dir=str(output_dir),
        batch_size=1,
        num_workers=0,
        device="cpu",
        amp=False,
        eval_interval=0
    )

    print(f"\n✅ Prediction completed! Results saved in: {output_dir}")





# from rfdetr import RFDETRBase
# from pathlib import Path

# if __name__ == "__main__":
#     # ===============================
#     # Initialize model
#     # ===============================
#     model = RFDETRBase(num_classes=1, pretrained=True, use_pretrained_backbone=True)

#     checkpoint_path = Path(r"E:/251100670036/TestFolder/Outputs/checkpoint.pth")
#     resume_training = checkpoint_path.exists()  # Only resume if checkpoint exists

#     # ===============================
#     # STAGE 1: Freeze backbone (fast training)
#     # ===============================
#     for param in model.model.model.backbone.parameters():
#         param.requires_grad = False

#     trainable_params = sum(p.numel() for p in model.model.model.parameters() if p.requires_grad)
#     total_params = sum(p.numel() for p in model.model.model.parameters())
#     print(f"Trainable parameters: {trainable_params} / {total_params}")

#     model.train(
#         dataset_dir=r"E:/251100670036/TestFolder/Dataset",
#         epochs=5,                # Stage 1 epochs
#         batch_size=1,
#         grad_accum_steps=1,
#         lr=1e-4,
#         output_dir=r"E:/251100670036/TestFolder/Outputs/Stage1",
#         num_workers=0,
#         device="cpu",
#         amp=False,
#         resume=str(checkpoint_path) if resume_training else None
#     )

#     # ===============================
#     # STAGE 2: Unfreeze backbone (fine-tuning)
#     # ===============================
#     for param in model.model.backbone.parameters():
#         param.requires_grad = True

#     trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
#     print(f"Stage 2 - Trainable parameters: {trainable_params} / {total_params}")

#     # Resume from Stage 1 checkpoint
#     stage1_checkpoint = Path(r"E:/251100670036/TestFolder/Outputs/Stage1/checkpoint.pth")
#     resume_stage2 = stage1_checkpoint.exists()

#     model.train(
#         dataset_dir=r"E:/251100670036/TestFolder/Dataset",
#         epochs=5,                # Stage 2 epochs
#         batch_size=1,
#         grad_accum_steps=1,
#         lr=5e-5,                 # smaller LR for fine-tuning
#         output_dir=r"E:/251100670036/TestFolder/Outputs/Stage2",
#         num_workers=0,
#         device="cpu",
#         amp=False,
#         resume=str(stage1_checkpoint) if resume_stage2 else None
#     )

#     # ===============================
#     # Prediction on all test images
#     # ===============================
#     model.predict(
#         dataset_dir=r"E:/251100670036/TestFolder/Dataset",
#         output_dir=r"E:/251100670036/TestFolder/Outputs/Predictions",
#         batch_size=1,
#         num_workers=0,
#         device="cpu",
#         amp=False
#     )






