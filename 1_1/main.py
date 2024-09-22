from tank import Tank

t1 = Tank(x=0, y=0)
t2 = Tank(x=100, y=100, model='T-90М', ammo=80)

print(f'Создано танков: {Tank.count}')

t1.forward()
t1.forward()
t1.right()
t1.fire()

print(t1)