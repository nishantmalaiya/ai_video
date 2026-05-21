import torch
from diffusers import StableVideoDiffusionPipeline

def load_model(model_name: str):
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda")
    pipe.enable_model_cpu_offload()
    return pipe
