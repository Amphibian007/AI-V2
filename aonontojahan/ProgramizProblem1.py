#Programiz.com Problem 1
'''Create a program to split the restaurant bill among friends.
Get an integer input for the total number of friends and assign it to the total_friends variable.
Get an integer input for the restaurant bill and assign it to the bill variable.
Calculate the tax amount, which is 20% of the bill.
Add the tax to the bill and divide the total bill among friends.'''


total_friends = int(input("Enter number of friends: "))
bill = int(input("Enter total bill amount: "))

tax_amount = (bill * 20) / 100
bill = bill + tax_amount
perpersionbill = bill / total_friends
print(perpersionbill)
