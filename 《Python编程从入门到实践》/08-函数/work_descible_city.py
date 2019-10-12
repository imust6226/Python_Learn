#coding = utf-8

class DescCity():

    def __init__(self):
        pass

    def city_country(self, city, contry):
        msg = city.title() + "," + contry.title()
        return msg

dseccity = DescCity()
print(dseccity.city_country('santiago', 'chile'))

