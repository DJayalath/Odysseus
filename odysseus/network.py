import tensorflow as tf
from tensorflow import keras
import numpy as np
from .globals import FILE_TYPE_SET, SAMPLE_SIZE
from .file_processor import FileProcessor
import os

# Neural network that predicts file types
class Network:

    def __init__(self):
        self.model = tf.keras.models.load_model('model/trained')

    def single_predict(self, file):
        pred = self.model.predict(np.array([FileProcessor.read_file(file)]))
        pred[0] = self.softmax(pred[0])
        x = pred[0]
        fts = FILE_TYPE_SET[:]
        print(file)
        for j in range(3):
            idx = np.argmax(x, axis=0)
            prediction = fts[idx]
            prob = x[idx]
            print("    " + prediction + " " + "{:5.2f}%".format(prob * 100))
            x = np.delete(x, idx)
            fts.remove(prediction)

    def softmax(self,x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def explicit_predict(self, folder):
        arr = []
        extension = []
        paths = []
        for path, dirs, files in os.walk(folder):
            for f in files:
                name, ext = os.path.splitext(f)
                ext = ext.lower()
                if ext in FILE_TYPE_SET:
                    paths.append(f)
                    extension.append(ext)
                    arr.append(FileProcessor.read_file(os.path.join(path, f)))
        arr = np.stack(arr, axis=0)
        pred = self.model.predict(arr)
        for i in range(len(pred)):
            pred[i] = self.softmax(pred[i])
        for i in range(len(pred)):
            print(paths[i])
            x = pred[i]
            fts = FILE_TYPE_SET[:]
            for j in range(3):
                idx = np.argmax(x, axis=0)
                prediction = fts[idx]
                prob = x[idx]
                print("    " + prediction + " " + "{:5.2f}%".format(prob * 100))
                x = np.delete(x, idx)
                fts.remove(prediction)

    def save_weights(self):
        self.model.save_weights('./model/weights')
