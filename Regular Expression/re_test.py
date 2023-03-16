import re
generated_text =[ "1. The Ultimate Guide to Health and Beauty: This guide provides a comprehensive overview of the different health and beauty topics that can help you look and feel your best. It covers everything from nutrition, exercise, skincare, hair care, makeup, mental health, and more. You'll learn how to nourish your body for optimal health and beauty, how to create a wellness routine that works for you, and how to find balance in all areas of life. ",
             "2. Uncovering the Secrets to Looking and Feeling Your Best: In this section of the guide, we dive deeper into specific topics such as dieting tips for healthy weight loss or gain; ways to build muscle strength; simple steps for improving skin health; hair care techniques for long-lasting results; makeup application tips for a flawless finish; stress relief methods for better mental wellbeing; and more. You will discover what it takes to look and feel your absolute best each day. ",
           "Summary: The Ultimate Guide to Health and Beauty provides a comprehensive overview of topics related to physical health and beauty while Uncovering the Secrets to Looking and Feeling Your Best dives deeper into specific areas such as dieting tips, muscle building strategies, skincare techniques, hair care advice, makeup application tips, stress relief methods and more."]

#punctuations=r'''()-[]「」{};':'"\<>./@#$%^&*_~'''
punctuations = r'''\.．、：）- <>./@#$%^&*_~「」【】'''

#remove punctuation, start-char and numbers
def remove(str_list):
    pattern = '^[0-9]|[0-9]+'
    str_list = [re.sub(pattern, '', i) for i in str_list]
    str_list = [re.sub('^[!|-|?|.]','',i) for i in str_list]
    str_list = [re.sub('\n','',i) for i in str_list]
    str_list = [re.sub(r'\s+', ' ', i).strip() for i in str_list] # cleaning whitespace
    return str_list

#remove punctuation
def remove_punctuation(str_list):
    result = []
    
    for line in str_list:
        for x in line:
            if x in punctuations: 
                line = line.replace(x, "")
        result.append(line)
    return result

#remove 【1】
def remove_special_char(str_list):
    
    result = []
    for line in str_list:
        r = ''
        for i in line:
            if i.isalnum():
                r += i
        result.append(r)
    return result

#remove ❶, １ and etc.
def remove_emoji(str_list):
    emoji_pattern = re.compile("["
                           u"\u24FF-\u277E"  
                           u"\uFF10-\uFF19"  
                           u"\u2460-\u2468"  
                           "]+", flags=re.UNICODE)
    emoji_pattern = [re.sub(emoji_pattern, '', i) for i in str_list]
    return emoji_pattern

punc_1 = r'^[^:-]*[^\s+]*'
def remove_duplicate(str_list):
    for line in str_list:
        i = re.sub(punc_1, '', line)
        result.append(i)
    return result

result = remove_punctuation(generated_text)
#result = remove_special_char(result)
result = remove_emoji(result)
result = remove(result)
result = remove_duplicate(result)
print(result)