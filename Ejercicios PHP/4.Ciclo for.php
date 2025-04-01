<?php
echo("Ingrese el primer valor:\n");
$a = (int)fgets(STDIN); // Obtener el primer valor (base)
echo("Ingrese el segundo valor:\n");
$c = (int)fgets(STDIN); // Obtener el segundo valor (exponente)

$valor = 1; // Inicializamos el valor en 1 (porque cualquier número elevado a 0 es 1)

for ($i = 1; $i <= $c; $i++) {
    $valor *= $a; // Multiplicamos el valor por la base
}

echo("La potencia de $a elevado a $c es: $valor\n");

//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\4.Ciclo for.php" 
?>