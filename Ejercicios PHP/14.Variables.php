<?php
// Aplicando variables.
$a = 10;
$b = 4;

// Multiplicación:
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: * ' . "\n";
echo 'La segunda variable es: ' . $b . "\n";
$c = ($a * $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// División:
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: / ' . "\n";
$c = ($a / $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// Suma:
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: + ' . "\n";
echo 'La segunda variable es: ' . $b . "\n";
$c = ($a + $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// Resta:
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: - ' . "\n";
echo 'La segunda variable es: ' . $b . "\n";
$c = ($a - $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// Potenciación:
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: ** ' . "\n";
echo 'La segunda variable es: ' . $b . "\n";
$c = ($a ** $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// Porcentaje (módulo):
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: % ' . "\n";
echo 'La segunda variable es: ' . $b . "\n";
$c = ($a % $b);
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de dato es: ' . gettype($c) . "\n\n";

// Para ejecutar en terminal:
// php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\14.Variables.php"
?>
