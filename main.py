from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu = Menu()

money_handler = MoneyMachine()
play = True
while play:
 options = menu.get_items()
 choice = input(f"What would you like:{options}:").lower()
 if choice == "off":
    play = False
 
 elif choice == "report":
     maker.report()
     money_handler.report()
 else:
    drink = menu.find_drink(choice)
    if (maker.is_resource_sufficient(drink)):
      money_handler.make_payment(drink.cost)
    if maker.is_resource_sufficient(drink) == False:
       print("Sorry there are not enough resources!")


    