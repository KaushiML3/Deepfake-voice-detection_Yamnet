import numpy as np
import pandas as pd
import librosa
import os

import tensorflow as tf
import tensorflow_hub as hub

# Reload the model
current_direction = os.path.dirname(os.path.abspath(__file__))
deepfake_model = tf.saved_model.load(os.path.join(current_direction,"artifact/ann_human_or_bot"))


def load_wav_16k_mono(filename):
    try:
      
      """ Load a WAV file, convert it to a float tensor, resample to 16 kHz single-channel audio. """
      sound_sample,sr=librosa.load(filename ,sr=16000)
      return sound_sample
    
    except Exception as e:
      print("load_wav_16k_mono")
      return None

    

def infa_deepfake(audio_path):
  try:
      testing_wav_data = load_wav_16k_mono(audio_path)

      # Reload the model
      #reloaded_model = tf.saved_model.load(model_path)

      # If it's a saved model, access the signature
      infer = deepfake_model.signatures['serving_default']

      # Now use the model for prediction, passing in the necessary inputs (e.g., audio data)
      # Make sure 'testing_wav_data' is prepared in the required shape/format
      input_tensor = tf.convert_to_tensor(testing_wav_data, dtype=tf.float32)

      # Get the prediction output
      output = infer(input_tensor)
      predictions = output['output_0']  # Adjust 'output_0' based on your model's output signature

      #print(predictions)
      my_classes=['FAKE', 'REAL']

      human_bot = my_classes[tf.math.argmax(predictions)]
      #print(f'The main sound is: {human_bot}')
      status=1
      return status,human_bot


  except Exception as e:
      print("infa")
      status=0
      return status,e