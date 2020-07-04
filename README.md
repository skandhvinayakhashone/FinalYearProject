# FinalYearProject

Under Graduate Final Year Project : Advertisement recommendation engine analysis using content-based system.
Comparing and studying the performance of recommendation engines using different datasets to recommend advertisements.
The engine uses the following types of datasets to implement combinations of the same while recommending advertisements:

1. Objects in video.

2. Audio in Video.

3. Texts seen in video.

4. Description of the video.

Dependencies:


ffmpy >= 0.2.0

NLTK >= 3.4.0

numpy >= 1.18.0

opencv >= 3.4.8

pandas >= 0.25.0

pillow >= 5.4.0

pyenchant >= 3.0.0

pytesseract >= 0.3.0

pytorch >= 1.0.2

pytube >= 9.5.0

scikit-learn >= 0.22

wand >= 0.5.7

YOLO weights @ https://pjreddie.com/media/files/yolov3.weights

Instructions for use:

1. Download a playlist of youtube videos using youtube_downloader.py

2. Extract objects, texts, audio, descrtiptions using the respective extraction programs in the repo. 

3. Create different combinations of the same.

4. Use frontend.py to get recommendations for test videos.


