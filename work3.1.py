



#tamrinne bimarestn
while True:
    hospital_menu = input("1.paziresh 2.restaurant 3.exit")
    while True:
        match hospital_menu:
            case "1":
                paziresh_menu = input("1.moshakhasat 2.savabeq pezeshki 3.khadamate morede nazar 4.exit")
                match paziresh_menu:
                    case "1":
                        name = input("name:")
                        if name.isalpha() != True:
                            print("try again.")
                            break
                        else:
                            name = name.title()
                            print(name, "accepted.")
                        last_name = input("last name:")
                        if last_name.isalpha() != True:
                            print("try again.")
                            break
                        else:
                            last_name = last_name.title()
                            print(last_name, "accepted.")                      
                        father_name = input("father name:")
                        if father_name.isalpha() != True:
                            print("try again.")
                            break
                        else:
                            father_name = father_name.title()
                            print(father_name, "accepted.")
                        age = int(input("age:"))
                        if age < 18:
                            print("emkane pazireshe afrd kmtr 18 sal b surte online vojud ndr.")
                            break
                        else:
                            print(age, "accepted.")
                        kodde_melli = int(input("kodde melli:"))
                        if len(str(kodde_melli)) != 10 or str(kodde_melli).isnumeric() != True:
                            print("kodde melli 10 rqmi vared konid.")
                            break
                        else:
                            print(kodde_melli, "accepted.")
                        phone_number = int(input("phone number:"))
                        if len(str(phone_number)) != 11 or str(phone_number).isnumeric() != True or str(phone_number).startswith("09") != True:
                            print("lotfn shomare hamrahe 11 rqmi ba 09- vared konid.")
                            break
                        else:
                            print(phone_number, "accepted.")
                        email = input("email:")
                        if email.endswith("@gmail.com") != True:
                            print("try again.")
                            break
                        else:
                            print(email, "accepted.")
                        job_menu = input("1.shaqel 2.mohassel 3.bazneshsteh 4.hichkodam")
                        match job_menu:
                            case "1":
                                job = input("your job:")
                                if job.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    job = job.title()
                                    print(job, "accepted.")
                            case "2":
                                tahsilat = input("last degree:")
                                if tahsilat.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    tahsilat = tahsilat.title()
                                    print(tahsilat, "accepted.")
                            case "3":
                                bazneshasteh = input("organe bazneshastegi:")
                                if bazneshasteh.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    bazneshasteh = bazneshasteh.title()
                                    print(bazneshasteh, "accepted.")
                            case "4":
                                print("accepted.")
                        date_menu = input("1.year 2.month 3.date")
                        match date_menu:
                            case "1":
                               year =  int(input("year:"))
                               if str(year).isnumeric() != True or len(str(year)) != 4 or str(year).startswith("13") != True:
                                   print("lotfn sale tvlodde khodra ba formte 13-- vared konid.")
                                   break
                            case "2":
                               month =  int(input("month:"))
                               if str(month).isnumeric() != True or month > 12  or month < 1:
                                   print("try again.")
                                   break
                            case "3":
                               date =  int(input("date:"))
                               if str(date).isnumeric() != True or date > 31 or date < 1:
                                   print("try again")
                                   break
                        print(year, month, date, "accepted")                            
                        sex_menu = input("1.male 2.female 3.other")
                        match sex_menu:
                            case "1":
                                print("male. accepted")
                            case "2":
                                print("female. accepted")
                            case "3":
                                print("other. accepted")
                        bime_menu = input("1.bime paye 2.bime tkmili 3.faqede bime")
                        match bime_menu:
                            case "1":
                                bime_paye = input("bime paye shoma:")
                                if bime_paye.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    bime_paye = bime_paye.title()
                                    print(bime_paye, "accepted.")
                            case "2":
                                bime_takmili = input("bime takmilie shoma:")
                                if bime_takmili.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    bime_takmili = bime_takmili.title()
                                    print(bime_takmili, "accepted.")
                            case "3":
                                print("faqede bimeh. accepted.")
                        address_menu = input("1.ostan 2.shahr 3.khiaban 4.kuche 5.pelak 6.vahed")
                        match address_menu:
                            case "1":
                                ostan = input("ostan:")
                                if ostan.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    ostan = ostan.title()
                                    print(ostan, "accepted")
                            case "2":
                                shahr = input("shahr:")
                                if shahr.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    shahr = shahr.title()
                                    print(shahr, "accepted")
                            case "3":
                                khiaban = input("khiaban:")
                                if khiaban.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    khiaban = khiaban.title()
                                    print(khiaban, "accepted")
                            case "4":
                                kuche = input("kuche:")
                                if kuche.isalpha() != True:
                                    print("try again.")
                                    break
                                else:
                                    kuche = kuche.title()
                                    print(ostan, "accepted")
                            case "5":
                                pelak = input("pelak:")
                                if pelak.isnumeric() != True:
                                    print("try again.")
                                    break
                                else:
                                    print(pelak, "accepted.")
                            case "6":
                                vahed = input("vahed:")
                                if vahed.isnumeric() != True:
                                    print("try again.")
                                    break
                                else:
                                    print(vahed, "accepted.")
                    case "2":
                        smoking = int(input("aya sigar mikeshid(1.true 2.false):"))
                        if smoking != 1 and smoking != 2:
                            print("try again.")
                            break
                        else:
                            smoking = smoking == 1
                            print("smoking:", smoking)
                        bastari = int(input("aya dar yek sale akhir bastari shodid(1.true 2.false);"))
                        if bastari != 1 and bastari != 2:
                            print("try again.")
                            break
                        else:
                            bastari = bastari == 1
                            print("bastari dar yek sale akhir:", bastari)
                        pregnancy = int(input("aya bardar hastid(1.true 2.false"))
                        if pregnancy != 1 and pregnancy != 2:
                            print("try again.")
                            break
                        else:
                            pregnancy = pregnancy == 1
                            print("pregnancy:", pregnancy)
                        shirdehi = int(input("aya dar dorane shirdehi hstin(1.true 2.false):"))
                        if shirdehi != 1 and shirdehi != 2:
                            print("try again.")
                            break
                        else:
                            shirdehi = shirdehi == 1
                            print("shirdehi:", shirdehi)
                        jarahi = int(input("aya amale jarahi dr yek sale akhir dshtid(1.true 2.false):"))
                        if jarahi != 1 and jarahi != 2:
                            print("try again.")
                            break
                        else:
                            jarahi = jarahi == 1
                            print("jarahi:", jarahi)
                        bimari = int(input("aya sebeqe bimri darid(1.true 2.false):"))
                        if bimari != 1 and bimari != 2:
                            print("try again.")
                            break
                        bimari = bimari == 1    
                        if True:
                            print("bimari:", bimari)
                            if bimari == True:
                                name_bimari = input("name bimari:")
                                print(name_bimari)
                        medicine = int(input("aya daruye khassi msrf mikonid(1.true 2.false):"))
                        if medicine != 1 and medicine != 2:
                            print("try again.")
                            break
                        medicine = medicine == 1    
                        if True:
                            print("medicine:", medicine)
                            if medicine == True:
                                name_medicine = input("name daru:")
                                print(name_medicine)
                    case "3":
                        khedmat_menu = input("1.azmayesh 2.bastari 3.jarrahi 4.exite")
                        match khedmat_menu:
                            case "1":
                                azmayesh = input("name azmayesh madde nzre khodra vared konid:")
                                if azmayesh.isalnum() != True:
                                    print("try again.")
                                    break
                                else:
                                    doctor_name = input("name pezeshke shoma:")
                                    if doctor_name.isalpha() != True:
                                        print("try again.")
                                        break
                                    else:
                                        print("azmayeshhaye drkhastie shoma:", azmayesh,"name pezeshke shoma:", doctor_name)
                            case "2":
                                bakhshe_bastari = input("name bkhshe bastari:")
                                if bakhshe_bastari.isalnum() != True:
                                    print("try again.")
                                    break
                                else:
                                    doctor_name = input("name pezeshke shoma:")
                                    if doctor_name.isalpha() != True:
                                        print("try again.")
                                        break
                                    else:
                                        print("bakhshe bastari:", bakhshe_bastari, "name pezeshke shoma:", doctor_name)
                            case "3":
                                jarrahi = input("name amale jarrahi:")
                                if jarrahi.isalnum() != True:
                                    print("try again.")
                                    break
                                else:
                                    doctor_name = input("name pezeshke shoma:")
                                    if doctor_name.isalpha() != True:
                                        print("try again.")
                                        break
                                    else:
                                        print("name jarrahi:", jarrahi, "name pezeshke shoma:", doctor_name)
                            case "4":
                                break
                    case "4":
                        break
            case "2":
                restaurant_menu = input("1.breakfast 2.meals 3.drinks 4.exit")
                while True:
                    match restaurant_menu:
                        case "1":
                            breakfast_menu = input("1.nimru 2.omlet 3.exit")
                            match breakfast_menu:
                                case "1":
                                    num_nimru = int(input("tedade sefresh:"))
                                    qeimt_nimru = 1.1 * 300 * num_nimru
                                    if num_nimru <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_nimru)
                                case "2":
                                    num_omlet = int(input("tedade sefresh:"))
                                    qeimt_omlet = 1.1 * 400 * num_omlet
                                    if num_omlet <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_omlet)
                                case "3":
                                    break
                        case "2":
                            meals_menu = input("1.qorme sabzi 2.kubide 3.exit")
                            match meals_menu:
                                case "1":
                                    num_qormeh = int(input("tedade sefresh:"))
                                    qeimt_qormeh = 1.1 * 500 * num_qormeh
                                    if num_qormeh <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_qormeh)
                                case "2":
                                    num_kubideh = int(input("tedade sefresh:"))
                                    qeimt_kubideh = 1.1 * 600 * num_kubideh
                                    if num_kubideh <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_kubideh)
                                case "3":
                                    break
                        case "3":
                            drinks = input("1.tea 2.coffee 3.water 4.exit")
                            match drinks:
                                case "1":
                                    num_tea = int(input("tedade sefresh:"))
                                    qeimt_tea = 1.1 * 150 * num_tea
                                    if num_tea <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_tea)
                                case "2":
                                    num_coffee = int(input("tedade sefresh:"))
                                    qeimt_coffee = 1.1 * 500 * num_coffee
                                    if num_coffee <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_coffee)
                                case "3":
                                    num_water = int(input("tedade sefresh:"))
                                    qeimt_water = 1.1 * 500 * num_water
                                    if num_water <= 0:
                                        print("try again.")
                                        break
                                    else:
                                        print("pardakhti:", qeimt_water)
                                case "4":
                                    break
                        case "4":
                            break
                break
            case "3":
                break


                        
                        


                        

                                
                            
                                

                        

                        




