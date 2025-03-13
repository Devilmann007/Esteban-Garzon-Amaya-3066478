# Diccionario en Ruby con formato literal
auto = {'marca' => 'Ford', 'color' => 'rojo', 'modelo' => 'sedan', 'placa' => 'ROS227'}

# Diccionario en Ruby con símbolos como claves
coche = {:marca => 'Ford', :color => 'rojo', :modelo => 'sedan', :placa => 'ROS227'}

# Imprimimos el elemento de la clave :color en el hash coche
puts coche[:color]  # 'rojo'

# Modificamos el elemento de la clave :color en el hash coche
coche[:color] = "Verde"
# Imprimimos el nuevo valor de la clave :color
puts coche[:color]  # 'Verde'

# Ahora con la marca
puts coche[:marca]  # 'Ford'
coche[:marca] = "Renault"
puts coche[:marca]  # 'Renault'

# Recorrer el diccionario y traer todos los elementos con .each
coche.each do |clave, valor|
  puts "#{clave}: #{valor}"  # Esto imprimirá todos los pares clave-valor del diccionario
end
