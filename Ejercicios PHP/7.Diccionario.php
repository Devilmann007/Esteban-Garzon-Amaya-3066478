<?php
// Creación de un conjunto (array asociativo)
$coche = array(
    'marca' => 'Ford',
    'color' => 'rojo',
    'modelo' => 'sedan',
    'placa' => 'ROS227'
);

// Acceso a un valor
echo $coche['color'] . "\n";  // Imprime el color

// Cambiar el valor
$coche['color'] = 'verde';
echo $coche['color'] . "\n";  // Imprime el nuevo color

// Acceso a otro valor
echo $coche['marca'] . "\n";  // Imprime la marca

// Cambiar el valor de la marca
$coche['marca'] = 'Renault';
echo $coche['marca'] . "\n";  // Imprime la nueva marca

// Imprime todo el array
print_r($coche);//print_r para imprimir todo el contenido de un arreglo.
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\7.Diciconario.php"
?>