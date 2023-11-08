price = float
percent = float


def apply_vat(price, percent):
    new_price = None
    new_percent = None

    if isinstance(price, str):
        return (f'Price ({price}) is not a number')
    elif isinstance(percent, str):
        return (f'Percent ({percent}) is not a number')
    elif price < 0:
        return (f'Price ({price}) is negative')
    elif percent < 0:
        return (f'Percent ({percent}) is negative')
    elif percent > 100:
        return (f'Percent ({percent}) is superior to 100%')
    elif 0 <= percent <= 100 and price >= 0 :
        new_percent = 1 + percent / 100
        new_price = price * new_percent
        return new_price

#print (f'{apply_vat(100 , 110)}')