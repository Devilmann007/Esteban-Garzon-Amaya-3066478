<?php
$a = array(1, 2, 3, 4, 5);
$b = array(6, 7, 8, 9, 10);
$c = array();

for ($contador = 0; $contador < count($a); $contador++) {
    $c[] = $a[$contador] * $b[$contador];
}

print_r($c);
#Funciones
#Definicion y llamada
// Función mostrar_texto
function mostrar_texto() {
    echo "Hola mundo\n";
}

mostrar_texto();  // Llamada a la función

// Función multiplicacion_1 (variables dentro de la función)
function multiplicacion_1() {
    $x = 5;
    $y = 8;
    echo $x * $y . "\n";
}

multiplicacion_1();  // Llamada a la función

// Función multiplicacion_2 (variables fuera de la función)
function multiplicacion_2() {
    global $x, $y;  // Usamos global para acceder a las variables fuera de la función
    echo $x * $y . "\n";
}

$x = 5;
$y = 8;
multiplicacion_2();  // Llamada a la función

// Función multiplicar con retorno
function multiplicar() {
    $a = 5;
    $b = 8;
    return $a * $b;
}

$resultado = multiplicar();  // Guardamos el resultado de la multiplicación
echo $resultado + 5 . "\n";  // Imprime la multiplicación más 5

// Función validar_dato (retorna un valor booleano)
function validar_dato() {
    global $a;  // Usamos global para acceder a la variable $a
    if ($a == 5) {
        return true;
    } else {
        return false;
    }
}

$a = 5;  // Asignamos valor a la variable $a
$dato = validar_dato();  // Llamada a la función validar_dato
echo $dato ? 'true' : 'false';  // Muestra true o false dependiendo del resultado
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\8.Funciones.php"
?>