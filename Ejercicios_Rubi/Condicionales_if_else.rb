# Condición simple
a = 2
if a == 2
  puts "A es igual a 2"
else
  puts "A es diferente de 2"
end

# Condiciones combinadas

Nombre = "Esteban"
Edad = 27
Pais = "Colombia"

# Usamos elsif para concatenar las condiciones

if Nombre == 'Esteban' and Edad == 27 and Pais == 'Colombia'
  puts "Su nombre es #{Nombre}, tiene #{Edad} y es de #{Pais}"
elsif Nombre == 'Esteban' and not Edad == 27
  puts "Su nombre es #{Nombre}, pero no tiene 28 años"
elsif Nombre != 'Esteban' and Edad == 27
  puts "Su nombre no es #{Nombre}, pero tiene 28 años"
else
  puts "No se llama Esteban ni tiene 27 años"
end

