import requests

firstname = "Urszula"
if firstname[-1] == "a":
    gender = "f"
else:
    gender = "m"

gender = "f" if firstname[-1] == "a" else "m" #shortened version of the code

#list comprehension
list_a = ["Adam", "Eva", "John", "jack", "will", "mark"]
list_b = []

#classic loop
for firstname in list_a:
    list_b.append(firstname.capitalize())

print(list_b)

#shortened version of code
         #<new item>             for <item>    in <list>
list_c = [firstname.capitalize() for firstname in list_a]
print(list_c)

list_d = []
for firstname in list_a:
    if firstname != firstname.capitalize():
        list_d.append(firstname.capitalize())

print(list_d)

         #<new item>             for <item>    in <list> if <condition>
list_e = [firstname.capitalize() for firstname in list_a if firstname != firstname.capitalize()]
print(list_e)

list_f = [firstname.capitalize() for firstname in list_a if firstname == firstname.capitalize()]
print(list_f)

list_g = []
for firstname in list_a:
    if len(firstname) >= 4:
        list_g.append(firstname)
print(list_g)

         #<new item> for <item>   in <list> if <condition>
list_g = [firstname for firstname in list_a if len(firstname) >= 4]
print(list_g)

         #<new item>     for <item>    in <list>
list_h = [len(firstname) for firstname in list_a ]
print(list_h)

#creating dictionary in a shortened way
         #<new item key: value>             for <item>    in <list>
dict_a = {firstname: firstname.capitalize() for firstname in list_a}
print(dict_a)

dict_b = {firstname: len(firstname) for firstname in list_a} #len shouldn't be a key, because keys mustn't repeat
print(dict_b) #duplicating a key won't throw an error but will loose the data!

#if you're using custom library and upload it to github, you cant commit ths library
#so other person won't be able to use it. You should generate the file with requirements.
# code to generate the requests.txt is pasted into the terminal: pip freeze > requirements.txt

#-----USING APIS-----
url = "https://api.agify.io/?name=Urszula"
response = requests.get(url)
print(response)
json = response.json()
print(json)
print(json["name"])
print(json["age"])