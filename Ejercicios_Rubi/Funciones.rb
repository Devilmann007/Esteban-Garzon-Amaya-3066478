# uso de elementos en dos Arrays diferentes
a=[1,2,3,4,5,]
b=[6,7,8,9,10]
c=[]

for contador in 0..(a.length - 1) #es un rango inclusivo, que va hasta el último índice de a.
  c.push(a[contador]*b[contador])
end
puts c

#Funciones
#En Rubi las funciones son metodos

def saludo
  puts "Hola mundo desde Rubi"
end
saludo 
# Variables dentro del metodo
def multiplicar
  a = 5
  b = 8
  puts (a*b)
end
multiplicar
#Variables fuera del metodo
def multiplicar1(a,b)#convertimos las variables a y b en parametros del metodo
  puts (a*b)
end
a = 5
b = 8
multiplicar1(a,b)
# Devolver los valores con la instruccion return
def multiplicar2
  a = 5
  b = 8
  return a * b
end
resultado = multiplicar2 # Devolvemos la multplicacion y la convertimos en una variable
puts(resultado+5)
#Podemos devolver cualquier tipo de dato, y tratarlo como tal fuera del metodo
def validar_dato(a) # si la variable esta fuera del metodo convertirla en un parametro con ()
  if a==5
      return true
  else
      return false
  end
end  
a = 5
dato = validar_dato(a) # Pasamos `a` como argumento al método
puts dato