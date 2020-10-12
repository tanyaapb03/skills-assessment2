"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string."""


    # split the words in phrase by spaces 
    #create a variable counter- to count number of times string is repeated 
    # blank dictionary 
    # for loop to iterte through splitted_phrase
    # add value in loop to dictionary as key and counter as value

    sentence= phrase.split(" ")
    words={}
    for word in sentence:
       if word in words:
           words[word]=words[word]+1
            
       else:
           words[word]=1
    return words








    # This function should take a single string and return a dictionary
    # that has all of the distinct words as keys and the number of
    # times that word appears in the string as values.

    # For example::

    #     >>> print_dict(count_words("each word appears once"))
    #     {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    # Words that appear more than once should be counted each time::

    #     >>> print_dict(count_words("rose is a rose is a rose"))
    #     {'a': 2, 'is': 2, 'rose': 3}

    # It's fine to consider punctuation part of a word (e.g., a comma
    # at the end of a word can be counted as part of that word) and
    # to consider differently-capitalized words as different::

    #     >>> print_dict(count_words("Porcupine see, porcupine do."))
    #     {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
   

    


def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order."""

    melon={"Honeydew" :2.50 ,"Cantaloupe":2.50,"Watermelon":2.95,"Musk":3.25,"Crenshaw":3.25,"Christmas":14.25}
    
    individual_melon=[]
    
    for key,value in melon.items():
        if value == price:
            individual_melon.append(key)
    
    if len(individual_melon) == 0:
        print ("none found")
    else:
        print (individual_melon)   
       
    
print_melon_at_price(7)







   



def translate_to_pirate_talk(phrase):
    
    
    
    dict_translation = {"sir":"matey", "hotel": "fleabag inn","student": "swabbie" ,"man": "matey","professor": "foul blaggart","restaurant": "galley"
    ,"your":"yer","excuse":"arr","students":"swabbies","are":"be","restroom":"head","my":"me","is":"be"}
    
   
    words=phrase.split(" ")
    new_sentence=[]
   
    for word in words:
        if word in dict_translation.keys():
            new_sentence.append(dict_translation[word])
        else:
            new_sentence.append(word)
    
    final_sentence=" ".join(new_sentence)
   
    return final_sentence
    
    
    



# translate_to_pirate_talk(" i dont care of who ")



"""Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """








   


def kids_game(names):
#create a blank dictionary
#run a for loop in list and put the words first letter a s key in dictionary and word as value in it 
#
    name=names.split(" ")
    game={}
    output_list=[]
    for word in name:
        game[word[0]]=word

        if word[len(word)-1] == game.keys():

            output_list.append(game[word[0]])

        return output_list



"""Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # return []
