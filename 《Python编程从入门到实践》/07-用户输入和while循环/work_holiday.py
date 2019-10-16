#coding = utf-8


msg = "\nIf you could visit one place in the world,where would you go?"

responses = {}
while True:
    place = input(msg)
    
    if place == 'no':
        break
    name = input("\nMay I have your name?")
    responses[name] = place

for key, value in responses.items():
    print(key + " is a good place for " + value)
    
