# video-and-speech

Task 1 Counting Butterfly

Approach: transfer learning with pre-trained model 

1. Capture video from youtube: install youtube-dl and download in avi format for backup
2. Load video to Python: install opencv-python and read video by cv2.VideoCapture
3. Preprocess video as sequence of frames for ResNet50
4. Transfer learning: using YOLO object detector with ResNet50 image classifier (removed output layer) as features (https://pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/), continue training using butterfly dataset from Kaggle (https://www.kaggle.com/datasets/veeralakrishna/butterfly-dataset?resource=download)
5. Use rolling prediction averaging to reduce “flickering” in results (https://pyimagesearch.com/2019/07/15/video-classification-with-keras-and-deep-learning/)
6. Show counts of butterflies on each image frame
7. Fly in or out indication: whenever the count is different from previous frame, check location of missing/ new object. Split image into 9 parts and highlight the part of edge(s) where the object boundary crosses the edge(s) in the previous and the next 10 image frames.

Task 2 Pa Ta Ka

Approach: Speech-to-text; count and add indication; Text-to-speech

1. Speech-to-text: install speech_recognition, test engine/APIs and tune parameters
2. Count substring in string and add count to end of text
3. Text-to-speech: install gTTS 
