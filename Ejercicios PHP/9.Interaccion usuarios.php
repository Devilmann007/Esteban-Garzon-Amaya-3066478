<?php
echo('Escriba sus nombres completos: ');
$a = trim(fgets(STDIN));//trim elimina espacios y saltos de linea
echo('Escribas sus Apellidos completos: ');
$b = trim(fgets(STDIN));
echo('Escriba su profesion: ');
$c = trim(fgets(STDIN));
echo('Escriba su año de nacimiento: ');
$d = (int)(fgets(STDIN));
$e = 2025-$d;
echo("El (La) $c $a $b, tiene: $e años");
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\9.Interaccion usuarios.php"
?>