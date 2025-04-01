//Definimos un objecto, que es una coleccion de pares clave:valor
let coche={'marca': 'Ford', 'color': 'rojo', 'modelo': 'sedan', 'placa': 'ROS227'} 
//imprime todos los atributos contenidos en "coche"
console.log(coche)
//imprime el atributo "color".
console.log(coche["color"])
//cambia el valor dentro del atributo "color".
coche['color']="verde"
//imprime nuevo valor.
console.log(coche["color"])
//cambia el valor dentro del atributo "marca".
coche['marca']='renault'
//imprime nuevo valor.
console.log(coche["marca"])
//imprime todos los atributos contenidos en "coche" luego de cambios
console.log(coche)

//Para ejecutar en terminar: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\7.Diccionario.js"
