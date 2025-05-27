noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
if len(noun) >= 5 or len(verb) >=5 or len(adjective) >=5:
  story = ("One day, a "+ adjective +" "+ noun + " decided to "+ verb + " through the forest. "
        "Everyone who saw it was amazed, because it’s not every day you see a "+ adjective +" "+ noun + " trying to "+ verb + " like that. "
        "By the end of the day, the "+ noun +" had become a legend in the village!") 
else:
  story = ("Once upon a time, a "+ adjective + " " + noun + " decided to "+ verb + " across the quiet village. Everyone watched in awe as it disappeared into the mist.")
print(story)