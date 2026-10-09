# Hiking Trail Obstruction Detection

## Overview

This project uses deep learning to identify obstructions on hiking trails from images.

The goal is to train a segmentation model that can distinguish between:

* **Vegetation** — vegetation, grass, and trees
* **Trail** — the walkable hiking trail
* **Obstacle** — objects or areas obstructing the trail
* **Sky** — sky

The model is trained using data from two different datasets.

## How It Works

The program uses a DeepLabV3 image segmentation model with a Resnet50 CNN. The model assigns a class to individual pixels to help determine what portion of the trail is obstructed.

This allows the program to determine whether an obstruction exists and where the obstruction is.

## Datasets

The project currently uses two datasets: Freiburg Forest and TerrainSense.

The Freiburg Forest dataset provides images and pixel-level segmentation masks.

The TerrainSense dataset provides images with obstacle annotations in the form of bounding boxes

Both datasets are adjusted to have output labels fitting the 3 class format.

## Technologies

* **Python**
* **PyTorch**

## References

* [Freiburg Forest](https://deepscene.cs.uni-freiburg.de/)
* [TerrainSense](https://data.mendeley.com/datasets/r6cmjrr6kv/2)
* [DeepLabV3](https://pytorch.org/hub/pytorch_vision_deeplabv3_resnet101/)
