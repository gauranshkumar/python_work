details = {'gauransh':{'pass':'9205768854',
'email':'gauranshk21@gmail.com','age':'16','phone':'9205768854'}
,'sharwan':{'pass':'9868958402',
'email':'sharwank2001@gmail.com','age':'50','phone':'9868958402'}
,'kiran':{'pass':'9968251108',
'email':'kb.kiranbharti74@gmail.com','age':'43','phone':'9968251108'},
'hitesh':{'pass':'9013825255','email':'hit.jag.2012@gmail.com','age':'22','phone':'9013825255'}
}

import json

def create_member(name,email,age,phone):
    add = {name:{'pass':phone, 'email':email, 'age':age, 'phone':phone}}
    details.update(add)
    with open("all_details.json",'w') as f:
        json.dump(details, f,indent=3)

