#!/usr/bin/python3

movies= {

"scifi":{"best":"matrix","worst":"matrix reloaded"},
"comedy":{"best":"spaceballs","worst":"click"},
"horror":{"best":"conjuring","worst":"idk"},
}

print(type(movies))
print(movies)
print(movies["scifi"]["worst"])
print(movies["horror"]["best"])

print("Choose a genera: scifi, comedy, or horror")
genre = input(">")

print("Do you want the best or the wrost?")
choice = input(">")

print("This is the " + choice + " of " + genre + ": " + movies[genre][choice])

# F Strings - we like these
print(f"This is the {choice} of {genre} : {movies[genre][choice]}")


