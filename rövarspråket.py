__author__ = 'Erik Andersson'


def rovarspraket(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    new_str = ""
    for c in str:
        if c.lower() in consonants:
            if c.islower():
                new_str += c + 'o' + c
            else:
                new_str += c + 'O' + c
        else:
            new_str += c
    return new_str

print(
    rovarspraket(input("Enter a phrase to turn into the Robber's language:\n")))
