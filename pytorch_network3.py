#### Libraries
# Standard library
import pickle
import gzip

# Third-party libraries
import numpy as np
import torch
import torch.nn

#### Constants
print("Ready to go Cap !")

#### Load the MNIST data *Converted
def load_data(path="C:/python_files/", filename="mnist.pkl.gz"):
    f = gzip.open(path + filename, 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
    f.close()
    def to_tensor(data):
        tensor_x = torch.from_numpy(data[0].astype(np.float32))
        tensor_y = torch.from_numpy(data[1].astype(np.int32))
        return tensor_x, tensor_y
    return [to_tensor(training_data), to_tensor(validation_data), to_tensor(test_data)]

class Test_ConvPoolLayer(object):
    
    def __init__(self, training_data, conv_properties, poolsize=(2, 2)):
        ''' conv_properties = (number of feature maps, LRF_height, LRF_width)
        LRF - Local Receptive Field
        
        self.training_data is a tensor, has a form of (n_images, in_channels, iH, iW)

        self.w is also a tensor with a form of 
        (n_featur_maps, out_channels, in_channels/groups, kH, kW)

        self.conv_z is a list of tensors

        '''
        self.training_data = torch.reshape(training_data[0], (-1, 1, 28, 28))
        n_out = (np.prod(conv_properties)/np.prod(poolsize))

        #### Initialize weights and biases
        self.w = torch.reshape(torch.from_numpy(np.random.normal(
            loc=0.0, scale=np.sqrt(1.0/n_out), size=conv_properties).astype(np.float32)),
                (conv_properties[0], 1, 1, conv_properties[1], conv_properties[2]))
        self.b = torch.zeros(conv_properties[0], 1)

        #### Copute activations for each feature map and stope them in a list as tensors 
        self.conv_z = []
        for feature_map in range(conv_properties[0]):
            self.feature_map_z = torch.nn.functional.conv2d(
                self.training_data[:1], self.w[feature_map], self.b[feature_map])
            self.conv_z.append(self.feature_map_z)
    pass