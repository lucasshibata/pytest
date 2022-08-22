from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import *
from random import choice

application.development_mode = False
    
app = Ursina()

window.title = 'A weird place in the matrix'
window.show_ursina_splash = True
window.fullscreen = False
window.borderless = False
window.size = (720, 576)
# window.vsync = True

EditorCamera()

floor = Entity(texture="brick", position=(0, 0, 0), scale=50, collider="plane",
    color=color.rgb(151, 252, 187))

app.run()
