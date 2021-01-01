# DeepLearningTikTok
A tutorial for journalists to build deep learning models in order to monitor trends on TikTok

## Summary

TikTok has become a rising app and an important information source for journalists. Protests are organized on the platform--in June teens and K-Pop stans trended as they falsely registered for a Trump rally to artificially sell out the event. Live protest footage has also been recorded and shared on the app. In addition to political activity, the app has also been used by QAnon to spread conspiracy theories. When a conspiracy theory that Wayfair was selling children started to trend, Wayfair stock prices started to drop.

However despite the importance of the app, it’s notoriously hard to monitor. Unlike twitter and facebook, it’s primary media are videos. Though there are hashtags associated with each video, oftentime they are only loosely related to the topic of the video. In fact, many people add trending hashtags regardless of whether or not they relate to their video in the hopes of making it someone’s For You Page, essentially a user’s home feed of TikTok.

As such, I have created a tutorial for training a deep learning model to recognize a specific face on the app. (The face I have chosen is President Trump, however any face can be used. In fact, any image can be used. For example if you wanted to train the model to recognize confederate flags on the app, you can just swap the training data for images of confederate flags). This model is then used by a separate python script that will call a tiktok scraping api, and which can be run in the background of any computer, monitoring for potential appearances of Trump on the app. This will allow journalists to be alerted every time the president is trending on the app.

### TikTok scraper
TikTok does not currently have an accessible api, and so an open-source scraper was used for this project. I choose to use tiktok-scraper by github user drawrowfly, but you are welcome to use any of the tiktok scrapers available to you, you only need to adjust that part in the shell script accordingly.
Tiktok scraper used for project: https://github.com/drawrowfly/tiktok-scraper
