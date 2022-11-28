'''Create a python program that produces output similar to the one illustrated above'''

n= 5 # x axis 
k = 5 # y axis
for i in range (0,n+1):  #1  handles rows
    for j in range (k-i,0,-1): #(4,0,1) handles collumns(creates pattern) - values change according to outer loop
        print ('*', end = '') #printing stars, end= defines action after print, by default jumps to next line
    print ("\r") # end line after each row k-i

'''for k in range (4,0,-1):
    print (k, end = 'iu')'''