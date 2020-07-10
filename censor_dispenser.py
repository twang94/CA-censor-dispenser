# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


"""Write a function that can censor a specific word or phrase from a body of text, and then return the text.

Mr. Cloudy has asked you to use the function to censor all instances of the phrase learning 
algorithms from the first email, email_one. Mr. Cloudy doesn’t care how you censor it, he 
just wants it done.
"""
### first censor replace prompt - censoring while preserving word length (codecademy solution)
def censor_one(phrase, text):
    censor_item = ""
    for x in range(len(phrase)):
        if phrase[x] == " ":
            censor_item += " "
        else:
            censor_item += "X"
    return text.replace(phrase, censor_item)

# print(censor_one("learning algorithms", email_one))


"""
Write a function that can censor not just a specific word or phrase from a body of text, 
but a whole list of words and phrases, and then return the text.

Mr. Cloudy has asked that you censor all words and phrases from the following list in 
email_two.

proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithm", "her", "herself"]

"""

def censor_two(phraselist, text):
    output = []
    handlecase = [word.title() for word in phraselist]
    phraselist += handlecase
    # this handles censored words that contain other censored words, e.g. herself and her
    text_split = text.split(" ")
    for word in text_split:
        if word in phraselist:
            output.append("X" * len(word))
        else:
            output.append(word)
    output2 = " ".join(output)
    # handle remaining phrases + missed words
    for censor in phraselist:
        censor_item = ""
        for idx in range(len(censor)):
            if censor[idx] == " ":
                censor_item += " "
            else:
                censor_item += "X"
        output2 = output2.replace(" " + censor, " " + censor_item) #space strings handle censors in normal words
        output2 = output2.replace("\n" + censor, "\n" + censor_item)
    return output2
    
# print(censor_two(proprietary_terms, email_two))

"""The most recent email update has concerned Mr. Cloudy, but not for the reasons you might 
think. He tells you, “this is too alarmist for the Board of Investors! Let’s tone down the 
negative language and remove unnecessary instances of ‘negative words.’”

Write a function that can censor any occurance of a word from the “negative words” list 
after any “negative” word has occurred twice, as well as censoring everything from the list
 from the previous step as well and use it to censor email_three.

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", 
"alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", 
"damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", 
"horribly", "questionable"]
"""

def censor_three(phraselist, text):
    c2_split = email_three.split(" ")
    negcount = 0
    while negcount < 2: 
        for i in range(len(c2_split)):
            if c2_split[i] in phraselist:
                c2_split[i] = "****" + c2_split[i] + "****"
                negcount += 1
                break
    output = []
    for word in c2_split:
        if word in phraselist:
            output.append("X" * len(word))
        else:
            output.append(word)

    c3_text = " ".join(output) 
    
    for censor in phraselist:
        censor_item = ""
        for idx in range(len(censor)):
            if censor[idx] == " ":
                censor_item += " "
            else:
                censor_item += "X"
        for c in punctuations:
            c3_text = c3_text.replace(c + censor, c + censor_item) #space strings handle censors in normal words
            c3_text = c3_text.replace(censor + c, censor_item + c)
            c3_text = c3_text.replace(censor.title(), censor_item)
    for censor in proprietary_terms:
        censor_item = ""
        for idx in range(len(censor)):
            if censor[idx] == " ":
                censor_item += " "
            else:
                censor_item += "X"
        for c in punctuations:
            c3_text = c3_text.replace(c + censor, c + censor_item)
            c3_text = c3_text.replace(censor + c, censor_item + c)

    c3_text = c3_text.replace("****", "")
    return c3_text

punctuations = [",", ".", "(", ")", "!", " ", "\n"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
 "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", 
 "broken", "damage", "damaging", "dismal", "distressing", "distressed", 
 "concerning", "horrible", "horribly", "questionable"]
proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithm", "her", "herself"]
# print(censor_three(negative_words, email_three))

print(email_four)

combined_list = negative_words + proprietary_terms

"""
This final email has Mr. Cloudy in a frenzy. “We can’t let this information get out!” He 
tells you, “our company would be ruined! Censor it! Censor it all!”

Write a function that censors not only all of the words from the negative_words and 
proprietary_terms lists, but also censor any words in email_four that come before AND 
after a term from those two lists.
"""

# unfinished
def censor_four(phraselist, text):
    c4_split = text.split(" ")
    #for word in c4_split:
    # checking word before
    #print(output)
    #c4_text = " ".join(output)


print(censor_four(combined_list, email_four))
