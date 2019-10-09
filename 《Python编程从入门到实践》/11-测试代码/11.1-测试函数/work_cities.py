#coding = utf-8


def city_contry(city, contry):
    cityMsg = city + ',' + contry
    return cityMsg.title()
   
  
def city_contry_population1(city, contry, population):
    cityMsg = city + ',' + contry + ' - population ' + str(population)
    return cityMsg.title()
    
    

def city_contry_population2(city, contry, population=0):
    """Population有默认值，如果不填数据的话，则数据是空的"""
    if population !=0 :
        cityMsg = city + ',' + contry + ' - population ' + str(population)
       
    else:
        cityMsg = city + ',' + contry + ' - population No Data'
                
    return cityMsg.title()
