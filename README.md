# Computer-Vision-Emotion-Detection


Abstract:

This project focuses on developing an emotion recognition system capable of accurately identifying and classifying emotions from facial expressions. Utilizing computer vision and deep learning, the system analyzes facial features and categorizes them into predefined emotions such as happiness, sadness, anger, and surprise. The dataset, which was custom-built for this project, includes approximately 500+ labeled video clips, stored in the /collected_emotions/ folder, totaling around 3 GB. The model architecture, which incorporates several convolutional layers followed by dense layers, was constructed and trained using TensorFlow and Keras. The training process yielded a training accuracy of 95.2% and a validation accuracy of 91.9%, indicating strong performance in emotion classification. Once trained, this system can be used to detect and recognize emotions in real-time video feeds, making it useful for applications such as human-computer interaction, mental health assessment, and more.


Training Data: 

The data can be found in the /collected_data/ folder or accessed on Kaggle here.
Since there was no suitable pre-existing dataset for emotion detection, I compiled my own. I gathered 500+ video clips of people demonstrating various emotions, each labeled manually. In total, this dataset amounts to approximately 3 gigabytes.

OpenCV Data Collection Script: 

1. Use openCV face detection 





