# import time
import tkinter as tk 
from tkinter import StringVar
from tkinter import messagebox
preguntas = [

    {
        "pregunta": "¿Qué sistema del cuerpo humano es responsable de transportar oxígeno y nutrientes a través del cuerpo y eliminar los productos de desecho?",
        "respuestas": [
            "Sistema nervioso central",
            "Sistema circulatorio",
            "Sistema digestivo",
            "Sistema respiratorio"
        ],
        "respuesta correcta": "Sistema circulatorio"
    },

    {
        "pregunta": "¿Cómo se llama el proceso en el que los músculos se contraen y se acortan, permitiendo el movimiento del cuerpo?",
        "respuestas": [
            "Respiración",
            "Digestión",
            "Contracción muscular",
            "Difusión"
        ],
        "respuesta correcta": "Contracción muscular"
    },

    {
        "pregunta": "¿Qué órgano del sistema digestivo es responsable de absorber los nutrientes de los alimentos y enviarlos al torrente sanguíneo?",
        "respuestas": [
            "Estómago",
            "Intestino delgado",
            "Intestino grueso",
            "Hígado"
        ],
        "respuesta correcta": "Intestino delgado"
    },

    {
        "pregunta": "¿Cómo se llama el proceso por el cual los nutrientes y los productos de desecho son intercambiados entre el torrente sanguíneo y las células del cuerpo?",
        "respuestas": [
            "Circulación",
            "Difusión",
            "Osmosis",
            "Endocitosis"
        ],
        "respuesta correcta": "Difusión"
    },

    {
        "pregunta": "¿Qué es el tejido epitelial y dónde se encuentra en el cuerpo humano?",
        "respuestas": [
            "Un tejido que forma los huesos del cuerpo",
            "Un tejido que reviste las cavidades del cuerpo y las superficies de los órganos",
            "Un tejido que conecta los músculos a los huesos",
            "Un tejido que se encuentra en el cerebro y la médula espinal"
        ],
        "respuesta correcta": "Un tejido que reviste las cavidades del cuerpo y las superficies de los órganos"
    },
    
    {
        "pregunta": "¿Cómo se llama el sistema de órganos que es responsable de producir hormonas y regular las funciones corporales?",
        "respuestas": [
            "Sistema endocrino",
            " Sistema nervioso",
            "Sistema inmunológico",
            "Sistema digestivo"
        ],
        "respuesta correcta": "Sistema endocrino"
    }
]

class Trivia_Game:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.index_pregunta = 0
        self.puntaje = 0

        self.root = tk.Tk()
        self.root.title('Morfo Trivia Game')

        self.pregunta_label = tk.Label(self.root, text='', font=("Arial", 14))
        self.pregunta_label.pack(pady=10)

        self.opcion_var = StringVar()
        self.opcion_buttons = []

        for i in range(4):
            opcion_button = tk.Radiobutton(self.root, text='', variable=self.opcion_var, value=i, font=("Arial", 10))
            opcion_button.pack(pady=5)
            self.opcion_buttons.append(opcion_button)

        self.sig_button = tk.Button(self.root, text='Siguiente', command=self.siguiente_pregunta)
        self.sig_button.pack(pady=5)

        self.show_pregunta()
        self.root.mainloop()

    def show_pregunta(self):
        pregunta = self.preguntas[self.index_pregunta]
        self.pregunta_label.configure(text=pregunta['pregunta'])

        opciones = pregunta['respuestas']
        for i in range(len(opciones)):
            self.opcion_buttons[i].configure(text=opciones[i], value=opciones[i])

    def siguiente_pregunta(self):
        print(self.index_pregunta)
        self.check_respuesta()
        self.index_pregunta += 1


        if self.index_pregunta < len(self.preguntas):
            self.show_pregunta()
        else:
            messagebox.showinfo("Morfo Trivia Game", f"Game Over \nTu puntaje es: {self.puntaje}/{len(self.preguntas)}")        
            self.root.quit()

    def check_respuesta(self):
        respuesta = self.opcion_var.get()
        pregunta = self.preguntas[self.index_pregunta]
        respuesta_correcta = pregunta["respuesta correcta"]

        if respuesta == respuesta_correcta:
            self.puntaje += 1
        
        

game = Trivia_Game(preguntas)





# puntuacion = 0
# tiempo = time.time()



# for pregunta in preguntas:
#     print(pregunta["pregunta"])
    
#     for i, respuesta in enumerate(pregunta["respuestas"]):
#         print(f"{i + 1}. {respuesta}")

#     respuesta_usuario = input("Escribe el número de la respuesta correcta: ")

#     if pregunta["respuestas"][int(respuesta_usuario) - 1] == pregunta["respuesta correcta"]:
#         print("¡Respuesta correcta!")
#         puntuacion += 1

#     else:
#         print(f"Respuesta incorrecta. La respuesta correcta es {pregunta['respuesta correcta']}.")
        

# tiempo = time.time() - tiempo
# tiempo = tiempo/60

# print(f"Tu tiempo fue de {tiempo} minutos")
# print(f"Tu puntuación final es {puntuacion} de {len(preguntas)} preguntas.")