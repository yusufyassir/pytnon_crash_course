rivers = {
    'nile' : 'sudan',
    'amazon' : 'brazil',
    'mississipi' : 'america'
}

for river, country in rivers.items():
    print(f"the {river.title()} river runs through {country.title()}.")
print()

for river in rivers:
    print(river.title())
print()

for country in rivers.values():
    print(country.title())
