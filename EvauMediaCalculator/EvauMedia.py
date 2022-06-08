import tkinter as tk
from tkinter import Canvas, Toplevel, filedialog, Text    
import os

from pyparsing import common_html_entity

root = tk.Tk()

def ciencias():
    nuevaventanauno = tk.Toplevel(root)

    canvas = tk.Canvas(nuevaventanauno, height=600, width=200, bg="#A9EFFE")
    canvas.pack()

    frame = tk.Frame(nuevaventanauno, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Texto2 = tk.Label(frame,text="Inserta tus notas:")
    Texto2.pack()

    MatesTEXTO = tk.Label(frame,text="Matemáticas")
    MatesTEXTO.pack()

    matematicas = tk.Entry(frame)
    matematicas.pack()

    LenguaTEXTOCiencias = tk.Label(frame,text="Lengua")
    LenguaTEXTOCiencias.pack()

    LenguaCiencias = tk.Entry(frame)
    LenguaCiencias.pack()

    FilosofiaCienciasTEXTO = tk.Label(frame,text="Filosofía")
    FilosofiaCienciasTEXTO.pack()

    FilosofiaCiencias = tk.Entry(frame)
    FilosofiaCiencias.pack()

    InglesCienciasTEXTO = tk.Label(frame,text="Ingles")
    InglesCienciasTEXTO.pack()

    InglesCiencias = tk.Entry(frame)
    InglesCiencias.pack()

    EducaCienciasTEXTO = tk.Label(frame,text="Educacion Fisica")
    EducaCienciasTEXTO.pack()

    EducaCiencias = tk.Entry(frame)
    EducaCiencias.pack()

    FisicaTEXTO = tk.Label(frame,text="Fisica y Quimica")
    FisicaTEXTO.pack()

    Fisica = tk.Entry(frame)
    Fisica.pack()

    DibujoBioTEXTO = tk.Label(frame,text="Dibujo y biologia")
    DibujoBioTEXTO.pack()

    DibujoBio = tk.Entry(frame)
    DibujoBio.pack()

    Optativa1TEXTO = tk.Label(frame,text="Optativa 1")
    Optativa1TEXTO.pack()

    Optativa1 = tk.Entry(frame)
    Optativa1.pack()

    Optativa2TEXTO = tk.Label(frame,text="Optativa 1")
    Optativa2TEXTO.pack()

    Optativa2 = tk.Entry(frame)
    Optativa2.pack()

    def Calculo():
        canvas = tk.Canvas(nuevaventanauno, height=400, width=200, bg="#A9EFFE")
        canvas.pack()

        frame = tk.Frame(nuevaventanauno, bg="white")
        frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        NotaMates = int(matematicas.get())
        NotaLengua = int(LenguaCiencias.get())
        NotaFilo = int(FilosofiaCiencias.get())
        NotaIngles = int(InglesCiencias.get())
        NotaEduca = int(EducaCiencias.get())
        NotaFYQ = int(Fisica.get())
        NotaDibujoBig = int(DibujoBio.get())
        NotaOptativa1 = int(Optativa1.get())
        NotaOptativa2 = int(Optativa2.get())

        Suma = (NotaDibujoBig + NotaEduca + NotaFilo + NotaFYQ + NotaIngles + NotaLengua + NotaMates + NotaOptativa1 + NotaOptativa2)
        Media = Suma/9
        NotaEvau = Media*0.3

        StringMedia = "Tu nota media actual es " + str(Media)
        StringNotaEvau = "Tu nota actual en la Evau es" + str(NotaEvau)

        MediaFinal = tk.Label(frame,text=StringMedia)
        MediaFinal.pack()

        EvauFinal = tk.Label(frame, text=StringNotaEvau)
        EvauFinal.pack()

    Calcular = tk.Button(frame, text="Calcular",command=Calculo)
    Calcular.pack()



def NotaActualFuncion():
    nuevaventana = tk.Toplevel(root)
    
    def Primero():
            canvas = tk.Canvas(nuevaventana, height=200, width=200, bg="#A9EFFE")
            canvas.pack()

            frame = tk.Frame(nuevaventana, bg="white")
            frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

            Texto2 = tk.Label(frame,text="¿Que modalidad de Bachillerato?")
            Texto2.pack()

            PrimeroDeBachillerato = tk.Button(frame, text= "Ciencias",command=ciencias)
            PrimeroDeBachillerato.pack()

            PrimeroDeBachillerato = tk.Button(frame, text= "Sociales",command=Primero)
            PrimeroDeBachillerato.pack()

            PrimeroDeBachillerato = tk.Button(frame, text= "Humanidades",command=Primero)
            PrimeroDeBachillerato.pack()
    
    canvas = tk.Canvas(nuevaventana, height=200, width=200, bg="#A9EFFE")
    canvas.pack()

    frame = tk.Frame(nuevaventana, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    Texto1 = tk.Label(frame,text="¿Que curso de bachillerato estas?")

    PrimeroDeBachillerato = tk.Button(frame, text= "Primero De Bachillerato",command=Primero)
    PrimeroDeBachillerato.pack()

    SegundoDeBachillerato = tk.Button(frame, text="Segundo De Bachillerato", )
    SegundoDeBachillerato.pack()
  
canvas = tk.Canvas(root, height=200, width=200, bg="#A9EFFE")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

NotaActual = tk.Button(frame, text= "Nota Actual Evau",command=NotaActualFuncion )
NotaActual.pack()

NotaHipotetica = tk.Button(frame, text="Nota hipotetica Evau")
NotaHipotetica.pack()

root.mainloop()
