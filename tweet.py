import math

# For this Assignment, the MAX_TWEET_LENGTH is smaller than 140 so as to 
# simplify character counting and to avoid unnecessarily long strings.
MAX_TWEET_LENGTH = 60

# This ERROR_MESSAGE is to be used in the tweet_from_message function.
ERROR_MESSAGE = 'Fail: message too short'

def contains_bitly_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to a bit.ly URL of the 
    form 'http://bit.ly/'.

    Assume tweet is a valid tweet.

    >>> contains_bitly_url('Theory/AI/Philosophy Seminar- ' \
            'Jan 9:  http://bit.ly/12VuYyG')
    True
    >>> contains_bitly_url('http://bit.ly/14q3Rfz Google CS Development' \
            ' Talk: Jan 15')
    True
    >>> contains_bitly_url('Fairgrieve to play in goal http://www.nhl.com')
    False
    """
    
    return "http://bit.ly/" in tweet

# Complete this function body.


# Now define the other functions described in the handout.
def number_of_tweets_required(tweet):
    """ (str) -> int

    Return the number of tweets required to post the message.

    >>>number_of_tweets_required ("The class of CSC 108 at university of Toronto
    teaches us the language of python over the semester")
    2

    >>>number_of_tweets_required ("To test your work, you should
    call on each function with a variety of different arguments and check that
    the function returns the correct value in each case. This can be
    done in the shell or using another .py file, but must not be done in
    tweet.py.")
    5
    """

    return math.ceil(len(tweet) / MAX_TWEET_LENGTH)

def is_retweet(re_tweet, original_username):
    """ (str, str) -> bool

    Returns True or False depending on whether the tweet is in proper retweet
    format with the given username.

    >>>is_retweet("RT @MapleLeafs Fairgrieve to play in goal tonight",
    "MapleLeafs")
    True
    >>>is_retweet("@MapleLeafs Fairgrieve to play in goal tonight",
    "MapleLeafs")
    False
    >>>is_retweet("MT @Dan To test your work, you should
    call on each function with a variety of different arguments and check that
    the function returns the correct value in each case. This can be
    done in the shell or using another .py file, but must not be done in
    tweet.py, "Dan")
    False
    """
    
    if re_tweet.startswith("RT @") and re_tweet[4 : 4 + len(original_username)]\
       == original_username:
        print(True)
    elif re_tweet.startswith("MT @") and \
         re_tweet[4 : 4 + len(original_username)] == original_username and \
         len(re_tweet) <= MAX_TWEET_LENGTH :
        print(True)
    else:
        print(False)
       
def tweet_from_message(i, tweet):
    """ (int, str) -> str

    Returns the string from "tweet" with the index "i" given as "tweet" will be
    divided into strings of lenght "MAX_TWEET_LENGHT".

    >>>tweet_from_message(2, "To test your work, you should
    call on each function with a variety of different arguments and check that
    the function returns the correct value in each case. This can be
    done in the shell or using another .py file, but must not be done in
    tweet.py")
    ariety of different arguments and check that the function re

    >>>tweet_from_message(1, "To test your work, you should
    call on each function with a variety of different arguments and check that
    the function returns the correct value in each case. This can be
    done in the shell or using another .py file, but must not be done in
    tweet.py")
    To test your work, you should call on each function with a v
    """
    
    if i <= math.ceil(len(tweet)/MAX_TWEET_LENGTH):
        print(tweet [((i-1) * 60) : (i * 60)])
    else:
        print(ERROR_MESSAGE)

def format_retweet_from(tweet, username):
    """(str, str) -> str
    Takes the username and the tweet and returns the tweet as a retweet in
    either the RT or MT format depending on it's length by the username.

    >>>format_retweet_from("MapleLeafs won the game last night", "DanZingaro")
    RT @DanZingaro MapleLeafs won the game last night

    >>>format_retweet_from("To test your work, you should
    call on each function with a variety of different arguments and check that
    the function returns the correct value in each case. This can be
    done in the shell or using another .py file, but must not be done in
    tweet.py", "DanZingaro")
    MT @DanZingaro To test your work, you should...e in tweet.py
    """
    
#There are 8 characters in a retweet other than the username and tweet
#The extra characters in MT format are "MT @ ..."

#There are 5 characters in a retweet other than the username and tweet
#The extra characters in RT format are "RT @ "

    extra_chars = (len(tweet) + len(username) + 8) - MAX_TWEET_LENGTH

    if (len(tweet) + len(username) + 5 <= MAX_TWEET_LENGTH):
        print("RT @" + username + " " + tweet)

#If the tweet is valid and the username is valid yet they exceed 60 characters,
#Then the tweet has to be at least 41 chars long and at most 60 characters long.

    else:
        print("MT @" + username + " " + tweet[ : 25] + "..." + \
              tweet[ extra_chars + 25 : ])
