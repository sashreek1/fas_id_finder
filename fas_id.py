from fedora.client.fas2 import AccountSystem

fas = AccountSystem(username='sash713', password='m13e5s19s19i9')
s = input("enter a username : ")
people = fas.people_by_key(key=u'username',search=s,fields=['email'])
string = str(people)
x = string.find("'email': ")+9
string = string[x:-4]
print(string)