# Ley de Ohm
# V=I×R para hayar el voltaje
puts "Ingrese el valor del voltaje del circuito: "
voltaje = gets.chomp.to_f #.to_f para datos flotantes
puts "Ingrese el valor de la resistencia del circuito: "
resistencia = gets.chomp.to_f #.chomp para que el dato ingresado no genere salto de linea al ser utilizado
intensidad = (voltaje/resistencia) #Intesidad entiendase por amperaje
print"Al conectar un resistor de #{resistencia} ohm, a una fuente de #{voltaje} V el voltage circulara una corriente de #{intensidad} amperios"
# V es el voltaje (en voltios, V)
# I es la corriente (en amperios, A)
# R es la resistencia (en ohmios, Ω)