#realizar un programa para calcular la diferencia de edad entre 2 personas

edad_persona1= int(input ("Ingrese la edad de la primera persona "))
edad_persona2= int(input("Ingrese la edad de la segunda persona "))

diferencia_Edad= int(edad_persona1-edad_persona2)
print("La diferencia de edad entre las dos personas es: " ,diferencia_Edad)

# realizar un programa que calcule el iva del valor total de una factura con IVA del 19% y un apropina del 10 %

valorFactura=int(input("Ingrese el valor de la factura"))
iva=(valorFactura* 19) / 100
propina=(valorFactura*10) / 100
factura_Total= valorFactura + iva + propina
print(valorFactura)
print(iva)
print(propina)
print(factura_Total)