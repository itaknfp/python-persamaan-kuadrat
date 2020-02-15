import math
print("mencari x1 dan x2 dalam persamaan kuadrat ax2 + bx + c = 0 dengan rumus ABC")

konsta = int(input('Masukkan variabel a: '))
konstb = int(input('Masukkan variabel b: '))
konstc = int(input('Masukkan koefisien c: '))

dis = (konstb**2) - (4*konsta*konstc)
print ('nilai diskriminan= ',dis)
if dis<0:
    print ('Akar Imaginer')
elif dis==0:
    x=-konstb/2*konsta
    print ('Akar kembar= ',x)
else:
    x1=(-konstb+math.sqrt(dis))/2*konsta
    x2=(-konstb-math.sqrt(dis))/2*konsta
    print ('hasil x1 = ',x1,'dan hasil x2 = ',x2)
