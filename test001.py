# imports
import time
import platform
print(platform.python_version())

# Array: Matrix 11*10 + 4 Minutes
MatrixColumns = 11
MatrixRows = 10
MatrixMinutes = 4
# mask = [0]*(MatrixColumns*MatrixRows+MatrixMinutes)

# 0 ESKISTEFUNF
# 1 ZEHNZWANZIG
# 2 DREIVIERTEL
# 3 VORNEUMNACH
# 4 HALBXELFUNF
# 5 EINSTAGZWEI
# 6 DREISTZWOLF
# 7 SIEBENZVIER
# 8 NACHTASECHS
# 9 ZEHNEUNKUHR


def RowOffset (x):
    return x*MatrixColumns
def MatrixElt(x,y):
    return(x+y*MatrixColumns)

# functions for setting LED mask (0=LED off, 1=LED on)
def ES(mask):
    mask[0+RowOffset(0)]=mask[1+RowOffset(0)]=1 # 0

def IST(mask,x=0):
    if(x==0):
        lineNum = 0
        mask[3+RowOffset(0)]=mask[4+RowOffset(0)]=mask[5+RowOffset(0)]=1 #0
    else:
        mask[3+RowOffset(6)]=mask[4+RowOffset(6)]=mask[5+RowOffset(6)]=1 #6

def FUNF(mask,x=0):
    if(x==0):
        mask[7+RowOffset(0)]=mask[8+RowOffset(0)]=mask[9+RowOffset(0)]=mask[10+RowOffset(0)]=1 #0
    else:
        mask[7+RowOffset(5)]=mask[8+RowOffset(5)]=mask[9+RowOffset(5)]=mask[10+RowOffset(5)]=1 #5

def ZEHN(mask,x=0):
    if(x==0):
        mask[0+RowOffset(1)]=mask[1+RowOffset(1)]=mask[2+RowOffset(1)]=mask[3+RowOffset(1)]=1 #1
    else:
        mask[0+RowOffset(9)]=mask[1+RowOffset(9)]=mask[2+RowOffset(9)]=mask[3+RowOffset(9)]=1 #9

def ZWANZIG(mask):
    mask[4+RowOffset(1)]=mask[5+RowOffset(1)]=mask[6+RowOffset(1)]=mask[7+RowOffset(1)]=mask[8+RowOffset(1)]=mask[9+RowOffset(1)]=mask[10+RowOffset(1)]=1 #1

def DREI(mask,x=0):
    if(x==0):
        mask[0+RowOffset(2)]=mask[1+RowOffset(2)]=mask[2+RowOffset(2)]=mask[3+RowOffset(2)]=1 #2
    else:
        mask[0+RowOffset(6)]=mask[1+RowOffset(6)]=mask[2+RowOffset(6)]=mask[3+RowOffset(6)]=1 #6

def VIER(mask,x=0):
    if(x==0):
        mask[4+RowOffset(2)]=mask[5+RowOffset(2)]=mask[6+RowOffset(2)]=mask[7+RowOffset(2)]=1 #2
    else:
        mask[7+RowOffset(7)]=mask[8+RowOffset(7)]=mask[9+RowOffset(7)]=mask[10+RowOffset(7)]=1 #7

def DREIVIERTEL(mask):
    mask[0+RowOffset(2)]=mask[1+RowOffset(2)]=mask[2+RowOffset(2)]=mask[3+RowOffset(2)]=mask[4+RowOffset(2)]=mask[5+RowOffset(2)]=mask[6+RowOffset(2)]=mask[7+RowOffset(2)]=mask[8+RowOffset(2)]=mask[9+RowOffset(2)]=mask[10+RowOffset(2)]=1 #2

def VIERTEL(mask):
    mask[4+RowOffset(2)]=mask[5+RowOffset(2)]=mask[6+RowOffset(2)]=mask[7+RowOffset(2)]=mask[8+RowOffset(2)]=mask[9+RowOffset(2)]=mask[10+RowOffset(2)]=1 #2

def VOR(mask):
    mask[0+RowOffset(3)]=mask[1+RowOffset(3)]=mask[2+RowOffset(3)]=1 #3

def AUS(mask):
    mask[3+RowOffset(3)]=mask[4+RowOffset(3)]=mask[5+RowOffset(3)]=1 #3

def NACH(mask,x=0):
    if(x==0):
        mask[7+RowOffset(3)]=mask[8+RowOffset(3)]=mask[9+RowOffset(3)]=mask[10+RowOffset(3)]=1 #3
    else:
        mask[0+RowOffset(8)]=mask[1+RowOffset(8)]=mask[2+RowOffset(8)]=mask[3+RowOffset(8)]=1 #8

def HALB(mask):
    mask[0+RowOffset(4)]=mask[1+RowOffset(4)]=mask[2+RowOffset(4)]=mask[3+RowOffset(4)]=1 #4

def ELF(mask):
    mask[5+RowOffset(4)]=mask[6+RowOffset(4)]=mask[7+RowOffset(4)]=1 #4

def EIN(mask):
    mask[0+RowOffset(5)]=mask[1+RowOffset(5)]=mask[2+RowOffset(5)]=1 #5

