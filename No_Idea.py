#alles bij elkaar doen 123
import time
alle_getallen = list(range(1, 5))
print(alle_getallen)
print('dit was een testje, next \n')

def startding():
    keuze = str(input('kies a voor printen, enige optie mogenlijk lol'))
    if keuze == 'a':
        printen()
    #elif keuze == 'b':
        #not-defined-yet()
#what I'm going to try is alle_getallen+1 but that wont work somehow.
def printen():
	alle_getallen=list(range(0, int(input("tot welk getal? \n"))))
  #alle_getallen = int(alle_getallen)
  #alle_getallen = alle_getallen + 1
	#WAIT I KNOW HOW THIS WORKS
	print("printingg")
	for i in alle_getallen:
		print(str(i))
		time.sleep(0.1)
	printen()
startding()
