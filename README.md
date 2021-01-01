# DeepLearningTikTok
A tutorial for journalists to build deep learning models in order to monitor trends on TikTok

## Summary

TikTok has become a rising app and an important information source for journalists. Protests are organized on the platform--in June teens and K-Pop stans trended as they falsely registered for a Trump rally to artificially sell out the event. Live protest footage has also been recorded and shared on the app. In addition to political activity, the app has also been used by QAnon to spread conspiracy theories. When a conspiracy theory that Wayfair was selling children started to trend, Wayfair stock prices started to drop.

However despite the importance of the app, it’s notoriously hard to monitor. Unlike twitter and facebook, it’s primary media are videos. Though there are hashtags associated with each video, oftentime they are only loosely related to the topic of the video. In fact, many people add trending hashtags regardless of whether or not they relate to their video in the hopes of making it someone’s For You Page, essentially a user’s home feed of TikTok.

As such, I have created a tutorial for training a deep learning model to recognize a specific face on the app. (The face I have chosen is President Trump, however any face can be used. In fact, any image can be used. For example if you wanted to train the model to recognize confederate flags on the app, you can just swap the training data for images of confederate flags). This model is then used by a separate python script that will call a tiktok scraping api, and which can be run in the background of any computer, monitoring for potential appearances of Trump on the app. This will allow journalists to be alerted every time the president is trending on the app.

### TikTok scraper
TikTok does not currently have an accessible api, and so an open-source scraper was used for this project. I choose to use tiktok-scraper by github user drawrowfly, but you are welcome to use any of the tiktok scrapers available to you, you only need to adjust that part in the shell script accordingly.
Tiktok scraper used for project: https://github.com/drawrowfly/tiktok-scraper

### "DeepLearning_Model_Tiktok.ipynb"
The model is created using a colab notebook. The jupyter notebook version of that has been uploaded to this repo under this file. To create the model, you should upload the notebook into google colab (which is free) and run the cells. This is because you will have access to free gpus, which will make the training much faster. This notebook will then output an h5 file of the finished, trained model which you will then download onto your local. The jupyter notebook contains text to walk you through training the model, and there are four general steps.

Labeling the data: For this project, our data are images that are captured from TikTok videos. I chose to hand label all data instead of pulling a repository of images of President Trump. This is because deep learning networks are very sensitive to features in the images, and because I was looking at creating a model for TikTok, I only wanted to train the model on TikTok specific images. (For example most of the time Trump appears on TikTok it is a recording of a television or computer screen, since rarely are people on TikTok posting first-hand accounts of seeing Trump). As such the label process is the most time consuming process in creating this model. I labeled 505 images for this project by hand, and then supplemented them by using data augmentation (detailed in the jupyter notebook). If you would like to sub a different image for the model to recognize besides Trump, simply replace this step with images of the desired feature you wish to recognize and label accordingly. 

Running the images through a base model: In this project, I choose to run the images first through the VGG16 base model. VGG16 is a pre-trained model that takes in (224,224) RGB images and converts them into features. It comes out-of-the-box from the keras library and has been trained on millions of images from ImageNet. To read more about VGG16 model check out this site: https://neurohive.io/en/popular-networks/vgg16/

Training the model: We then create a sequential model with multiple Dense layers and dropout layers (to prevent overfitting). Using our data-augmented images, we train this sequential model on 50 epochs. For this step, you only need to ensure that the input layer and output layer remain consistent as described in the notebook--the rest of the model you can customize as you see fit. 

Saving the model: We then save the model as an h5 file and download it to our local. You should then move the model to the same directory as this github repo. When you run your shell script, it will call the model and expect it to be in the same parallel directory.







### Acknowledgments
This project was based on this online tutorial: https://www.analyticsvidhya.com/blog/2018/09/deep-learning-video-classification-python/
Thank you to the author Pulkit Sharma for their work!
