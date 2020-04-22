# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

FileConfirmed=open('source/GlobalDeath.csv', 'r')
lines=FileConfirmed.readlines()

head=lines[0].split(',') # index0为省份，1为国家地区，2为纬度，3为经度，后面的都是日期M/D/Y
lines.pop(0)

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
    temptime=head[i].split('/')
    time='2020-'+temptime[0]+'-'+temptime[1]
    XChina.append(i)
    XAmecria.append(i)
    XIran.append(i)
    XItaly.append(i)
    XSpain.append(i)
    XGermany.append(i)
    XFrance.append(i)
    XUK.append(i)
    valueChina=0
    valueFrance=0
    valueUK=0
    for line in lines:
        lineMessage=line.split(',')
        if  lineMessage[1]=='China':
            valueChina+=int(lineMessage[i])
        if lineMessage[1]=='US':
            YAmecria.append(int(lineMessage[i]))
        if lineMessage[1] == 'Iran':
            YIran.append(int(lineMessage[i]))
        if lineMessage[1] == 'Italy':
            YItaly.append(int(lineMessage[i]))
        if lineMessage[1] == 'Spain':
            YSpain.append(int(lineMessage[i]))
        if lineMessage[1] == 'Germany':
            YGermany.append(int(lineMessage[i]))
        if lineMessage[1] == 'France':
            valueFrance += int(lineMessage[i])
        if lineMessage[1] == 'United Kingdom':
            valueUK += int(lineMessage[i])

    YChina.append(valueChina)
    YFrance.append(valueFrance)
    YUK.append(valueUK)

x=np.arange(0,100)

plt.plot(XChina,YChina,label='China')
plt.plot(XAmecria,YAmecria,label='America')
plt.plot(XIran,YIran,label='Iran')
plt.plot(XItaly,YItaly,label='Italy')
plt.plot(XSpain,YSpain,label='Spain')
plt.plot(XGermany,YGermany,label='Germany')
plt.plot(XFrance,YFrance,label='France')
plt.plot(XUK,YUK,label='United Kingdom')


plt.title('Global Death')
plt.xlabel('Days')
plt.ylabel('Death')
plt.legend()
plt.savefig('plt/GlobalDeath.png',dpi=300)
plt.show()

plt.plot(XChina,YChina,label='China')
plt.plot(XAmecria,YAmecria,label='America')
plt.plot(XIran,YIran,label='Iran')
plt.plot(XItaly,YItaly,label='Italy')
plt.plot(XSpain,YSpain,label='Spain')
plt.plot(XGermany,YGermany,label='Germany')
plt.plot(XFrance,YFrance,label='France')
plt.plot(XUK,YUK,label='United Kingdom')


plt.title('Global Death As log')
plt.xlabel('Days')
plt.ylabel('Death')
plt.legend()
plt.semilogy()
plt.savefig('plt/GlobalDeathForLog.png',dpi=300)
plt.show()


