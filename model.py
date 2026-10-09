import torch
from torchvision.models.segmentation import deeplabv3_resnet50, DeepLabV3_ResNet50_Weights

def load_model():
  """
  Loads a DeepLabV3 segmentation model with a Resnet50 CNN with default weights

  Outputs 4 segmentation classes: Vegetation, Trail, Obstruction, Sky
  """
  model = deeplabv3_resnet50(weights=DeepLabV3_ResNet50_Weights.DEFAULT)

  model.classifier[4] = torch.nn.Conv2d(256, 4, 1)
  model.aux_classifier[4] = torch.nn.Conv2d(256, 4, 1)

  return model
