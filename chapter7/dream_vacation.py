dream_vacation = {}
#set flag to idicate polling is active
polling_active = True
while polling_active:
    name = input("\n What is your name? ")
    location = input(" Where would your dream vavciton be? ")
    dream_vacation[name] = location

    add = input("\nDo you want to poll someone else (yes/no) ? ")
    if add == 'no':
        polling_active = False
#after polling print data aquired
print ("\n----reulsts----")
for name, location in dream_vacation.items():
    print(f"{name.title()}, would like to go to {location.title()}.")