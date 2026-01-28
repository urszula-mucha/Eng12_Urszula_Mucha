#What are objects.
#they are seen as extension of the dictionary

#Objects - instances of class (user) with real data
from user import User

user1 = User("Urszula", 30)
user2 = User("Dziecko", 12)

user1.print_bye()
user2.print_hello()

logger = Logger()
logger.add("Message 1")
logger.add("Message 2")

logger.print_logs()

#         --- PIP STANDARDS ---
#Set of rules to write code in python
# 4 spaces indent
# 80 character length
# 1 line before the function method should be empty
# File encoded in UTF 8
#Lines shouldnt end with white-end characters
#collections should be in parentheses
#Snake case to use in the names
#CamelCase for classes names
#Constans written with CAPITAL letters
#watchout for small letter "l" with "1" and big letter "O" with "0"