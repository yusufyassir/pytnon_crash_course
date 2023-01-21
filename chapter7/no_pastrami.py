sandwich_orders = ['pastrami', 'grilled chees', 'pastrami', 'steak', 'burger', 'hotdog', 'pastrami']
print("the deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwaich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich.title()} sandwich is ready")
    finished_sandwaich.append(sandwich)
print(finished_sandwaich)