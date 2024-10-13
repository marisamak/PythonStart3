from hitbox import Hitbox

#hb2 = Hitbox(500,500,200,100)
#print(hb2)

#hb2.x = 50
#hb2.y = 30
#hb2.width = 200
#hb2.height = 300

#print(hb2)

#w = hb2.get_width() # если классы не приватные
#hb2.set_width(w*-2)
#print(hb2.get_width())
#print(hb2)

hb1 = Hitbox(0, 0, 100, 100)
hb2 = Hitbox(150, 100, 100, 100)
print(f'верхняя граница hb1: {hb1.top}, верхняя граница hb2: {hb2.top}')
print(f'нижняя шраница hb1: {hb1.bottom}, нижняя граница hb2: {hb2.bottom}')
print(f'левая граница hb1: {hb1.left}, левая граница hb2: {hb2.left}')
print(f'правая граница hb1: {hb1.right}, правая граница hb2: {hb2.right}')


intesection = hb1.intersects(hb2)
print(intesection)
