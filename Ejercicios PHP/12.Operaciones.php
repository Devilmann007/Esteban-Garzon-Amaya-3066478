<?php
//En este caso se le pedira al usuario el dato de entrada definidos en dos variables.
echo("Ingrese el primer valor: ");
$A = (int)(fgets(STDIN));//int: define el valor de la variable como un numero.
echo("Ingrese el segundo valor: ");
$B = (int)(fgets(STDIN));
//Definimos las operaciones a realizar.
$suma = $A+$B;
echo("la suma de los numeros es: $suma\n");
$res = $A-$B;
echo("la resta de los numeros es: $res\n");
$multi = $A*$B;
echo("la multiplicacion de los numeros es: $multi\n");
if ($B != 0) {
    $div = $A / $B;
    echo("La división de los números es: $div\n");
} else {
    echo "No se puede dividir por cero.\n";
}

//Definimos una variable que compare el igual y el mayor entre A y B.
$igual = ($A == $B) ? 'sí' : 'no';//compara los valores y devuelve una respuesta textual.
echo "¿El número $A es igual a $B? $igual\n";

$mayor = ($A > $B) ? $A : $B;
$menor = ($A < $B) ? $A : $B;

echo "El número menor es: $menor\n";//Devuelve el valor numerico si el valor es verdadero.
echo "El número mayor es: $mayor\n";//Devuelve el valor numerico si el valor es falso.

//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\12.Operaciones.php"
?>