import imageio
import os

def save_video(frames, output_path, fps):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    imageio.mimsave(output_path, frames, fps=fps)
