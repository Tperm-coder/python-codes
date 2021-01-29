import os
os.system('color b')
os.system('cls')

# TOC stands for type of connection
pap = True
while pap :
    os.system('color a')
    os.system('cls')
    TOC = input('series or parallel ?')
    if TOC == 'series' :
        NOR = int(input('what are the number of resistors ?'))
    # NOR stands for number of resistors


        SA = range(0,NOR)
    # SA stands for series array
        counter = 0
        SA2 = []
    # SA2 stands for series array number 2



        for i in SA :
            counter = counter + 1
            value = int(input('what is the value of resistor number ' + str(counter) + ' in ohm' + ' ?'))
            SA2.append(value)

        req = 0
    # req stands for equivilant resistance

        for i in SA2 :
            req = req + i

        print('equivilant resistance is ' + str(req) + ' ohm')
        input()



    elif TOC == 'parallel' :
        NOR = int(input('what is the number of resistors ?'))

        PA = range(0,NOR)
        counter = 0
        PA2 = []
        for i in PA :
            counter = counter +1
            voepr=int(input(('what is the value of the resistor number ' + str((counter)) + ' in ohm ?')))
            PA2.append(voepr)
        PA3 = []
        for i in PA2 :
            i = float((1/i))
            PA3.append(i)

        sezo = 0
        for i in PA3 :
            sezo = sezo + i

        sezo= float(1/sezo)
        print('equivilant resistance is ' + str(sezo) + ' ohm')
        input()
    tap = input('do you want to run again yes or no ?')
    if tap == 'yes' :
        pap = True
    else :
        pap = False
