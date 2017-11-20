# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from settings import TWITTER
import logging
import tweepy
from time import sleep
from chatterbot.response_selection import get_most_frequent_response
from creds import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)
chatbot = ChatBot(
    "TwitterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./twitter-database.db",
    twitter_consumer_key=TWITTER["CONSUMER_KEY"],
    twitter_consumer_secret=TWITTER["CONSUMER_SECRET"],
    twitter_access_token_key=TWITTER["ACCESS_TOKEN"],
    twitter_access_token_secret=TWITTER["ACCESS_TOKEN_SECRET"],
    trainer="chatterbot.trainers.TwitterTrainer"
	
)


chatbot.train()


chatbot.logger.info('Trained database generated successfully!')
print("Ready")
response = chatbot.get_response('What is wrong with humans?')
api.update_status(response)
print(response)





