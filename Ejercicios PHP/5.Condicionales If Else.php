<?php
$a=2;
if ($a ==2){
    echo("a vale 2. \n");
}else{
    echo('a es diferente de 2');
}
//Concatenar condiciones
$Nombre = 'Esteban';
$Edad = 28;
$Pais='Colombia';

if ($Nombre =='Esteban' && $Edad == 28 && $Pais =='Colombia'){
    echo("Su nombre es $Nombre, tiene $Edad años, y es de $Pais"); 
}
elseif($Nombre == 'Esteban' && $Edad!==28){
    echo('Su nombre es Esteban y no tiene 28 años');
}elseif($Nombre != 'Esteban' && $Edad == 28){
    print('Su nombre no es Esteban y tiene 28 años');
}else{
    echo('No se llama Esteban ni tiene 28 años');  
}
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\5.Condicionales If Else.php" 
?>