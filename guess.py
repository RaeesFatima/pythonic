import random

random_num=random.randint(1, 100)
retries=0
while True:
  try:
    num=int(input("enter a num"))
    if num >=1 and num<=10:
      if num == random_num:
        print("yes")
        break
      else:
        print("press 1 to try again, 2 to exit")
        choice=int(input())
        if choice==1:
          # continue
          retries+=1
          print("retries", retries)
          if retries>5:
            print("you have exceeded the limit")
            break
        else:
          print("bye")
          break
    else:
      print("enter num within the range")
  except ValueError:
    print("enter valid num")