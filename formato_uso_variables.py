miEdad= 39
print(f"Yo tengo {miEdad} años")

#print("hola mundo")

#paso 1: pedir la edad de la persona numero 1
edadPersona1 = int( input("Por favor, ingrese la edad de la primera persona:"))

#paso 2: pedir la edad de la persona numero 2
edadPersona2 = int(input("Por favor, ingrese la edad de la segunda persona:"))

#paso 3: calcular la diferencia en las edades
diferenciaDeEdad =(edadPersona1) - (edadPersona2)

#paso 4: imprimir la diferencia en las edades // dar formato con f "y dentro de comillas string y variables anidadas con resultado"
print(f'La diferencia en las edades es de {diferenciaDeEdad} años')

VariablePascalCase= "Todas las variables inicial de palabras va en mayúsculas"
camelCase= "Primera palabra en minúscula y las demás en mayúsculas"
variable_snake_case= "Palabra guion bajo y palabra"

valorFactura=int(input("Ingrese el valor de la factura"))
iva=(valorFactura* 19) / 100 
propina=(valorFactura*10) / 100
factura_Total= valorFactura + iva + propina

print(valorFactura)
print(iva)
print(propina)
print(factura_Total)

# convertir de°C a °F

centigrados= int(input("Ingrese su medida en °C"))
fahrenheit= (centigrados*9/5) + 32
print(f"Son {fahrenheit}°F ")

# convertir °F a °C

fahrenheit= int(input("Ingrese los grados fahrenheit a convertir"))
centigrados= (fahrenheit-32)*5/9 
print(f"Son {centigrados}°C")

# operaciones aritméticas avanzadas

suma= 43+27
resta= 83 -12
multiplicacion= 98*2
division= 58 /45
division_entera= 88 //54
modulo_residuo= 15%3
potenciacion=(25**2)
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo_residuo)
print(potenciacion)

#IMC
peso=float(input("ingrese su peso en kg"))
estatura=int(input("ingrese su estatura en cms"))
imc= (peso / estatura) **2
print(f("Tu indice de masa corporal es {imc} kg/cms2"))

if imc > 0  and imc < 18.5:
    print("Su peso es inferior al normal")
elif imc <= 24.9:
    print("Su peso es normal")
elif imc <= 29.9:
    print("Usted tiene sobrepeso")
else:
    print("Usted esta en obesidad")


# Calcular la utilidad bruta

ingresos=int("Digite sus ingresos ")
costos=int("Digite los costos")
impuesto= (ingresos *30) / 100 
utilidad_Bruta= ingresos - impuesto - costos 

print(f"La utilidad bruta en su trabajo fue de {utilidad_Bruta}")

