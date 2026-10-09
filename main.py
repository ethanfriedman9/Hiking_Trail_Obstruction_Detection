import torch
from model import load_model

def train_model():
  device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
  )
  model = load_model().to(device)
  

if __name__ == "__main__":
  train_model()
