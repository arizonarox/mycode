#!/usr/bin/python3

movies= [{"scifi":{"best":"matrix","worst":"matrix reloaded"}},{"comedy":{"best":"spaceballs","worst":"click"}},{"horror":{"best":"conjuring","worst":"idk"}},]

# 1. Prompt user for scifi, comedy, or horror
print("Choose a genre: scifi, comedy, or horror")
genre = input(">")
index = -1
while index == -1:
    if genre == "scifi":
        index = 0
    elif genre == "comedy":
        index = 1
    elif genre == "horror":
        index = 2
    else:
        print("choose a genra: scifi, comedy, or horror")
        genre = input(">")
        
# 2. Prompt user for best or worst
print("Do you want best or worst movie?")
choice = input(">")
while choice == True:
    if choice == "best" or choice == "worst":
        break
    else:
        print("Do you want best or worst movie?")
        choice = input(">")

### Teachers solution
for i in movies:
    if genre in i.keys():
        print(f"The {choice} of {genre} film is: {i[genre][choice].capitalize()}")



# 3. Print the output of the users choices


#print(f"This is the {choice} of {genre} : {movies[index][genre][choice]}")
# 4. Make movie capitalized when returned
#answer = movies[index][genre][choice]
#print(f"This is the {choice} of {genre} : {answer}.title")

