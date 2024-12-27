##### TEXTBUTTON RENPY #####
## Contenedor para los botones  
    vbox:  
        xalign 0.1  
        yalign 0.5  
        spacing 15  

## Espaciado entre botones  
        textbutton "Jugar" action Start()  
        textbutton "Cargar" action ShowMenu("load")  
        textbutton "Opciones" action ShowMenu("preferences")  
        textbutton "Acerca de" action ShowMenu("about")  
        textbutton "Ayuda" action ShowMenu("help")  
        textbutton "Salir" action Quit() 



##### IMAGEBUTTON RENPY #####
## Contenedor para los botones  
    vbox:  
        xalign 0.1  
        yalign 0.5  
        spacing 5  

## Espaciado entre botones  
        imagebutton:  
            idle "extra/gui/jugar_idle.png"  
            hover "extra/gui/jugar_hover.png"  
            action Start()  
            hover_sound "audio/boton.mp3"

        imagebutton:  
            idle "extra/gui/cargar_idle.png"  
            hover "extra/gui/cargar_hover.png"  
            action ShowMenu("load")  
            hover_sound "audio/boton.mp3"

        imagebutton:  
            idle "extra/gui/opciones_idle.png"  
            hover "extra/gui/opciones_hover.png"  
            action ShowMenu("preferences")  
            hover_sound "audio/boton.mp3"

        imagebutton:  
            idle "extra/gui/about_idle.png"  
            hover "extra/gui/about_hover.png"  
            action ShowMenu("about")  
            hover_sound "audio/boton.mp3"

        imagebutton:  
            idle "extra/gui/ayuda_idle.png"  
            hover "extra/gui/ayuda_hover.png"  
            action ShowMenu("help")
            hover_sound "audio/boton.mp3"  

        imagebutton:  
            idle "extra/gui/salir_idle.png"  
            hover "extra/gui/salir_hover.png"  
            action Quit()
            hover_sound "audio/boton.mp3"
