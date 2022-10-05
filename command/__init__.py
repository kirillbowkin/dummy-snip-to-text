import easyocr
import torch

window_name = "Screenshot"
reader = easyocr.Reader(["en", "ru"], gpu=torch.cuda.is_available())