#Tarea perfil de usuario - Flavia Aray

#Se pregunta el nombre verificando que esté en mayusculas
#y se saluda de acuerdo a la respuesta
nombre = input("¿Cuál es tu nombre? ")
if nombre[1] == ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'):
    print("¡Hola", nombre, "!")
else: 
    input("Por favor escriba su nombre empezando con mayúscula")

#Se pregunta el sexo y se saluda de acuerdo a la respuesta
sexo = input("¿Cuál es tu sexo? (M o F) ")

if sexo == "M":
    print("Hola, amigo!")
elif sexo == "F":
    print("Hola, amiga!")
else:
    input("Por favor escriba M o F")

#Se pregunta la región y se respnde con un mensaje
region = input("¿De qué región eres? (America, Europa o Asia) ")
print("¡ Me encanta", region, "!")

#Se pregunta lo favorito de esta region
favorito = print("¿Cuál es tu cosa preferida de la región? ")
if region == "America":
    input("¿Prefieres su comida, sus paisajes o su música? ")
elif region == "Europa":
    input("¡Prefieres su gastronomia, sus vinos o sus templos !")
else:
    input("¿Prefieres su tecnología, su moda o su comida? ")
    