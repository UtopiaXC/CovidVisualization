# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

FileConfirmed=open('source/GlobalConfirm.csv', 'r')
lines_confirm=FileConfirmed.readlines()
lines_confirm.pop(0)

FileRecovered=open('source/GlobalRecovered.csv', 'r')
lines_recovered=FileRecovered.readlines()
lines_recovered.pop(0)

FileDeath=open('source/GlobalDeath.csv', 'r')
lines_death=FileDeath.readlines()
lines_death.pop(0)



XChina=[]
YChina=[]
XAmecria=[]
YAmecria=[]
XIran=[]
YIran=[]
XItaly=[]
YItaly=[]
XSpain=[]
YSpain=[]
XGermany=[]
YGermany=[]
XFrance=[]
YFrance=[]
XUK=[]
YUK=[]


for i in range(4,94,1):
    XChina.append(i)
    XAmecria.append(i)
    XIran.append(i)
    XItaly.append(i)
    XSpain.append(i)
    XGermany.append(i)
    XFrance.append(i)
    XUK.append(i)
    valueChina=0
    valueAmerica=0
    valueItaly=0
    valueIran=0
    valueSpain=0
    valueGermany=0
    valueFrance=0
    valueUK=0
    dvalueChina = 0
    dvalueAmerica = 0
    dvalueItaly = 0
    dvalueIran = 0
    dvalueSpain = 0
    dvalueGermany = 0
    dvalueFrance = 0
    dvalueUK = 0

    for line in lines_confirm:
        lineMessage=line.split(',')
        if  lineMessage[1]=='China':
            valueChina += int(lineMessage[i])
        if lineMessage[1]=='US':
            valueAmerica += int(lineMessage[i])
        if lineMessage[1] == 'Iran':
            valueIran += int(lineMessage[i])
        if lineMessage[1] == 'Italy':
            valueItaly += int(lineMessage[i])
        if lineMessage[1] == 'Spain':
            valueSpain+= int(lineMessage[i])
        if lineMessage[1] == 'Germany':
            valueGermany += int(lineMessage[i])
        if lineMessage[1] == 'France':
            valueFrance += int(lineMessage[i])
        if lineMessage[1] == 'United Kingdom':
            valueUK += int(lineMessage[i])

    for line in lines_death:
        lineMessage = line.split(',')
        if lineMessage[1] == 'China':
            dvalueChina += int(lineMessage[i])
        if lineMessage[1] == 'US':
            dvalueAmerica += int(lineMessage[i])
        if lineMessage[1] == 'Iran':
            dvalueIran += int(lineMessage[i])
        if lineMessage[1] == 'Italy':
            dvalueItaly += int(lineMessage[i])
        if lineMessage[1] == 'Spain':
            dvalueSpain += int(lineMessage[i])
        if lineMessage[1] == 'Germany':
            dvalueGermany += int(lineMessage[i])
        if lineMessage[1] == 'France':
            dvalueFrance += int(lineMessage[i])
        if lineMessage[1] == 'United Kingdom':
            dvalueUK += int(lineMessage[i])

    for line in lines_recovered:
        lineMessage = line.split(',')
        if lineMessage[1] == 'China':
            dvalueChina += int(lineMessage[i])
        if lineMessage[1] == 'US':
            dvalueAmerica += int(lineMessage[i])
        if lineMessage[1] == 'Iran':
            dvalueIran += int(lineMessage[i])
        if lineMessage[1] == 'Italy':
            dvalueItaly += int(lineMessage[i])
        if lineMessage[1] == 'Spain':
            dvalueSpain += int(lineMessage[i])
        if lineMessage[1] == 'Germany':
            dvalueGermany += int(lineMessage[i])
        if lineMessage[1] == 'France':
            dvalueFrance += int(lineMessage[i])
        if lineMessage[1] == 'United Kingdom':
            dvalueUK += int(lineMessage[i])

    YChina.append(valueChina-dvalueChina)
    YAmecria.append(valueAmerica-dvalueAmerica)
    YIran.append(valueIran-dvalueIran)
    YItaly.append(valueItaly - dvalueItaly)
    YSpain.append(valueSpain - dvalueSpain)
    YGermany.append(valueGermany - dvalueGermany)
    YFrance.append(valueFrance - dvalueFrance)
    YUK.append(valueUK - dvalueUK)






x=np.arange(0,100)

plt.plot(XChina,YChina,label='China')
plt.plot(XAmecria,YAmecria,label='America')
plt.plot(XIran,YIran,label='Iran')
plt.plot(XItaly,YItaly,label='Italy')
plt.plot(XSpain,YSpain,label='Spain')
plt.plot(XGermany,YGermany,label='Germany')
plt.plot(XFrance,YFrance,label='France')
plt.plot(XUK,YUK,label='United Kingdom')


plt.title('Global Net Confirmed')
plt.xlabel('Days')
plt.ylabel('Net Confirmed')
plt.legend()
plt.savefig('plt/GlobalNetConfirm.png',dpi=300)
plt.show()

plt.plot(XChina,YChina,label='China')
plt.plot(XAmecria,YAmecria,label='America')
plt.plot(XIran,YIran,label='Iran')
plt.plot(XItaly,YItaly,label='Italy')
plt.plot(XSpain,YSpain,label='Spain')
plt.plot(XGermany,YGermany,label='Germany')
plt.plot(XFrance,YFrance,label='France')
plt.plot(XUK,YUK,label='United Kingdom')


plt.title('Global Net Confirmed As Log')
plt.xlabel('Days')
plt.ylabel('Net Confirmed')
plt.legend()
plt.semilogy()
plt.savefig('plt/GlobalNetConfirmForLog.png',dpi=300)
plt.show()


