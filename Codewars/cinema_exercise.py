def movie (card, ticket, perc):
    sist_A = 0


    sist_B = card
    tkt = ticket

    cont = 0

    while sist_B >= sist_A:
        cont += 1
        sist_A = ticket * cont 
        sist_B = tkt * perc

        sist_B = sist_B + tkt
    print(cont)

card = 500
ticket = 15
perc = 0.90


movie(card, ticket, perc)