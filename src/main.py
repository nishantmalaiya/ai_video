from config import settings
from src.model_loader import load_model
from src.video_generator import generate_frames
from src.video_writer import save_video


def main():
    print("Loading model...")
    pipe = load_model(settings.MODEL_NAME)

    print("Generating frames...")
    frames = generate_frames(
        pipe,
        settings.INPUT_IMAGE_PATH,
        settings
    )

    print("Saving video...")
    save_video(
        frames,
        settings.OUTPUT_VIDEO_PATH,
        settings.FPS
    )

    print("✅ Video generated:", settings.OUTPUT_VIDEO_PATH)


if __name__ == "__main__":
    main()
