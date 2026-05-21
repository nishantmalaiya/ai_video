from PIL import Image

def generate_frames(pipe, image_path, settings):
    image = Image.open(image_path).convert("RGB")

    result = pipe(
        image=image,
        num_frames=settings.NUM_FRAMES,
        motion_bucket_id=settings.MOTION_BUCKET_ID,
        noise_aug_strength=settings.NOISE_AUG_STRENGTH
    )

    return result.frames
