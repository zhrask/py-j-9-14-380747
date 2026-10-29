








#tamrinne gym
#while True:
#    gym_menu = input("1.sabtenam 2.exit")
#    while True:
#        match gym_menu:
#            case "1":
#                sabtenam_menu = input("1.moshakhasat 2.savabeq varzeshi 3..exit")
#                match sabtenam_menu:
#                    case "1":
#                        name = input("name:")
#                        if name.isalpha() != True:
#                            print("try again.")
#                            break
#                        else:
#                            name = name.title()
#                            print(name, "accepted.")
#                        last_name = input("last name:")
#                        if last_name.isalpha() != True:
#                            print("try again.")
#                            break
#                        else:
#                            last_name = last_name.title()
#                            print(last_name, "accepted.")                      
#                        father_name = input("father name:")
#                        if father_name.isalpha() != True:
#                            print("try again.")
#                            break
#                        else:
#                            father_name = father_name.title()
#                            print(father_name, "accepted.")
#                        age = int(input("age:"))
#                        if age < 18:
#                            print("emkane pazireshe afrd kmtr 18 sal b surte online vojud ndr.")
#                            break
#                        else:
#                            print(age, "accepted.")
#                        phone_number = int(input("phone number:"))
#                        if len(str(phone_number)) != 11 or str(phone_number).isnumeric() != True or str(phone_number).startswith("09") != True:
#                            print("lotfn shomare hamrahe 11 rqmi ba 09- vared konid.")
#                            break
#                        else:
#                            print(phone_number, "accepted.")
#                        email = input("email:")
#                        if email.endswith("@gmail.com") != True:
#                            print("try again.")
#                            break
#                        else:
#                            print(email, "accepted.")
#                        height = float(input("your heaight(cm):"))
#                        print(height, "accepted.")
#                        weight = float(input("your weight(kg):"))
#                        print(weight, "accepted.")
#                        sex_menu = input("1.male 2.female 3.other")
#                        match sex_menu:
#                            case "1":
#                                print("male. accepted")
#                            case "2":
#                                print("female. accepted")
#                            case "3":
#                                print("other. accepted")
#                        bime = int(input("aya niaz b bime varzeshi darid?(1.true 2.false):"))
#                        if bime != 1 and bime != 2:
#                            print("try again.")
#                        bime = bime == 1
#                        print("bime varzeshi:", bime)
#                        if bime == True:
#                            bime_cost = int(input("mablaqe bime ra vared konid:"))
#                            pardakhti_bime = bime_cost * 1.1
#                            print("bime shoma anjam shod prdakhti shoma:", pardakhti_bime)
#                        coach_menu = input("1.morabbi mikham 2. bedune morabbi")
#                        match coach_menu:
#                            case "1":
#                                coach = int(input("aya morabbie khassi made nzr drid?(1.ble 2.kheir):"))
#                                if coach != 1 and coach != 2:
#                                    print("try again.")
#                                coach = coach == 1
#                                import random
#                                coach_names = ["sara", "maryam", "setreh"]
#                                print("yeki az behtrin morabi haye ma baraye shoma:", random.choice(coach_names))
#                                if coach == True: 
#                                    coach_name = input("name morabbie made nzr shoma(sara, maryam, setareh):") 
#                                    if coach_name.isalpha() != True or coach_name != "sara" or coach_name != "maryan" or coach_name != "setareh":
#                                        print("try again.")
#                                        break
#                                    else:
#                                        print("morabie shoma", coach_name)
#                            case "2":
#                                print("bedune morabbi")
#                        gym_cost = int(input("hazine sabtenam:"))
#                        if bime == True:
#                            gym_cost = gym_cost + pardakhti_bime
#                            print("pardakhti:", gym_cost)
#                        else:
#                            print("pardakhti:", gym_cost)
#                    case "2":
#                        sabeqe_varzeshi = input("aya qbln varzeshi anjam dadid?(1.ble 2.kheir):")
#                        if sabeqe_varzeshi != 1 and sabeqe_varzeshi != 2:
#                            print("try again.")
#                            break
#                        sabeqe_varzeshi = sabeqe_varzeshi == 1
#                        if sabeqe_varzeshi == True:
#                            name_varzesh_qabli = input("name varzesh ya varzeshhayee k qbln anjm ddid:")
#                            tule_dore_varzesh = input("che modatte b varzesh mshqul budid:")
#                            print(name_varzesh_qabli, tule_dore_varzesh)
#                        else:
#                            print("hich vqt baraye shuru dir nist.")
#                    case "3":
#                        break
#            case "2":
#                break












