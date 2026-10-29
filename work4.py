





#tamrine shabih saze hesabe banki
#transactions = []
#mojudi = 0
#while True:
#    start_menu = input("1.variz 2.bardasht 3.mojudi 4.tarakonesh show 5.majmue varizi ha show 6.varizi show 7.exit")
#    while True:
#        match start_menu:
#            case "1":
#                variz = int(input("mablaqe varizie shoma:"))
#                if variz > 0:
#                    mojudi += variz
#                    transactions.append(("variz", variz))
#                    print("variz ba moafqiat anjm shod.")
#                    break
#                else:
#                    print("mablaq na motabar.")
#                    break
#            case "2":
#                bardasht = int(input("mablaqe bardashtie shoma:"))
#                if bardasht > 0 and bardasht <= mojudi:
#                    mojudi -= bardasht
#                    transactions.append(("bardasht", bardasht))
#                    print("brdsht ba moafqiat anjm shod.")
#                    break
#                else:
#                    print("mojudie shoma kafi nist.")
#                    break
#            case "3":
#                print("mojudie shoma:", mojudi)
#                break
#            case "4":
#                for i in transactions:
#                    print(i)
#                break
#            case "5":
#                majmu_variz = 0
#                for i in transactions:
#                    if i[0] == "variz":
#                        majmu_variz += i[1]
#                print("majmue varizie shoma:", majmu_variz)
#                break
#            case "6":
#                for i in transactions:
#                    if i[0] == "variz":
#                        print(i)
#                break
#            case "7":
#                break




#shabih saze hesabe bnki ye model dg

#transactions = []
#mojudi = 0
#while True:
#    start_menu = input("1.variz 2.bardasht 3.mojudi 4.tarakonesh show 5.majmue varizi ha show 6.varizi show 7.exit")
#    while True:
#        match start_menu:
#            case "1":
#                variz = int(input("mablaqe varizie shoma:"))
#                if variz > 0:
#                    mojudi += variz
#                    transactions.append(+variz)
#                    print("variz ba moafqiat anjm shod.")
#                    break
#                else:
#                    print("mablaq na motabar.")
#                    break
#            case "2":
#                bardasht = int(input("mablaqe bardashtie shoma:"))
#                if bardasht > 0 and bardasht <= mojudi:
#                    mojudi -= bardasht
#                    transactions.append(-bardasht)
#                    print("brdsht ba moafqiat anjm shod.")
#                    break
#                else:
#                    print("mojudie shoma kafi nist.")
#                    break
#            case "3":
#                print("mojudie shoma:", mojudi)
#                break
#            case "4":
#                for i in transactions:
#                    print(i)
#                break
#            case "5":
#                majmu_variz = 0
#                for i in transactions:
#                    if i > 0:
#                        majmu_variz += i
#                print("majmue varizie shoma:", majmu_variz)
#                break
#            case "6":
#                for i in transactions:
#                    if i > 0:
#                        print("+", i)
#                break
#            case "7":
#                break




#tamrine modiriate ketbkhaneh
#books = []
#while True:
#    library = input("1.afzudne ketb 2.namayeshe ketb ha 3.josto juye ketb 4.tedade ketb ha 5.pak krdne hme ketb ha 6.exit")
#    while True:
#        match library:
#            case "1":
#                new_book = input("your new book name:")
#                if new_book in books:
#                    print("the book is already available.")
#                    break
#                else:
#                    books.append(new_book)
#                    print("your book has been added to library.")
#                break
#            case "2":
#                print(books)
#                break
#            case "3":
#                check_book = input("what book are you looking for:")
#                if check_book in books:
#                        print("the book is availbe.")
#                        break
#                else:
#                    print("the book is not availble.")
#                    break
#            case "4":
#                print("books count:", len(books))
#                break
#            case "5":
#                books.clear()
#                print("library has been cleared.")
#                break
#            case "6":
#                break



#tamrine bazie hadse add
#guesses = []
#while True:
#    guesses_menu = input("1.sabte hads 2.hads show 3.tedade hads show 4.bozorgtrin hads show 5.pak krdne hads ha 6.exit")
#    while True:
#        match guesses_menu:
#            case "1":
#                number = float(input("number:"))
#                if number in guesses:
#                    print("in add qbln vared shode.")
#                    break
#                else:
#                    guesses.append(number)
#                    print("adde shoma vared shod.")
#                    break
#            case "2":
#                print(guesses)
#                break
#            case "3":
#                print("tedade hads ha:", len(guesses))
#                break
#            case "4":
#                if guesses:
#                    print("bozorgtrin hads:", max(guesses))
#                    break
#                else:
#                    print("addadi vojud ndrd.")
#                    break
#            case "5":
#                guesses.clear()
#                print("hads ha pak shod.")
#                break
#            case "6":
#                break






#tamrine sabade kharid
#products = []
#prices = []
#while True:
#    sabade_kharid = input("1.afzudne mahsul 2.namayeshe sbde kharid 3.hazfe mhsul 4.mohasebe tedde mahsulat 5. barresi vujude mahsul 6.majmue qeimte mahsulate sabade kharid 7.exit")
#    while True:
#        match sabade_kharid:
#            case "1":
#                mahsul = input("name mahsul:")
#                qeimt_mahsul = int(input("qeimte mahsul:"))
#                products.append(mahsul)
#                prices.append(qeimt_mahsul)
#                print("mahsule shoma b sabade khrid ezfe shod.")
#                break
#            case "2":
#                for i in range(len(products)):
#                    print(products[i], ":", prices[i])
#                break
#            case "3":
#                hazf_mahsul = input("name mhsuli k mikhahid hzf konid:")
#                if hazf_mahsul in products:
#                    shomre_mahsul_hazfi = products.index(hazf_mahsul)
#                    products.pop(shomre_mahsul_hazfi)
#                    prices.pop(shomre_mahsul_hazfi)
#                    print("mahsule shoma hzf shod.")
#                    break
#                else:
#                    print("mahsul dr sbd mojud nist.")
#                    break
#            case "4":
#                print("tedde mahsulate shoma:", len(products))
#                break
#            case "5":
#                check_mahsul = input("name mahsuli k mikhahid check konid:")
#                if check_mahsul in products:
#                    print("mahsul mojud ast.")
#                    break
#                else:
#                    print("mahsul na mojud.")
#                    break
#            case "6":
#                print("majmue qeimt haye kharide shoma:", sum(prices))
#                break
#            case "7":
#                break













