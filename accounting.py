melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

MELON_PRICES = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

def melons_purchased(path):
    """ Tallies the number of melons based on melon type, from the file of Orders by Type that includes Order Number, Melon Type, and Number of Melons Purchased """
    
    melon_orders_file = open(path)

    for line in melon_orders_file:
        melon_order = line.split("|")
        melon_type = melon_order[1]
        melon_count = int(melon_order[2])
        melon_tallies[melon_type] += melon_count

    melon_orders_file.close()

def melon_revenue(path):
    """ Takes the counts of Melons by Type Function and multiplies them by their respective Melon Prices """

    print "\n TOTAL REVENUE"

    melons_purchased(path)

    total_revenue = 0

    for melon_type in melon_tallies:
        price = MELON_PRICES[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold {} {} melons at ${} each for a total of ${}".format(melon_tallies[melon_type], melon_type, price, revenue)

def sales_report(path):
    """ Creates a Sales Report that sums the sales made by Salespeople versus the Online store and states if Salespeople should still be employed based on the results of those sales. """

    print "\n SALES DATA"

    sales_orders_file = open(path)

    sales = [0, 0]
    
    for line in sales_orders_file:
        order_price = line.split("|")
        if order_price[1] == "0":
            sales[0] += float(order_price[3])
        else:
            sales[1] += float(order_price[3])
    
    print "Salespeople generated ${} in revenue.".format(sales[1])
    
    print "Internet sales generated ${} in revenue.".format(sales[0])
    
    if sales[1] > sales[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"


melon_revenue("orders-by-type.txt")
sales_report("orders-with-sales.txt")

