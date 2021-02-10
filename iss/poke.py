#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget
def main():

    chocie = input("What pokemon?").lower().strip()

    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/"+choice).json()
    
    #print(pokeapi)
    image_url=pokeapi["sprites"]["front_default"]
    print(image_url)
    image = wget.download(image_url)
    print(image)
    count = 0
    for i in pokeapi["game_indices"]:
        count = count+1
    #print("# of Games:", len(pokeapi["game_indices"]))cl
    print(count)
    for i in pokeapi["moves"]:
        print(i["move"]["name"])
main()
