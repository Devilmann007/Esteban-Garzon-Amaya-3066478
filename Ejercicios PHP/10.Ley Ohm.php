<?php
echo('Ingrese el valor del voltaje del circuito: ');
$Voltaje = (int)(fgets(STDIN));
echo('Ingrese el valor de la resistencia del circuito: ');
$Resistencia = (int)(fgets(STDIN));
$Intensidad = $Voltaje/$Resistencia; //Intesidad entiendase por amperaje
echo("Al conectar un resistor de: $Resistencia ohm, a una fuente de: $Voltaje V, El voltage circulara una corriente de $Intensidad amperios");
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\10.Ley Ohm.php"
?>