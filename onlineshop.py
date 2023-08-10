goods = [
    {
    'name': 'Iphone 14',
    'brand': 'Apple',
    'price': 1200,
    
    },

    {
    'name': 'Samsung Galaxy A23',
    'brand': 'Samaung',
    'price': 600,
    
    },
    
    {
    'name': 'Xiaomi Mi13 Ultra',
    'brand': 'Xiaomi',
    'price': 800,
    
    },
    {
    'name': 'Iphone 11',
    'brand': 'Apple',
    'price': 500,
    
    },
    
       
]

#def item_price(item):
    #return item['price']

#print(sorted(goods, key=item_price))

#print(sorted(goods, key=lambda item: item['price']))

apple_list = filter(lambda item: item['brand']=='Apple', goods)
print(list(apple_list))