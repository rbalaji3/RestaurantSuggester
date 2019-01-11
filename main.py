from user import User
from api import Api
from restaurant import Restaurant
from city import City
from suggest import Suggest

#First: gets user to log in
#Takes note of what they have eaten at previously, helps them find stuff by suggesting restaurants
#stores all restaurant data using api
#asks if they want to eat somewhere familiar or somewhere new


print("Please enter your username")
username = input("Username: ")
print("Please enter your password: ")
password = input("Password: ")

print("Please enter your city")
city_name = input()
user_city = City(city_name)
user = User(username, password, user_city)
print("Please enter the restaurants you have eaten at: (Enter quit to quit)")

data = {}
rest_name = ""
while True:
    rest_name = input()
    if (rest_name == "quit"):
        break
    rest = Restaurant(rest_name, user_city)
    res_id = rest.getRestaurantId()
    try:
        data[res_id] += 1
    except:
        data[res_id] = 1
user.set_Data(data)
#user.set_Data({'18424988': 1, '17317233': 1, '17317873': 1, '17317935': 1, '17317476': 1, '17317260': 1, '17318108': 1, '17317942': 1})

suggestor = Suggest()
print("What type of restaurant suggestion would you like?")
print("For a familiar suggestion, enter 1")
print("For a less suggestion, enter 2")
print("For a new suggestion, enter 2")
choice = input()
if (choice == 1):
    print(suggestor.familiar(user))
if (choice == 2):
    print(suggestor.less_familiar(user))
if (choice == 3):
    print(suggestor.completlynew(user))
else:
    print("Invalid Input")
