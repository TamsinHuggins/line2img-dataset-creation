# Line Drawing Dataset Creation

This Python project converts a batch of photo images into line drawings, creating a dataset for training generative AI models. The dataset can be used to train models that translate line drawings into photo-realistic images.

## Features

- **Batch Processing**: Automatically processes images from subdirectories.
- **Edge Detection**: Uses Gaussian smoothing and Sobel filters to generate clean line drawings.
- **Flattened Output**: Outputs all processed images into a single folder for easy dataset handling.

## Requirements

- Python 3.x
- Libraries: `numpy`, `scipy`, `matplotlib`, `imageio`

Install dependencies:
```bash
pip install numpy scipy matplotlib imageio