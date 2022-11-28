def delete_reps(given_list,max_N): #[1,2,3,1,2,1,2,3] max n is 2
    val_to_check=0
    counter = 0 #1 2
# we take item in list, count the number of times it appears. if its count == 2 we del its position

    for item in given_list: #1 
        val_to_check = item # val to check is 1 
        for index, val in enumerate(given_list): #index 5, val 1
            if counter == 0 and val == val_to_check: #1 == 1 
                counter += 1
            elif counter < max_N and val == val_to_check: #1<2 and 1 = 1
                counter +=1
            elif counter == max_N and val== val_to_check:
                del given_list[index]
            else:
                continue
        counter = 0
    print (given_list) #iterate throught entire list before printing

given_list = [1,2,3,1,2,1,2,3] 
number = 0
delete_reps(given_list,number)




        
