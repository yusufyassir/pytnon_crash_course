def make_car(manu, model, **car_info):
    """get cars info in a dictionary"""
    car_info['manufacturer'] = manu
    car_info['model'] = model
    return car_info

car = make_car('toyota', 'hilux',
               color = 'white',
               tow_package = True)

print(car)