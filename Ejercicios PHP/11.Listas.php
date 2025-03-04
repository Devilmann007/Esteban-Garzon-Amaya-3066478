<?php
$Lista1 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
echo $Lista1[4]; // Traerá el dato en la posición 4 de la lista, que es 'Viernes'
echo "\n";

$Lista2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
print_r($Lista2); // Traerá toda la lista completa de datos

echo "\n";

$Lista3 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
echo $Lista3[0]. "y" .$Lista3[3];
echo "\n";

// Podemos colocar varios tipos de datos dentro de una lista de array
$Lista4 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 1, 2, 3, ['Esteban', 0.2, 2.25, true]];

echo $Lista4[0]. " y " .$Lista4[4]; // Traerá 'Lunes y Viernes'
echo "\n";
echo $Lista4[9][0]; // Traerá 'Esteban' (elemento dentro del subarreglo)
echo "\n";

// Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\11.Listas.php"
?>
