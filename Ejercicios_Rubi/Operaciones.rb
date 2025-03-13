#Operaciones en Rubi
puts "ingrese valor: "
a = gets.chomp.to_i
puts "ingrese valor: "
b = gets.chomp.to_i

suma = (a+b)
puts "la suma de los numeros es: #{suma}"
res = (a-b)
puts "la resta de los numeros es: #{res}"
multi = (a*b)
puts "la multiplicacion de los numeros es: #{multi}"
div = (a/b) 
puts "la division de los numeros es: #{div}"

igual = a == b
if igual
  puts "Los números son iguales: #{a}"
else
  puts "Los números no son iguales: #{a} y #{b}"
end
# Mayor
if a > b
  puts "El número mayor es: #{a}"
else
  puts "El número mayor es: #{b}"
end
# Menor
if b > a
  puts "El número menor es: #{a}"
else
  puts "El número menor es: #{b}"
end