tc='wrong choice'
a=0
z=eval(input('1 for bike,2 for auto,3 for ecocar,4 for suv,5 for luxury . enter your choice:'))
b=eval(input('enter starting kilometer:'))
c=eval(input('enter ending kilometer:'))
d=eval(input('1 for AC, 2 for non AC, enter ur choice :'))
x=c-b
if z==1:
   a=x*5
   print('you travelled in bike\n')
   print('travel cost is Rs.5 per km')
   f=int(input('enter no of shares    :'))
if z==2:
   a=x*8
   print('you travelled in auto\n')
   print('travel cost is Rs.8 per km')
   f=int(input('enter no of shares    :'))
if z==3:
   a=x*12
   print('you travelled in economical car\n')
   print('travel cost is Rs.12 per km')
   f=int(input('enter no of shares    :'))
if z==4:
   a=x*15
   print('you travelled in SUV\n')
   print('travel cost is Rs.15 per km')
   f=int(input('enter no of shares    :'))
if z==5:
    a=x*20
    print('you travelled in luxury car\n')
    print('travel cost is Rs.20 per km')
    f=int(input('enter no of shares   :'))

print('distance travelled     :',x,'kms')
print('basic travel cost is Rs:',a)

if d==1:
    e=a*0.1
    print('charge for AC is     Rs;',e)
if d==2:
    e=0
    print('charge for AC is 0')

tc=a+e
g=tc/f
print('------------------------------------')
print('Total travel cost is Rs:',tc)
print('------------------------------------')
print('Each person share is Rs:',g)
print('------------------------------------')
print('Thanks for Travelling')