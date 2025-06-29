import sys
import os
import tensorflow as tf
import torch

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from layer2.federated_trainer import SimpleModel

def convert_model():
    # Load the PyTorch model
    model = SimpleModel()
    # Convert to TensorFlow (simplified, assumes compatible architecture)
    tf_model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(1, input_dim=1)
    ])
    # Dummy training to set weights (replace with actual conversion logic)
    tf_model.set_weights([torch.tensor([[0.1]]).numpy(), torch.tensor([0.05]).numpy()])
    # Convert to TensorFlow Lite
    converter = tf.lite.TFLiteConverter.from_keras_model(tf_model)
    tflite_model = converter.convert()
    with open('zabe_model.tflite', 'wb') as f:
        f.write(tflite_model)
    print("Converted model saved as zabee_model.tflite")

if __name__ == "__main__":
    convert_model()