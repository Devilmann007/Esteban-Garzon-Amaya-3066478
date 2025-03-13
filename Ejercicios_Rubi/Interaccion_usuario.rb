puts "Escriba sus nombres completos: "
a = gets.chomp
puts "Escribas sus Apellidos completos: "
b = gets.chomp
puts "Escriba su profesion: "
c = gets.chomp
puts "Escriba su año de nacimiento: "
d = gets.to_i # no agregamos .chomp por que no es un dato que vayamos a imprimir
#Calculamos la edad
e = (2025-d)
print "El (La) #{c}, #{a} #{b}, tiene #{e} años"
# En Rubi puts genera automaticamente salto de linea al final de la impresion para evitar esto podemos usar print
# gets genera automaticamente salto de linea en el dato ingresado, usar gets.chomp