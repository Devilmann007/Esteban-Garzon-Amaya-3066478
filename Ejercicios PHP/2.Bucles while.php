<?php
//definimos la variable contador
$contador = 0;
while($contador<30){
    $contador+=1;
    echo('iteracion'. $contador. "\n");
}
while(true){
    echo("'introduzca  un valor mayor a 10'\n");
    $a = fgets(STDIN);//comando para leer entrada del usuario desde la terminal
    if($a>10){
        echo("Es correcto");
        break;
    }
    else{
        echo("'Es incorrecto, pruebe de nuevo'\n");
    }
}
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\2.Bucles while.php"
?>