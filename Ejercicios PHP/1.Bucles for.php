<?php
//definimos las variables con el simbolo $ seguido del nombre de la variable($Variable)
//array para definir una lista de arreglo
$Nombres = array("Esteban", "Alejandra", "Andres", "Jesus");

//Recorre el indice del arreglo desde 0 ($i=0)
//Asegura que el bucle se ejecute mientras el índice sea menor que la cantidad de elementos en el arreglo.($i<count)
//aumenta el índice en cada iteración para acceder al siguiente elemento del arreglo. ($i++)
for ($i=0; $i<count($Nombres); $i++){
    echo $Nombres[$i]."\n";//salto de linea entre cada nombre
}
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\1.Bucles.php" 
?>
