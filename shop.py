####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Salma's"
signature_flavors = ["banofee", "salted caramel", "pistachio"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    for i in menu:
        print ("- %s: %s KD" %(i,menu[i]) )


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for i in original_flavors:
        print (" - %s" %(i))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for i in signature_flavors:
        print (" - %s" %(i))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        print ("Sorry this item is not available in the menu.")
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    order = input ("> ")

    while order != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input ("> ")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >=5:
        print ("This order is eligible for credit card payment.")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in menu:
            total = total + menu[order]
        elif order in original_flavors:
            total = total + original_price
        elif order in signature_flavors:
            total = total + signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print ("- %s" %order)
    totalP= get_total_price(order_list)
    print ("Your total is: %s KD" %(totalP))
    accept_credit_card(totalP)
    print ("Thank you for shopping at %s!! Please come again!" %(cupcake_shop_name))

