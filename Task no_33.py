# Given a list of words, concatenate them into a single string separated by spaces

def concatenate_word(list_word):
    concatenate_string=' '.join(list_word)
    return concatenate_string



list_word=["Hello","How","are","You","Doing?"]

result=concatenate_word(list_word)

print(result)