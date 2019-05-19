#BRR
#MSAW


import random, string



inp_letter1=input('''
                        "1" for vowel 
                        "2" for constonant 
                        "3" for any letter

    First letter ------->    ''')
inp_letter2=input('Second letter ----->  ')
inp_letter3=input('Third letter ----->  ')
inp_letter4=input('Fourth letter ----->  ')
inp_letter5=input('Fifth letter ----->  ')

vowels="aeiouy"
const='bcdfghjklmnpqrstvwxz'
others=string.ascii_lowercase


def gen_erator():

  if inp_letter1=="1":
    letter1=(random.choice(vowels)).upper()

  elif inp_letter1=="2":
    letter1=(random.choice(const)).upper()

  elif inp_letter1=="3":
    letter1=(random.choice(others)).upper()

  else:
    letter1=inp_letter1.upper()


  if inp_letter2=="1":
    letter2=(random.choice(vowels))

  elif inp_letter2=="2":
    letter2=(random.choice(const))

  elif inp_letter2=="3":
    letter2=(random.choice(others))

  else:
    letter2=inp_letter2




  if inp_letter3=="1":
    letter3=(random.choice(vowels))

  elif inp_letter3=="2":
    letter3=(random.choice(const))

  elif inp_letter3=="3":
    letter3=(random.choice(others))

  else:
    letter3=inp_letter3



  if inp_letter4=="1":
    letter4=(random.choice(vowels))

  elif inp_letter4=="2":
    letter4=(random.choice(const))

  elif inp_letter4=="3":
    letter4=(random.choice(others))

  else:
    letter4=inp_letter4




  if inp_letter5=="1":
    letter5=(random.choice(vowels))

  elif inp_letter5=="2":
    letter5=(random.choice(const))

  elif inp_letter5=="3":
    letter5=random.choice(others)

  else:
    letter5=inp_letter5

  name2=letter1+letter2+letter3+letter4+letter5
  return name2

for i in range(20):
  print(gen_erator())
