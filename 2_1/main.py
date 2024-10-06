from hitbox import Hitbox

hb2 = Hitbox(500,500,200,100)
print(hb2)

hb2.x = 50
hb2.y = 30
hb2.width = 200
hb2.height = 300

print(hb2)

#w = hb2.get_width() # если классы не приватные
#hb2.set_width(w*-2)
#print(hb2.get_width())
#print(hb2)

