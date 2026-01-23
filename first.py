def get_total(stock, cart):
    """
        >>> shopping_list = ["bread", "apple", "banana", "orange", "juice", "chicken", "milk"]
        >>> store = {"banana": (1.5, 20), "apple": (2, 0), "orange": (2, 12), "kiwi": (0.5, 51), "bread": (3.5, 36), "milk": (4, 42), "cereal": (7.5, 26)}
        >>> get_total(store, shopping_list)
        11.0
        >>> store
        {'banana': (1.5, 19), 'apple': (2, 0), 'orange': (2, 11), 'kiwi': (0.5, 51), 'bread': (3.5, 35), 'milk': (4, 41), 'cereal': (7.5, 26)}
        >>> shopping_list = ["cereal", "cereal", "banana", "milk", "apple", "cheese"]
        >>> get_total(store, shopping_list)
        20.5
        >>> store
        {'banana': (1.5, 18), 'apple': (2, 0), 'orange': (2, 11), 'kiwi': (0.5, 51), 'bread': (3.5, 35), 'milk': (4, 40), 'cereal': (7.5, 24)}
    """
    total=0

    for item in cart:
        if item in stock:
            price = stock[item][0]
            qty = stock[item][1]
            if qty > 0:
                total = total + price
                stock[item] = (price, qty - 1)
    return total

shopping_list = ["bread", "apple", "banana", "orange", "juice", "chicken", "milk"]
store = {"banana": (1.5, 20), "apple": (2, 0), "orange": (2, 12), "kiwi": (0.5, 51), "bread": (3.5, 36), "milk": (4, 42), "cereal": (7.5, 26)}
print(get_total(store, shopping_list))
print(store)