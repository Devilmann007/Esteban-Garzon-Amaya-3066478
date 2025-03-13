nombres = ['Esteban', 'Hans', 'Jhon', 'Juan Pablo']  # Esto es un array

# Usando un bucle 'for' (aunque no es tan común en Ruby)
for nombre in nombres
  puts nombre  # 'puts' para imprimir cada nombre
end

# Para recorrer un array, es más común usar el método 'each'
nombres.each do |nombre|  # 'each' es más idiomático en Ruby
  puts nombre
end
