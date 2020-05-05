#alles bij elkaar doen 123
import time
alle_getallen = list(range(1, 5))
print(alle_getallen)
print('dit was een testje, next \n')

def startding():
    keuze = str(input('kies a voor printen, enige optie mogenlijk lol\n'))
    if keuze == 'a':
        printen()
    elif keuze == 'b':
        testscriptje()

def printen():
	alle_getallen=list(range(0, int(input("tot welk getal? \n"))))
	alle_getallen = int(alle_getallen)
	print("printingg")
	for i in alle_getallen:
		print(str(i))
		time.sleep(0.1)
	printen()
startding()

def testscriptje():
	getal = int(input("kies getal"))
	range_ding = list(range(0, getal))
	print(range_ding)
