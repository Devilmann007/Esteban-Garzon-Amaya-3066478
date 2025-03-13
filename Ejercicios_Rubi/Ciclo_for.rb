puts "Ingrese el primer valor"
A = gets.to_i 
puts "Ingrese el segundo valor"
B = gets.to_i
for i in 1..5
  valor = A ** B
  puts "Iteracion #{i}: La potencia de #{A} sobre #{B} es igual a: #{valor}"
end