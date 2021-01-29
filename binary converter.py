import os
os.system('color b')
jett = True
while jett :
    os.system('cls')
    als = input('From binary to number type btn, from number to binary type ntb: ')
    if als == 'btn' :
        print('write your number in binary (without spaces) and i will convert it to a real number ')
        x = input()
        x = x [::-1]
        val = 0
        counter = 0
        for i in x :
            if i == '1':
                val = val + (2 ** int(counter))
            counter = counter +1
        print(val)
        input()
    else :
        print('write your number and i will convert it to binary')
        z = int(input())
        arr = []
        arr2 = []
        arr3 = []
        vounter = 0
        if z == 1 :
            print(1)
        elif z == 0 :
            print(0)
        else :
            while z > 0 :
                counter = 0
                while 2 ** counter  <= z :
                    counter = counter + 1
                counter = counter - 1
                arr.append(counter)
                z  = z - (2 ** counter )
            for i in range(65) :
                arr3.append(i)
            for i in arr3 :
                if i in arr :
                    arr2.append('1')
                else:
                    arr2.append('0')
            st = ''.join(arr2)
            st = st[::-1]
            more = st.index('1')
            r = st[(more):]
            r = ' '.join(r)
            print(r)
            input()












    # ans = input('Do you want to run again ? yes or no ?')
    # if ans == 'yes' :
    #     jett = True
    # else :
    #     jett = False
