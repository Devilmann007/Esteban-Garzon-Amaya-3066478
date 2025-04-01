<?php
class Usuario{
    public $nombre;
    public $pin;
    public $saldo;

    public function __construct($nombre, $pin, $saldo){
        $this->nombre = $nombre;
        $this->pin = $pin;
        $this->saldo = $saldo;
    }
}

class Banco{
    public $Usuarios;

    public function __construct($Usuarios = []){
        $this->Usuarios = $Usuarios;
    }

    public function autenticar($nombre, $pin){
        foreach ($this->Usuarios as $Usuario) {
            if ($Usuario->nombre == $nombre && $Usuario->pin == $pin) {
                echo('Estás logeado.'."\n");
                return $Usuario;
            }
        }
        echo('Nombre o pin incorrectos.\n');
        return null; // El return está fuera del foreach
    }

    public function sacar_dinero($Usuario, $cantidad){
        if ($Usuario->saldo < $cantidad) {
            echo('Saldo insuficiente.\n');
        } else {
            $Usuario->saldo -= $cantidad;
            echo('El saldo disponible es: ' . $Usuario->saldo."\n"); 
        }
    }
} 
$alejandra = new Usuario("Alejandra", 9711, 450);
$esteban = new Usuario("Esteban", 9707, 500);
$andres = new Usuario("Andres", 2734, 980);

$banco = new Banco([$alejandra, $esteban, $andres]);
while (true) {
    echo("Bienvenido al Banco!\npor favor, identifíquese!.\n");
    echo("Introduzca el nombre:\n");
    $nombre = trim(fgets(STDIN));//trim elimina espacios y saltos de linea 
    echo("Introduzca el pin:\n");
    $pin = (int)fgets(STDIN);

    $usuario = $banco->autenticar($nombre, $pin);
    if ($usuario){
        while(true){
            echo("Por favor, elija una de estas opciones:\n 1. Sacar dinero\n 2. Terminar sesión.\n");
            $opcion = (int)fgets(STDIN);

            if($opcion=="1"){
                echo("Introduce cantidad a sacar:\n");
                $saldo=(int)fgets(STDIN);
                $banco->sacar_dinero($usuario,$saldo);
            }elseif($opcion=="2"){
                echo("Saliendo del sistema.");
                break;
            }    
            else {
                echo("Opción incorrecta. Por favor, introduzca otra opción.\n");
            }            
        }
    }
    echo("Usuario no autenticado. Por favor, introduzca nombre y pin correctos.");    
}
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\3.Cajero.php" 
?>