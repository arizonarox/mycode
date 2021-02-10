#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

yuck= ["celery","carrots"]

for dic in farms:
    print(dic["agriculture"])

choice = input("Pick a farm: NE Farm, W Farm, or SE Farm")

print(choice)

for dic in farms:
    if dic["name"] == choice:
        for crop in dic["agriculture"]:
            if crop not in yuck:
                print(crop)
    #else:
     #   print("dang")








