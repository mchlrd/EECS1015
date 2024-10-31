#fruit quantity
num_apples = int(input('How many apples? '))
num_peaces = int(input('How many peaches? '))
num_watermelon = int(input('How many watermelons? '))

#fruit's price per unit
price_apples = 2.94
price_peaches = 3.99
price_watermelon = 7.99

#calculate the total price
total_price = (price_apples * num_apples) + (price_peaches * num_peaces) + (price_watermelon * num_watermelon)

#return the total price
print(total_price)
