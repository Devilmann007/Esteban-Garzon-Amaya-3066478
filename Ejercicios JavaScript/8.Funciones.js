//definimos array's con <[]
let a =[1,2,3,4,5]
let b =[6,7,8,9,10]
let c =[]

/*bucle for que recorre los indices de los arrays a y b 
a.length devuelve el numero de elementos 
.push agrega un elemento a c, en este caso la multiplicacion de los objetos a y b*/
for (let contador = 0; contador<a.length; contador++){
    c.push(a[contador]*b[contador])    
}
console.log(c)

//Funciones:
function mostrar_texto(){
    console.log("Hola mundo")
}
mostrar_texto()

//Funcion multiplicacion con sus variables declaradas dentro de la funcion.
function multiplicacion_1(){
    let x = 5
    let y = 8
    console.log(x*y)
}
multiplicacion_1()

//Funcion multiplicacion con sus variables declaradas fuera de la funcion.
function multiplicacion_2(){
    console.log(x*y)    
}
let x = 5
let y = 8
multiplicacion_2()

/*Las funciones pueden devolver los valores con la instruccion return
En el siguiente caso devolveremos la multiplicacion, y el resultado lo guardamos en una variable,
que luego imprimimos sumandole un valor*/

function multiplicar(){
    a = 5
    b = 8
    return a * b
}
Resultado=multiplicar()//declara la variable resultado como la ejecucion de la funcion multiplicar.
console.log(Resultado+5)//Multiplica a y b luego le suma 5.

//Podemos devolver cualquier tipo de dato, y tratarlo como tal fuera de la funcion.
//Funcion en la que se valida si la variable "a" es igual a 5 o no; que decicion booleana definir.
function validar_dato(){
    if (a==5){
        return true
    }else
        return false
}
a = 5 //declara el valor de la variable "a".
dato=validar_dato()//define la variable dato segun la funcion validar_dato.
console.log(dato) //imprime el valor booleano despues de validar el dato.

//Para ejecutar en terminar: node "C:\Users\Esteban Amaya\OneDrive - SENA\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\8.Funciones.js"