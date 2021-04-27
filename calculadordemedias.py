#calcular las medias version alpha 

suma=0.0
print("Hola,¡Vamos a calcular tus medias!")
print("¿Cuantos examenes has tenido?")
n = int(input())
for i in range(n):
    print ("Dame la nota de un examen")
    nota=float(input())
    suma=suma+nota 
media=suma/n
print ("Tu media es ",str(media))

print ("¿Cuanto valen los examenes en esa asignatura?")
porcentaje = float(input())
total=media*(porcentaje/100)
porcentajefinal=total/100
falta=10-total
print ("De momento tienes un ",(total)) 
print ("Para sacar un 10 necesitas en los siguientes items un ",(falta)) 

