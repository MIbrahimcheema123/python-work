# how to take profit
actual_cost =float(input("enter the total cost of the thing :"))
selling_cost =float(input("enter the sale cost of the thing :"))
if (actual_cost<selling_cost) :
    amount = selling_cost - actual_cost
    print("total profit = {0}".format(amount))
else:
    print("No Profit!!!")