Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

Geeks.pop('bag')
Geeks['address'] = 'Улица Ибраимова, 103'
Geeks['phone_number'] = 996555555555
Geeks['instagram'] = 'geeks_edu'
Geeks['courses'].append('UX/UI')
Geeks['courses'] = set(Geeks['courses'])
Geeks['founding_date'] = '2018'
courses_in_geeks = len(Geeks['courses'])
print(f'Каличество кусов: {courses_in_geeks}')

for key, value in Geeks.items():
    print(f'{key}: {value}')
