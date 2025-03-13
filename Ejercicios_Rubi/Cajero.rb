# Clase Usuario: Representa a un usuario con nombre, pin y saldo
class Usuario
  # Declaración de los atributos: nombre, pin y saldo
  attr_accessor :nombre, :pin, :saldo
  
  # Método de inicialización de la clase, establece los valores de los atributos
  def initialize(nombre, pin, saldo)
    @nombre = nombre  # Asigna el nombre del usuario
    @pin = pin        # Asigna el pin del usuario
    @saldo = saldo    # Asigna el saldo inicial del usuario
  end
end

# Clase Banco: Representa un banco que tiene una lista de usuarios
class Banco
  # Declaración de los atributos: una lista de usuarios
  attr_accessor :usuarios

  # Método de inicialización que recibe una lista de usuarios
  def initialize(usuarios)
    @usuarios = usuarios  # Asigna la lista de usuarios al banco
  end

  # Método para autenticar a un usuario en base a su nombre y pin
  def autenticar(nombre, pin)
    # Itera sobre la lista de usuarios
    @usuarios.each do |usuario|
      if usuario.nombre == nombre  # Si el nombre coincide
        if usuario.pin == pin     # Si el pin también coincide
          puts "Bienvenido a su banco, #{nombre}."
          return true              # Autenticación exitosa
        else
          puts "Nombre o pin incorrecto, intente de nuevo."
          return false             # Si el pin es incorrecto
        end
      end
    end            
    puts "El usuario no existe."  # Si no se encuentra al usuario con ese nombre
    return false                  # Autenticación fallida
  end

  # Método para realizar una transacción de retiro de dinero
  def sacar_dinero(nombre, saldo)
    # Itera sobre la lista de usuarios
    @usuarios.each do |usuario|
      if usuario.nombre == nombre  # Si el nombre del usuario coincide
        if usuario.saldo < saldo  # Si el saldo es insuficiente para retirar
          puts "Saldo insuficiente."
          break                    # Detiene el proceso si no hay suficiente dinero
        elsif usuario.saldo >= saldo  # Si el saldo es suficiente
          usuario.saldo -= saldo     # Descuenta la cantidad de dinero retirada
          puts "El saldo disponible es: #{usuario.saldo}."  # Muestra el saldo restante
        end
      end
    end
  end
end

# Creación de instancias de la clase Usuario
ana = Usuario.new('Ana', 9872, 450)    # Usuario Ana con pin 9872 y saldo de 450
pablo = Usuario.new('Pablo', 5555, 200) # Usuario Pablo con pin 5555 y saldo de 200
rodrigo = Usuario.new('Rodrigo', 2222, 900)  # Usuario Rodrigo con pin 2222 y saldo de 900

# Creación de una instancia de la clase Banco con los usuarios creados
banco = Banco.new([ana, pablo, rodrigo])

# Bucle principal para interactuar con el sistema de cajero
while true
  system("cls") || system("cls") #Esto limpia la pantalla al inicio de cada ciclo del bucle principal
  # Solicita al usuario su nombre y pin para ingresar
  puts "Bienvenido al Banco."
  puts "Por favor, digite su usuario."
  nombre = gets.chomp            # Lee el nombre ingresado por el usuario
  puts "Por favor, digite su pin."
  pin = gets.chomp.to_i          # Lee el pin y lo convierte a entero
  
  # Si el nombre y el pin son correctos, se autentica al usuario
  if banco.autenticar(nombre, pin)
    # Bucle interno para mostrar opciones una vez el usuario esté autenticado
    while true
      puts "Por favor digite una de estas opciones: "
      puts "1. Sacar dinero."
      puts "2. Consultar saldo."
      puts "3. Terminar sesión."
      opcion = gets.chomp         # Lee la opción seleccionada por el usuario

      # Si elige la opción 1 (Sacar dinero)
      if opcion == "1"
        puts "Digite la cantidad de dinero a retirar."
        saldo = gets.chomp.to_f    # Lee el monto a retirar y lo convierte a número flotante
        banco.sacar_dinero(nombre, saldo)  # Llama al método para retirar dinero

      # Si elige la opción 2 (Consultar saldo)
      elsif opcion == "2"
        # Itera sobre los usuarios para encontrar al que coincida con el nombre ingresado
        banco.usuarios.each do |usuario|
          if usuario.nombre == nombre
            puts "El saldo disponible es: #{usuario.saldo}"  # Muestra el saldo disponible
          end
        end

      # Si elige la opción 3 (Terminar sesión)
      elsif opcion == "3"
        puts "Saliendo del sistema, gracias por utilizar nuestro cajero."
        break  # Sale del bucle interno y termina la sesión

      else
        # Si se ingresa una opción incorrecta
        puts "Opción incorrecta, por favor, digite una opción válida."
      end
    end
  else
    # Si la autenticación falla, muestra un mensaje
    puts "Usuario no autenticado. Por favor, introduzca nombre y pin correctos."
  end
end
