import random

def decesar(phrase, decalage):
  caracteres_speciaux = [32,33,39,40,41,44,45,46,58,59,63]
  error = False
  message = ""
  #Met le décalage à un nombre inférieur ou égal à 26
  while decalage > 26:
    decalage = decalage - 26
  for caractère in phrase:
    #Proscrit certains caractères spéciaux d'être décryptés
    if ord(caractère) in caracteres_speciaux:
      message = message + chr(ord(caractère))
    #Décrypte le message avec la clé de décalage donnée
    else:
      #Décrypte les lettres minuscules
      if ord(caractère) >= 97 and ord(caractère) < 123:
        if (ord(caractère) - decalage) < 97:
          message = message + chr(ord(caractère) - decalage + 26)
        else:
          message = message + chr(ord(caractère) - decalage)
      #Décrypte les lettres majuscules
      elif ord(caractère) >= 65 and ord(caractère) < 91:
        if (ord(caractère) - decalage) < 65:
          message = message + chr(ord(caractère) - decalage + 26)
        else:
          message = message + chr(ord(caractère) - decalage)          
      #Envoie un message d'erreur si un caractère n'est pas pris en compte
      else:
        error = True
        e = caractère
  if error == True:
    message = "La chaine de caractère n'est pas conforme à cause du caractère " + e
  return message



def cesar(phrase, decalage):
  caracteres_speciaux = [32,33,39,40,41,44,45,46,58,59, 63]
  error = False
  message = ""
  #Met le décalage à un nombre inférieur ou égal à 26
  while decalage > 26:
    decalage = decalage - 26
  for caractère in phrase:
    #Proscrit certains caractères spéciaux d'être cryptés
    if ord(caractère) in caracteres_speciaux:
      message = message + chr(ord(caractère))
    #Crypte le message avec la clé de décalage
    else:
      #Crypte les lettres minuscules
      if ord(caractère) >= 97 and ord(caractère) < 123:
        if (ord(caractère) + decalage) > 122:
          message = message + chr(ord(caractère) + decalage - 26)
        else:
          message = message + chr(ord(caractère) + decalage)
      #Crypte les lettres majuscules
      elif ord(caractère) >= 65 and ord(caractère) < 91:
        if (ord(caractère) + decalage) > 90:
          message = message + chr(ord(caractère) + decalage - 26)
        else:
          message = message + chr(ord(caractère) + decalage)
      #Envoie un message d'erreur si un caractère n'est pas pris en compte
      else:
        error = True
        e = caractère
  if error == True:
    message = """La chaine de caractère n'est pas conforme à cause du caractère " """ + e
  return message



####Fonction magique
def magie(texte, d, i):
    d2=random.randrange(0, 25)
    indicateur=chr(97+d2)
    r=cesar(texte[i], d2)
    indicateur=cesar(indicateur, d)
    r=r+indicateur
    return r

####Fonction immagique
def immagie(texte):
    cle=ord(texte[0])-96
    i=3
    r=""
    while i<len(texte):
        cle2=ord(decesar(texte[i], cle))-96
        r=r+decesar(texte[i-1], cle2)
        i=i+2
    return r


####CORPS
A=int(input("0 pour encrypter, 1 pour décrypter:"))
if A==0:
    x=str(input("Donnez le message à crypter:"))
    n=random.randrange(0, 25)
    r=chr(n+97)+" "
    i=0
    I=0
    erreur=False
    while i<len(x) and erreur==False:
        if len(magie(x, n, i))>3:
          while I<(len(magie(x, n, i))-1):
            print(magie(x, n, i)[I], end= "")
            I=I+1
          print(""" " """)
          erreur=True
        r=r+magie(x, n, i)
        i=i+1
    if erreur==False:
      print(r)
elif A==1:
    x=str(input("Donnez le message à décrypter:"))
    print(immagie(x))
else:
    print("ERREUR:La valeur choisie doit être 0 ou 1")
