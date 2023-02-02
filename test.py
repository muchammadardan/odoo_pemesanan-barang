import math
import json

products = [
    {
        'nama': 'Aqua Cool Gel For Only Skin 100ml',
        'R': 150,
        'S': 25000,
        'C': 0.5,
        'H': 1000,
        'WD': 25,
        'L': 3,
        'UD': 2,
    }
]

# EOQ, TOC, TCC, TC, F*, T, Exp, SS, ROP
for product in products:
    product['EOQ'] = round(math.sqrt(
        (2 * product['R'] * product['S']) / (2000 * product['C'])))
    product['TOC'] = round((product['R'] / product['EOQ']) * product['S'])
    product['TCC'] = round((product['EOQ'] / 2) * product['H'])
    product['TC'] = round(product['TOC'] + product['TCC'])
    product['F'] = round(product['R'] / product['EOQ'], 2)
    product['T'] = round(product['EOQ'] / product['R'])
    product['EXP'] = round(product['WD'] / product['F'])
    product['SS'] = round(product['UD'] * product['R'] / product['WD'])
    product['ROP'] = round((product['L'] * product['R'] /
                            product['WD']) + product['SS'])

print(json.dumps(products))
