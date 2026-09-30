




#tamrine avval sheklha ba setare

for i in range(1,8):
    for j in range(1,8):
        if j + i == 8 or i == j or i == 1 or i == 7:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1,8):
    for j in range(1,8):
        if j + i == 8 or i == j or j == 1 or j == 7:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1,8):
    for j in range(1,8):
        if j == 1 or (i == 4 and j == 7) or (i == 2 and j == 3) or (i == 3 and j == 5) or (i == 5 and j == 5) or (i == 6 and j == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#agar list bld budim:)
star = [(2,3),(3,5),(4,7),(5,5),(6,3)]
for i in range(1,8):
    for j in range(1,8):
        if j == 1 or (i,j) in star:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(1,8):
    for j in range(1,8):
        if j == 7 or (i ==2  and j == 5) or (i == 3 and j == 3) or (i == 4 and j == 1) or (i == 5 and j == 3) or (i == 6 and j ==5):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#agar list bld budim:)
star = [(2,5),(3,3),(4,1),(5,3),(6,5)]
for i in range(1,8):
    for j in range(1,8):
        if j == 7 or (i,j) in star:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#tamrine dovvom mohasebe prdkhti

while True:
   salary = int(input("your salary:"))
   if salary > 200 or salary < 5:
       print("wrong salary. try again!")
   elif 100 <= salary <= 200:
       pardakhti = 0.65 * salary
       print("pardakhti ba 35% tax:", pardakhti)
   elif 90 <= salary < 100:
       pardakhti = 0.8 * salary
       print("pardakhti ba 20% tax:", pardakhti)
   elif 70 <= salary < 90:
       pardakhti = 0.85 * salary
       print("pardakhti ba 15% tax:", pardakhti)
   elif 60 <= salary < 70:
       pardakhti = 0.9 * salary
       print("pardakhti ba 10% tax:", pardakhti)
   elif 50 <= salary < 60:
       pardakhti = 0.95 * salary
       print("pardakhti ba 5% tax:", pardakhti)
   elif 40 <= salary < 50:
       pardakhti = 0.97 * salary
       print("pardakhti ba 3% tax:", pardakhti)
   elif 30 <= salary < 40:
       pardakhti = 0.98 * salary
       print("pardakhti ba 2% tax:", pardakhti)
   else:
       print("no tax, pardakhti:", salary)

#tamrine sevvom nomarate daneshamuz ha
while True:
    score = float(input("student score:"))
    if score < 0 or score > 20:
        print("wrong score, try again!")
    elif 17 <= score <= 20:
        if 19 <= score <= 20:
            print("A++")
        elif 18 <= score < 19:
            print("A+")
        else:
            print("A")
    elif 14 <= score < 17:
            if 16 <= score < 17:
                print("B++")
            elif 15 <= score < 16:
                print("B+")
            else:
                print("B")
    elif 11 <= score < 14:
            if 13 <= score < 14:
                print("C++")
            elif 12 <= score < 13:
                print("C+")
            else:
                print("C")
    elif 8 <= score < 11:
            if 10 <= score < 11:
                print("D++")
            elif 9 <= score < 10:
                print("D+")
            else:
                print("D")
    elif 5 <= score < 8:
            if 7 <= score < 8:
                print("E++")
            elif 6 <= score < 7:
                print("E+")
            else:
                print("E")
    elif 2 <= score < 5:
            if 4 <= score < 5:
                print("F++")
            elif 3 <= score < 4:
                print("F+")
            else:
                print("F")
    else:
         print("you failed.")



#tamrine chaharom user and pass
while True:
    age = int(input("your age:"))
    username = input("username:")
    password = input("password:")
    length = len(password)
    if age < 16:
        print("mahdudiate senni zire 16 sal")
        break
    elif username == "admin" and password == "1234567890":
        print("welcome.")
        break
    elif len(password) < 10:
        print("not strong password, try again.")
        if username != "admin" and password == "1234567890":
            print("wrong username, try again.")
        elif username == "admin" and password != "1234567890":
            print("wrong password, try again.")
        else:
            print("wrong user and pass, try again.")
    