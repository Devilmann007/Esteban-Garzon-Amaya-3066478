puts "selecione la figura a calcular su area: "
puts "1 para rombo"
puts "2 para rectangulo"
puts "3 para cuadrado"
puts "4 para trapecio"
figura= gets.chomp 
Pi=3.1416
Const= 2
case figura #En lugar de match en rubi se utiliza case 
when '1' # Rombo
  puts "ingresa el valor de la diagonal mayor: "
  dmayor = gets.to_f
  puts "ingresa el valor de la diagonal menor: "
  dmenor = gets.to_f
  area = (dmayor*dmenor)/Const
  puts "El area del rombo es: #{area}"
when '2' # Rectangulo
  puts "ingresa el valor del largo del rectangulo: "
  largo = gets.to_f
  puts "ingresa el valor del ancho del rectangulo: "
  ancho = gets.to_f
  area = (largo*ancho)
  puts "El area del rectangulo es: #{area}"
when '3' # Cuadrado
  puts "ingresa el valor del lado del cuadrado: "
  lado = gets.to_f
  area = (lado*lado)
  puts "El area del cuadrado es: #{area}"         
when '4' # Trapecio
  puts "ingresa el valor de la base mayor: "
  bmayor = gets.to_f
  puts "ingresa el valor de la base menor: "
  bmenor = gets.to_f
  puts "ingrese la altura del trapecio: "
  h = gets.to_f
  area = ((bmayor+bmenor)*h)/Const
  puts "El area del trapecio es: #{area}"
else # else para crear una condicion en la que se cierre case
  puts "Opción no válida. Por favor, elija una opción entre 1 y 4."
end