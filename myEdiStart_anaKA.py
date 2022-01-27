# textfile Bearbeitung
# analyze Kontoauszug

# (a) search for keywords
keylist = {'Kontostand','Basislastschrift','Kartenzahlung','LOHN','Übertrag','UEBERWEISUNG','DA-GUTSCHRIFT','EURO-UEBERW'}
keynums = [0,0,0,0,0,0,0,0,0]
# (b) search for pattern  nn.07. nn.07.
# (c) build list of block entries
# (d) search for pattern 'dd,dd H' and 'dd,dd S'
# (e) search for keyword 'Kontostand' and build list of Eingänge/Ausgänge
# (f) output / output data structure to Json file

myFile = open(r"C:/Users/49157/myPython/testfiles/text/KontoAuszug_07_21.txt","r", encoding='utf8')
print("---------------")
print("Analyse Kontoauszug:")
print("---------------")
lines = myFile.readlines()
n = 0
keycnt = 0
for mKeyword in keylist:
    keycnt +=1
    for line in lines:
        n += 1
        result = line.find(mKeyword)
        #print(result)
        if (result >= 0):
            print(f'{n}: {line}')
            keynums[keycnt] += 1
    print(f'{keynums[keycnt]} times found {mKeyword}')
print("%d lines read" % n)
print(f'{keynums}')
print("---------------")
print("Summen:")
n = 0
sumS = 0.0
sumH = 0.0
merk = 0
#with open('testfiles/text/KontoAuszug_07_21.txt') as f:
for line in lines:
    n += 1
    resultPN = line.find('PN:')
    if (resultPN >= 0):
        resultH  = line.find(' H')
        if (resultH >= 0):
            subPN = line[resultPN:resultPN+6]
            subBetrag = line[resultPN+7:resultH]
            subDate = line[0:6]
            subA = subBetrag.replace('.','')
            subB = subA.replace(',','.')
            sumH = sumH + float(subB)
            print(f'{n} {subDate} {subPN} H:      {subBetrag}')
        resultS  = line.find(' S')
        if (resultS >= 0):
            subPN = line[resultPN:resultPN+6]
            subBetrag = line[resultPN+7:resultS]
            subDate = line[0:6]
            subA = subBetrag.replace('.','')
            subB = subA.replace(',','.')
            sumS = sumS + float(subB)
            print(f'{n} {subDate} {subPN} S: {subBetrag}')
    resultAK = line.find('alter Kontostand')
    resultNK = line.find('neuer Kontostand')
print("Result: S %6.2f, H %6.2f, diff %6.2f" % (sumS,sumH,sumH-sumS))
print("---------------")

#read
# myFile.read([n])
# myFile.readline([n])
# myFile.readlines()


#write
# myFile.write("Hello \n")
# myFile.writelines(L)

myFile.close()
