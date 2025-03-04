<?php
echo "Seleccione la figura para calcular su área: \n\n";
echo "1 para rombo\n";
echo "2 para rectángulo\n";
echo "3 para cuadrado\n";
echo "4 para trapecio\n";
echo ": ";
$Figura = trim(fgets(STDIN)); // Lee la figura seleccionada

$Pi = 3.1416;
$const = 2; // Valor constante

switch ($Figura) {
    case '1':
        echo "Ingresa el valor de la diagonal mayor: ";
        $Dmayor = (int)fgets(STDIN);
        echo "Ingresa el valor de la diagonal menor: ";
        $Dmenor = (int)fgets(STDIN);
        $Area = ($Dmayor * $Dmenor) / $const;
        echo "El área del rombo es: $Area\n";
        break;
    case '2':
        echo "Ingresa el valor del largo del rectángulo: ";
        $Largo = (int)fgets(STDIN);
        echo "Ingresa el valor del ancho del rectángulo: ";
        $Ancho = (int)fgets(STDIN);
        $Area = $Largo * $Ancho;
        echo "El área del rectángulo es: $Area\n";
        break;
    case '3':
        echo "Ingresa el valor del lado del cuadrado: ";
        $Lado = (int)fgets(STDIN);
        $Area = $Lado * $Lado;
        echo "El área del cuadrado es: $Area\n";
        break;
    case '4':
        echo "Ingresa el valor de la base mayor: ";
        $Bmayor = (int)fgets(STDIN);
        echo "Ingresa el valor de la base menor: ";
        $Bmenor = (int)fgets(STDIN);
        echo "Ingresa la altura del trapecio: ";
        $H = (int)fgets(STDIN);
        $Area = (($Bmayor + $Bmenor) * $H) / 2;
        echo "El área del trapecio es: $Area\n";
        break;
    default:
        echo "Opción no válida.\n";
        break;
}
//Para ejecutar en terminal: php "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios PHP\6.Condicionales.php"
?>
