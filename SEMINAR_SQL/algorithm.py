import relations

#Potraga primarnih kljuceva preko funkcionalnih ovisnosti
for main in relations.dependencies:
    print(main,"=>:")

    (main_key,main_value)=main.split("->")

    #Petlja za provodenje algoritma za pronalazenje primarnog kljuca n puta 
    #radi rasirivanja i drugih teorema
    for i in range(len(relations.dependencies)):
        #print(set(main_key),"->",set(main_value))
     #   print("rel len:",len(relations.relation))
      #  print("main val len:",len(main_value))
       # print("main:",main_key+""+main_value) 
        # for el in main_key:
        #     if set(el).issubset(set(main_value)):
        #         continue
        #     else:

        #Primjena refleksivnosti
        main_value+=main_key
        # print("main value:",main_value)
        # print("main key:",main_key)

        #Pretrazivanje da li postoji tranzitivnost i primjenjivanje unije ako je pronadena tranzitivnost
        for e in relations.dependencies:
            (key,value)=e.split("->")
            # print("value:",value)
            # print("val:",val)
            # print("value:",value

            #Provajera ako A->B I B-> POTOME A->C i primjena unije A->B U A->C |=A->BC
            if set(key).issubset(set(main_value)):
                main_value+=value
            else:
                continue
        flag=0
        #print(main_key,"->",main_value)

        #Primjena Prosirivanja 
        for e in relations.relation:
            for k in relations.dependencies:
                (ky,v)=k.split("->")

                #Provjera da li postoji clan koji je ujedno kljuc neke funkcionalne osvisnosti
                # jer je njega optimalno prvog nadodati
                if e==ky and not(set(e).issubset(set(main_value))):
                    main_key+=ky
                    main_value+=v
                    flag=1
                    break
            if flag==1:
                break

        #ako nismo nasli clan koji je ujedno kljuc funkcionalne ovisnosti dodajemo
        # redom clan koji se ne nalazi s desne strane ograde relacije tj algoritma za primarni kljuc 
        if flag==0:
            for e in relations.relation:
                if set(e).issubset(set(main_value)):
                    continue
                else:
                    main_key+=e
                    main_value+=e
                    break

    #Postavljanje lijeve i desne strane u SET da se izbrisu clanovi koji su duplikati
    #npr. aabba->abcaacab |= ab->abc
    main_key=set(main_key)
    main_value=set(main_value)
    main_key="".join(main_key)
    main_value="".join(main_value)

    #stvaranje te relacije da se vidi da je kljuc pokrio sve clanove relacije
    temp=main_key+"->"+main_value
    print(temp)
    relations.prime_key.append(temp)
print(relations.prime_key)

#lista bez desne strane tj samo kljuc algoritma bez funckionalne ovisnosti
real_prime_key=[]
for e in relations.prime_key:
    (key,value)=e.split("->")
    real_prime_key.append("".join(sorted(key)))
# for e in real_prime_key:
#     e=sorted(e)
#     e="".join(e)

#print(set(sorted(real_prime_key)))

#Sortiranje liste kljuceva po velicini tako da ide od najmanjeg prema najvecemu
real_prime_key=sorted(list(set(real_prime_key)))
#print(real_prime_key)
# for e in real_prime_key:
#     e=''.join(sorted(e))
#real_prime_key.sort(key=len)
#print("sort()::",real_prime_key)

#Ispis primarnih kljuceva relacije
print(sorted(real_prime_key,key=len))