def EINS(mask):
    mask[0+RowOffset(5)]=mask[1+RowOffset(5)]=mask[2+RowOffset(5)]=mask[3+RowOffset(5)]=1 #5

def TAG(mask):
    mask[4+RowOffset(5)]=mask[5+RowOffset(5)]=mask[6+RowOffset(5)]=1 #5

def ZWEI(mask):
    mask[7+RowOffset(5)]=mask[8+RowOffset(5)]=mask[9+RowOffset(5)]=mask[10+RowOffset(5)]=1 #5

def ZWOLF(mask):
    mask[6+RowOffset(6)]=mask[7+RowOffset(6)]=mask[8+RowOffset(6)]=mask[9+RowOffset(6)]=mask[10+RowOffset(6)]=1 #6

def SIEBEN(mask):
    mask[0+RowOffset(7)]=mask[1+RowOffset(7)]=mask[2+RowOffset(7)]=mask[3+RowOffset(7)]=mask[4+RowOffset(7)]=mask[5+RowOffset(7)]=1 #7

def NACHT(mask):
    mask[0+RowOffset(8)]=mask[1+RowOffset(8)]=mask[2+RowOffset(8)]=mask[3+RowOffset(8)]=mask[4+RowOffset(8)]=1 #8

def ACHT(mask):
    mask[1+RowOffset(8)]=mask[2+RowOffset(8)]=mask[3+RowOffset(8)]=mask[4+RowOffset(8)]=1 #8

def SECHS(mask):
    mask[6+RowOffset(8)]=mask[7+RowOffset(8)]=mask[8+RowOffset(8)]=mask[9+RowOffset(8)]=mask[10+RowOffset(8)]=1 #8

def NEUN(mask):
    mask[3+RowOffset(9)]=mask[4+RowOffset(9)]=mask[5+RowOffset(9)]=mask[6+RowOffset(9)]=1 #9

def UHR(mask):
    mask[8+RowOffset(9)]=mask[9+RowOffset(9)]=mask[10+RowOffset(9)]=1 #9

def setHourText(mask, h):
	if (h < 100) : # >=100 special cases
		h %= 12
        if(h==0 or h==12):
            ZWOLF(mask)
        elif (h==1):
            EINS(mask)
        elif (h==2):
            ZWEI(mask)
        elif (h==3):
            DREI(mask)
        elif (h==4):
            VIER(mask)
        elif (h==5):
            FUNF(mask)
        elif (h==6):
            SECHS(mask)
        elif (h==7):
            SIEBEN(mask)
        elif (h==8):
            ACHT(mask)
        elif (h==9):
            NEUN(mask)
        elif (h==10):
            ZEHN(mask)
        elif (h==11):
            ELF(mask)
	# special cases
	if (h==100):
		EIN(mask)

def setMaskFromTime():
    newMask = [0]*(MatrixColumns*MatrixRows+MatrixMinutes)
        
    # ES IST always
    ES(newMask)
    IST(newMask)

    curtime=time.localtime()
    minutes = curtime.tm_min
    hours = curtime.tm_hour

    if(minutes < 5):
        setHourText(newMask,100 if (hours == 1) else hours) # ESs IST EIN UHR - nicht EINS UHR
        UHR(newMask)
    elif(minutes < 10):
        FUNF(newMask)
        NACH(newMask)
        setHourText(newMask,hours) 
    elif(minutes < 15):
        ZEHN(newMask)
        NACH(newMask)
        setHourText(newMask,hours) 
    elif(minutes < 20):
        VIERTEL(newMask)
        NACH(newMask)
        setHourText(newMask,hours) 
    elif(minutes < 25):
        ZWANZIG(newMask)
        NACH(newMask)
        setHourText(newMask,hours) 
        # ZEHN(newMask)
        # VOR(newMask)
        # HALB(newMask)
        setHourText(newMask,hours+1) 
    elif(minutes < 30):
        FUNF(newMask)
        VOR(newMask)
        HALB(newMask)
        setHourText(newMask,hours+1)
    elif(minutes < 35):
        HALB(newMask)
        setHourText(newMask,hours+1)
    elif(minutes < 40):
        FUNF(newMask)
        NACH(newMask)
        HALB(newMask)
        setHourText(newMask,hours+1)
    elif(minutes < 45):
        # ZEHN(newMask)
        # NACH(newMask)
        # HALB(newMask)
        ZWANZIG(newMask)
        VOR(newMask)
        setHourText(newMask,hours+1)
    elif(minutes < 50):
        VIERTEL(newMask)
        VOR(newMask)
        #DREIVIERTEL(newMask)
        setHourText(newMask,hours+1)
    elif(minutes < 55):
        ZEHN(newMask)
        VOR(newMask)
        setHourText(newMask,hours+1)
    else:
        FUNF(newMask)
        VOR(newMask)
        setHourText(newMask,hours+1)

    return newMask
#

def D_printMatrix(mask):
    for i in range(0,MatrixRows):
        for j in range(0,MatrixColumns):
            print(mask[MatrixElt(j,i)])

D_printMatrix(setMaskFromTime())

