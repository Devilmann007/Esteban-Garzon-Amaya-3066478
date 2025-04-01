<?php
// Tabla de la verdad

// El operador lógico && solo devuelve true si ambos valores son true.
$a = true;
$b = false;
echo($a && $b) ? 'true' : 'false';// El resultado será "false" porque b es igual a false
echo("\n"); 
// Comparación de $a y $b, y luego $c < $d con operador lógico &&
$a = 2;
$b = 3;
$c = 4;
$d = 10;
//? 'true' : 'false'; en php true es = 1 y false no imprime nada, por esta razon agregamos true y false como cadena de texto
echo ($a == $b && $c < $d) ? 'true' : 'false'; // El resultado será "false" porque $a no es igual a $b
echo "\n"; // Salto de línea para mejorar la legibilidad

// El operador lógico ! invierte el valor de la expresión booleana
// Se evalúa primero la expresión ($a == $b), se invierte con ! y luego se compara con ($c > $d)
echo(!($a == $b) && ($c > $d) ) ? 'true' : 'false'; // El resultado será "true" porque ($a == $b) es false, y ! lo convierte en true.

// Para ejecutar en terminal:
// php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\13.Tabla de la verdad.php"
?>
