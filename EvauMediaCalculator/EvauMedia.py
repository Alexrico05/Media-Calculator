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

    def Calculo():
        canvas = tk.Canvas(nuevaventanauno, height=400, width=200, bg="#A9EFFE")
        canvas.pack()

        frame = tk.Frame(nuevaventanauno, bg="white")
        frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        StringMedia = "Tu nota media actual es" + str(Media)
        StringNotaEvau = "Tu nota actual en la Evau es" + str(NotaEvau)

        MediaFinal = tk.Label(frame,text=StringMedia)
        MediaFinal.pack()

        EvauFinal = tk.Label(frame, text=StringNotaEvau)
        EvauFinal.pack()

    Texto2 = tk.Label(frame,text="Inserta tus notas:")
    Texto2.pack()

@@ -88,23 +72,41 @@ def Calculo():
    Optativa2 = tk.Entry(frame)
    Optativa2.pack()

    NotaMates = int(matematicas)
    NotaLengua = int(LenguaCiencias)
    NotaFilo = int(FilosofiaCiencias)
    NotaIngles = int(InglesCiencias)
    NotaEduca = int(EducaCiencias)
    NotaFYQ = int(Fisica)
    NotaDibujoBig = int(DibujoBio)
    NotaOptativa1 = int(Optativa1)
    NotaOptativa2 = int(Optativa2)

    Suma = (NotaDibujoBig + NotaEduca + NotaFilo + NotaFYQ + NotaIngles +NotaLengua + NotaMates + NotaOptativa1 +NotaOptativa2)
    Media = int(Suma)/9
    NotaEvau = int(Media)*0,3

    Calcular = tk.Button(frame, text= "Calcular",command=Calculo)
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
