#Q1-Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
import re
email = ' zuke26@facebook.com'
email1='page33@google.com'
email2='jeff42@amazon.com'
print(re.findall(r'(.+)@(.+)\.(.+)',email),end=" ")
print(re.findall(r'(.+)@(.+)\.(.+)',email1),end=" ")
print(re.findall(r'(.+)@(.+)\.(.+)',email2))
#methode 2 print in a single list
import re
email = ' zuke26@facebook.com jeff42@amazon.com page33@google.com '

print(re.findall(r'(.+)@(.+)\.(.+) (.+)@(.+)\.(.+) (.+)@(.+)\.(.+)',email))



#Q2-Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"\b[Bb]\w+")
result=p.findall(text)
print(result)

#Q3-Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence
import re
s="A, very very; irregular_sentence"
result=re.sub(r'[^A-Za-z0-9]', ' ', s)

print(result)


#Q4-Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
#             tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
#           desired_output = 'Good advice What I would do differently if I was learning to code today'
#
import re
tweet ='''Good advice! RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt'''

def clean_tweet(tweet):
    tweet=re.sub('http\S+\s*',' ',tweet) 
    tweet=re.sub('RT|cc',' ',tweet)
    tweet=re.sub('#\S+',' ',tweet)
    tweet=re.sub('@\S+',' ',tweet)
    tweet=re.sub('[%s]'% re.escape("""!"#$%&'( )*+,-./:;<=>?@[\]^_ `{|}~"""),' ',tweet)
    #tweet=re.sub('\s+',' ',tweet)
    return tweet
print(clean_tweet (tweet))