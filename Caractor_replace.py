# Don't use this Fuck word in my program
# Print to >> uc to ** or UC to @@

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "uc":
            if letter.isupper():
                translation = translation + "*"  # add fuck to f**k
            else:
                translation = translation + "@"  # add FUCK to F@@K
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter Word :")))


