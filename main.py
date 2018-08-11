import torch
import numpy as np
import draw_window
import input_converter
from conv_net_pytorch import ConvNet

def save():
    path_to_file = "C:/python_files/saved_images/image.png"
    draw_window.image1.save(path_to_file)
    input_converter.convert()
    model = ConvNet()
     
    # Load the model
    model.load_state_dict(torch.load('C:/python_files/pytorch_models/conv_net_model.ckpt'))

    # Test the model
    model.eval()
    greyscale_matrix = input_converter.convert()
    in_image = torch.from_numpy(
                greyscale_matrix.astype(np.float32).reshape(1, 1, 28, 28))
    outputs = model(in_image)
    _, predicted = torch.max(outputs.data, 1)   

    number = str(predicted.item())
    draw_window.cv1.create_text((105, 20), font=("purisa", 16), text=number, tags='number')