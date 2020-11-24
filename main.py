import random

quit = True
count = 0
total = 0
print("Jaden's Math Practice!!👍🤎")
print("Addition")

while(quit):
  for i in range(10):
    x = random.randrange(1, 10)
    answer = int(input(f"{x} + 5 = "))
    total = total +1
    print(answer)
    b = x + 5
    if answer == b:
        print("Correct! Good Job!👍")
        count = count + 1
    else:
        print("Well.. try again")
  con = input("Do you want to continue(Y/N)? ").upper()
  if con == "N":
      quit = False
a = int(count / total * 100)
print(f"Jaden, You have {count}point in {total}!! it's ${a}%")
