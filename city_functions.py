#coding = utf-8

def city_country(city, country):
    message = city.lower().title() + "," + country.title()
    return message
    
def city_country2(city, country="china"):
    message = city.title() + "," + country.title()
    return message

def city_country3(city, country, population = "50w"):
    message = city.title() + "," + country.title() +  " - population " + population
    return message
    
