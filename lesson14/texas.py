from random import choice

# This is a custom module :)
capital = "Austin"

bird = "Northern Mockingbird"

flower = "Bluebonnet"

song = "Texas, Our Texas"


def randomfunfact():
    funfacts = [
        "Almost every type of biome on Earth is present in Texas.",
        "Texas is the 2nd most populated state in the US.",
        "Texas was the last state to free its slaves following the American Civil War.",
        "Texans tend to love Texas. Too much, sometimes.",
    ]

    index = choice("0123")

    print(funfacts[int(index)])


# Important to have to following in order to
# call something inside the module
# Otherwise it will run everytime the current file is run,
# even if not called
if __name__ == "__main__":
    randomfunfact()
