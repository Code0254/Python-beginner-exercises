def card_game(ed, grace, linus):
    count = 0
    for i in range(4):
        for j in range (4):
            print (f'j is {j} and i is {i}')
            if ed[j]> grace[i] and ed[j] > linus[i]:
                count+= 1
                ed[j] = 0
                break
    return count >=2


ed = [2,5,8,11]
grace = [1,4,7,10]
linus= [0,3,6,9]

card_game(ed, grace, linus)

            