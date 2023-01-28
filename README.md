# ProCity-Tweet-Bot
ProCity Updates is a Twitter Bot designed to tweet out a graphic for the top 10 on tarik’s 10 man custom lobbies via discord.
<br><br>
<center>
<img src = "images\sampletweet.png">
</center>
<br>

# Contents
1. Usage
2. Development
    - Web Scrapping
    - Table Generation
    - Tweepy
3. See it in action
# Usage
<pre><code>1. git clone https://github.com/niyarrbarman/procity-twt-bot.git 
2. pip3 install -r requirements.txt
3. python3 bot.py</code></pre> 
# Development
 ## Web Scraping
 Web scraping is the process of using bots to extract content and data from a website. There was no initial content for data extraction. So the easiest path is to check the XHR calls in the network tab in devTools and look for some content in each request.<br><br>
 We used [Insomnia](https://insomnia.rest/) to automate this process.<br>

 ![insomnia dashboard](images\insomnia.png)
 ## Table Generation
 We cleaned the JSON file we received from Insomnia and then using <code>pandas</code> library we created the 'Top 10' table. We used <code>pandas.style</code> for the graphic. 
 ## Tweepy
 We created a twitter developer account and generated access codes for our account. We then used <code>tweepy</code> to post the tweets. 
 # See it in action
 [Click here](https://twitter.com/ProCityUpdates) to view our bot.



