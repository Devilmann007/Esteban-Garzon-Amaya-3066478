Contador=0
while (Contador<30)    
    Contador += 1
    console.log('iteracion', Contador)
//Combinado con if else
const prompt = require('prompt-sync')();
while (true){
    console.log('introduzca  un valor mayor a 10');
    let a = Number(prompt());
    if (a > 10){
        console.log('Es correcto');
        break;
    } 
    else{
        console.log('Es incorrecto, pruebe de nuevo');
    }            
}
/*const prompt = require('prompt-sync')(); //Este código se usa en Node.js para importar y configurar la librería prompt-sync,
que permite leer entrada del usuario de forma síncrona (sin callbacks ni promesas).*/
//Para ejecutar en terminal, se debe digitar el siguite comando: node "Ejercicios JavaScript/2.Bucles while.js" (node "ubicacion del archivo")
      