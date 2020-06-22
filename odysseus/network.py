import numpy as np
import tensorflow as tf
from .file_processor import FileProcessor

class Network:

    def __init__(self):
        # Load the TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path="odysseus/model.tflite")
        self.interpreter.allocate_tensors()

        # Get input and output tensors.
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # Test the model on random input data.
        self.input_shape = self.input_details[0]['shape']

    def softmax(self,x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def predict(self, file):

        data = np.array([FileProcessor.read_file(file)])

        self.interpreter.set_tensor(self.input_details[0]['index'], np.array(data, dtype=np.float32))
        self.interpreter.invoke()

        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        return self.softmax(output_data[0])
