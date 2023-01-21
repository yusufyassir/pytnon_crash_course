sandwich_orders = ['grilled chees', 'steak', 'burger', 'hotdog', 'gyro']
finished_sandwaich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich.title()} sandwich is ready")
    finished_sandwaich.append(sandwich)
print(finished_sandwaich)