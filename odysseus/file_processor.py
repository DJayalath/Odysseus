import numpy as np
import os
from random import randrange
from .globals import FILE_TYPE_SET, SAMPLE_SIZE, SAMPLE_LENGTH

# Processes files in dataset and saves the byte arrays
class FileProcessor:
    
    @staticmethod
    def read_file(f):
        in_file = open(f, "rb")
        ba = bytearray(in_file.read())
        in_file.close()

        first_bytes = [(float(i) / 255.0) for i in ba[:SAMPLE_LENGTH]]

        last_bytes = [(float(i) / 255.0) for i in ba[-SAMPLE_LENGTH:]]

        return np.array(first_bytes + last_bytes)
