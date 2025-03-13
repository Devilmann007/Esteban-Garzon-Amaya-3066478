contador = 0
while contador < 5
  contador += 1
  puts "Iteracion " + contador.to_s # Convierte la variable Contador en una cadena para poder concatenarla con "Iteracion ".
end  # Este 'end' cierra el primer while

contador = 0
while contador < 5
  contador += 1
  puts "Iteracion #{contador}"  # Interpolación de cadenas, más común en Ruby
end  # Este 'end' cierra el segundo while

#En RUBI si la variable comienza con MAYUSCULA la convierte en una constante
#Las variables en RUBI deben comenzar con minuscula

#Combinado con if else
while true 
  puts "Introduzca un valor mayor a 10: "
  #gets reconoce la entrada de valor como string usar gets.to_i para convertir la entrada a un número
  #to_i (para enteros) o to_f (para flotantes) flotante=decimales o reales
  a = gets.to_i #gets traer salto de linea automatico, usar gets.chomp para evitarlo
  if a > 10
    puts "Es correcto"
    break
  else
    puts "Es incorrecto, pruebe de nuevo."
  end
end 