import currency
from prettytable import PrettyTable
import pandas as pd

#Data import
df = pd.read_csv('Shop.csv', delimiter=',', index_col=0, header=0, encoding='utf-8')
item1 = df.xs('One')
item2 = df.xs('Two')
item3 = df.xs('Three')
print(item1['Price'], item1['Item'], item1['Number'])


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

msg = str()
owner = 'Shop Owner'
items = {1: "Hat", 2: "Apple", 3: "Iron Sword"}
shop = ["Hat", "Apple", "Iron Sword"]
prices = {items[1]: 100, items[2]: 200, items[3]: 300}

NEWITEMS = [item1['Number'], item2['Number'], item3['Number']]
NEWSHOP = [item1['Item'], item2['Item'], item3['Item']]
NEWPRICES = [item1['Price'], item2['Price'], item3['Price']]


shopTable = PrettyTable(["Number", "Item", "Price"])


def tablegen():
    x = 0
    for x in NEWSHOP:
        shopTable.add_row([NEWITEMS[x], NEWSHOP[x], NEWPRICES[x]])
        x = x + 1


def salesman(msg):
    (print(Color.BOLD + "{0}: ".format(owner) + Color.END, "{0}".format(msg)))


def main():
    x = 0
    salesman("Hello, welcome to the shop.")
    salesman("This is what is currently available for sale:")

    shopTable.align["Number"] = "l"  # Left align city names
    shopTable.padding_width = 1  # One space between column edges and contents (default)
    shopTable.add_row([1, shop[0], prices[items[1]]])
    tablegen()
    print(shopTable)

    for i in items:
        print(i, shop[x])
        x = x + 1
    salesman("What would you like to buy?")
    choice = input("Enter a number: ")
    if choice == '1':
        salesman("Good choice, a beautiful {0}. That will be {1} quartz.".format(items[1], prices[items[1]]))
        if currency.playerQuartz >= prices[items[1]]:
            currency.playerQuartz = currency.playerQuartz - prices[items[1]]
            salesman("Great! I've added it to your inventory. You now have {0} quartz.".format(currency.playerQuartz))
        else:
            salesman("I'm sorry, you do not have enough quartz. You only have {0}. You need {1} more.".format(currency.playerQuartz, prices[items[1]]-currency.playerQuartz))
    elif choice == '2':
        salesman("Wonderful, a delicious {0}. That will be {1} quartz.".format(items[2], prices[items[2]]))
        if currency.playerQuartz >= prices[items[2]]:
            currency.playerQuartz = currency.playerQuartz - prices[items[2]]
            salesman("Great! I've added it to your inventory. You now have {0} quartz.".format(currency.playerQuartz))
        else:
            salesman("I'm sorry, you do not have enough quartz. You only have {0}. You need {1} more.".format(currency.playerQuartz, prices[items[2]]-currency.playerQuartz))
    elif choice == '3':
        salesman("Great decision, a strong {0}. That will be {1} quartz.".format(items[3], prices[items[3]]))
        if currency.playerQuartz >= prices[items[3]]:
            currency.playerQuartz = currency.playerQuartz - prices[items[3]]
            salesman("Great! I've added it to your inventory. You now have {0} quartz.".format(currency.playerQuartz))
        else:
            salesman("I'm sorry, you do not have enough quartz. You only have {0}. You need {1} more.".format(currency.playerQuartz, prices[items[3]]-currency.playerQuartz))
    else:
        salesman("I'm sorry, that's not an option.")
main()
