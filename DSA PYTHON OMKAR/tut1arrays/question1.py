# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expense=[2000,2350,2600,2130,2190]

# question 1 
print("You spent {} dollars extra in Feb as compared to Jan".format(monthly_expense[1]-monthly_expense[0]))

# question 2
print("Total expense in first 3 months: {}".format(sum(monthly_expense[:3])))

from functools import reduce 
total_expense=reduce(lambda x,y:x+y, monthly_expense[:3])
print(f"total expense upto month 3 is {total_expense}")

# question 3 
months=['jan','feb','march','april','may']

for month,price in zip(months,monthly_expense):
    if price==2000:
        print(f"You spent $2000 in the month {month}")

# question 4 
monthly_expense.append(1980)
print(monthly_expense)

# question 5 
monthly_expense.insert(3,monthly_expense[3]-200)
print(monthly_expense[3])