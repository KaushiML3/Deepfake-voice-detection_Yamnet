# Deepfake-voice_detection_Yamnet
This repository contains a machine learning-based system to detect deepfake (synthetic) voices. The system utilizes audio feature extraction techniques such as YAMNet and deep learning models (ANN, CNN, RNN) to differentiate between real and fake audio.

# 🚀 Features
- Audio Preprocessing: Converts raw audio into meaningful features.
- Feature Extraction: Uses YAMNet to extract embeddings from audio signals.
- Dataset : Uses the kaggle "In The Wild (audio Deepfake)" dataset for training the model.[Link](https://www.kaggle.com/datasets/abdallamohamed312/in-the-wild-audio-deepfake)
- Deep Learning Models: Implements ANN, CNN, and RNN architectures for classification.
- Training & Evaluation: Trains models with labeled datasets and evaluates accuracy.
- Inference API: Provides an API to classify input audio as real or deepfake.
    1. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/Screenshot%20(97).png)
    2. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/Screenshot%20(98).png)

# Model Performance

1. ANN model atchitecture
- Model training stat: Accuracy and Val_lose
    1. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/ann%20s.png)
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score
    2. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/ann%20c.png)
  
                        precision    recall  f1-score   support
                fake       0.97      0.95      0.96       446
                real       0.96      0.98      0.97       554

            accuracy                           0.97      1000
           macro avg       0.97      0.97      0.97      1000
        weighted avg       0.97      0.97      0.97      1000


2. CNN model atchitecture
- Model training stat: Accuracy and Val_lose
    1. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/cnn%20s.png)
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score
    2. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/cnn%20c.png)
  
                        precision    recall  f1-score   support
                fake       0.97      0.96      0.97       446
                real       0.97      0.97      0.97       554

            accuracy                           0.97      1000
           macro avg       0.97      0.97      0.97      1000
        weighted avg       0.97      0.97      0.97      1000


3. RNN model atchitecture
- Model training stat: Accuracy and Val_lose
    1. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/rnn%20s.png)
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score
    2. ![image](https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet/blob/main/src_img/rnn%20c.png)
  
                        precision    recall  f1-score   support
                fake       0.94      0.93      0.94       446
                real       0.94      0.95      0.95       554

            accuracy                           0.94      1000
           macro avg       0.94      0.94      0.94      1000
        weighted avg       0.94      0.94      0.94      1000

Best Model Achieved: ANN with 97% accuracy


# 🛠️ Setup & Installation

1.Clone the repository:
```python
git clone https://github.com/KaushiML3/Deepfake-voice-detection_Yamnet.git
cd Deepfake-voice-detection_Yamnet
```

2.Install dependencies:
```python
pip install -r requirements.txt

```

3.Run inference
- change the direction for API folder
```python
python main.py

```
