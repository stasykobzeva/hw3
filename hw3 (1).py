items = {
    'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
    'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
    'sausage':{'na5me': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
} 

price_less_20 = { c: items[c]["count"] < 20 for c in items } 
print(price_less_20 )