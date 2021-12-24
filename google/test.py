
# count_letters

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower(): ## change all letters to lower to be able deal with all possibilty
    # Check if the letter needs to be counted or not
    if letter.isalpha():      ## we should exclude any thing rather than alpha
                              ## we have to options,1- first appear , 2- repeated
      if letter not in result:## first time
        result[letter] = 1    ## add to dict as k and v, letter:1
        # Add or increment the value in the dictionary
      else:                   ## 2- how adjust counting(value) for certain key
        result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}