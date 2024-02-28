#define unwanted punctuation marks
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#remove punctuation
def strip_punctuation(str1):
    for char in punctuation_chars:
        str1 = str1.replace(char, '')
    return str1


# obtain list of positive words to use
positive_words = []

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#count positive words in string
def get_pos(str1):
    str1 = strip_punctuation(str1)
    num_pos_words = 0
    for word in str1.split(' '):
        if word.lower() in positive_words:
            num_pos_words += 1
    return num_pos_words

# obtain list of negative words to use
negative_words = []

with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#count negative words in string
def get_neg(str1):
    str1 = strip_punctuation(str1)
    num_neg_words = 0
    for word in str1.split(' '):
        if word.lower() in negative_words:
            num_neg_words += 1
    return num_neg_words

#access data file; create output file with header row
twitter_data = open('project_twitter_data.csv', 'r')
outfile = open('resulting_data.csv', 'w')

header = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score'
cntrlE = '\n'

outfile.write(header)
outfile.write(cntrlE)

#append results for each line of data file to output file
lst_lines = []
for lin in twitter_data.readlines()[1:]:
    lst_lines.append(tuple(lin.split(',')))
for tweet_text, retweet_count, reply_count in lst_lines:
    numberRetweets = retweet_count
    numberReplies = reply_count.replace('\n', '')
    positiveScore = get_pos(tweet_text)
    negativeScore = get_neg(tweet_text)
    netScore = positiveScore - negativeScore
    
    outfile.write('{},{},{},{},{}'.format(numberRetweets, numberReplies, positiveScore, negativeScore, netScore))
    outfile.write(cntrlE)

twitter_data.close()
outfile.close()
