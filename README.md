# Line Drawing Dataset Creation

This Python project converts a batch of photo images into line drawings, creating a dataset for training generative AI models. The dataset can be used to train models that translate line drawings into photo-realistic images.

## Features

- **Directory flattening**: Dataset for line2img training will have just 2 directories: images and line drawings. Original image dataset will be flattened.
- **Edge Detection**: Uses Gaussian smoothing and Sobel filters to generate clean line drawings.
- **Flattened Output**: Outputs all processed images into a single folder for easy dataset handling.

## Requirements

- Python 3.x
- Libraries: `numpy`, `scipy`, `matplotlib`, `imageio`

Install dependencies:

``` 
pip install numpy scipy matplotlib imageio
```



## Todos

- Flatten image dataset
- Process images to all be of standard dimensionality
- Run line drawing generation code
- code that will pick out generated line drawings that are almost entirely black or almost entirely white
   - delete both line drawing and original image from dataset 
