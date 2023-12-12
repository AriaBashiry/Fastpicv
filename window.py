from tkinter import *
import requests
import json



api = requests.get("http://127.0.0.1/users")
response = '{ "users": '+api.text+' }'

root = Tk()
root.title("Post App")
root.geometry("400x400")




data = json.loads(response)
for i in data['users']:
    nametxt = Label(text="name")
    emailtxt = Label(text="email")

    print(i)
    print(data)
    name = i['name']
    email = i['email']

    nametxt.config(text=name)
    emailtxt.config(text=email)

    nametxt.pack()
    emailtxt.pack()




root.mainloop()