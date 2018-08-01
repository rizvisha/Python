import builtins

# Check for use of functions print and input.

our_print = print

def disable_print(*args):
    raise Exception("You must not call print anywhere in your code!")

def disable_input(*args):
    raise Exception("You must not call input anywhere in your code!")

builtins.print = disable_print
builtins.input = disable_input

import tweet

# Get the initial value of the constants
constant_1_before = [60]
constant_2_before = ['Fail: message too short']

# Type check tweet.contains_bitly_url
result = tweet.contains_bitly_url('Test 123')
assert isinstance(result, bool), \
       '''tweet.contains_bitly_url should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.number_of_tweets_required
result = tweet.number_of_tweets_required('Test 123')
assert isinstance(result, int), \
       '''tweet.number_of_tweets_required should return an int, but returned {0}
       .'''.format(type(result))

# Type check tweet.is_retweet
result = tweet.is_retweet('Test 123', '456')
assert isinstance(result, bool), \
       '''tweet.is_retweet should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.tweet_from_message
result = tweet.tweet_from_message(1, 'Test 123')
assert isinstance(result, str), \
       '''tweet.tweet_from_message should return a str, but returned {0}
       .'''.format(type(result))

# Type check tweet.format_retweet_from
result = tweet.format_retweet_from('Test 123', '456')
assert isinstance(result, str), \
       '''tweet.format_retweet_from should return a str, but returned {0}
       .'''.format(type(result))


# Get the final values of the constants
constant_1_after = [tweet.MAX_TWEET_LENGTH]
constant_2_after = [tweet.ERROR_MESSAGE]

# Check whether the constants are unchanged.
assert constant_1_before == constant_1_after, \
       '''Your function(s) modified the value of constant MAX_TWEET_LENGTH
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    
assert constant_2_before == constant_2_after, \
       '''Your function(s) modified the value of constant ERROR_MESSAGE
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    

our_print("""

The type checker passed.

This means that the functions in tweet.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")

