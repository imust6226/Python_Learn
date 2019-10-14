#coding = utf-8

def car_info(maker, type_m, **fields):
    """定义一个空的字典，用来存储所有的信息"""
    car = {}

    car['maker'] = maker
    car['type'] = type_m
    for key, value in fields.items():
        car[key] = value
    return car

car1 = car_info('subaru', 'outback', color = 'red', tow_package = True)
print(car1)


