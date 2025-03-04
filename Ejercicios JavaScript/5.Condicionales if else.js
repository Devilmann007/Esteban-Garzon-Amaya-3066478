let a = 2
if (a == 2){
    console.log("a vale 2")
}else{
    console.log("a es diferente de 2")
}
//concatenar condiciones
let nombre = "Esteban"
let edad = 27
let pais = "Colombia"

if (nombre=="Esteban" && edad==27 && pais=="Colombia"){
    console.log('Su nombre es', nombre,'tiene',edad,'y es de',pais)
}else if(nombre=="Esteban" && !(edad==27)){// && ! significa "Y no"
    console.log('Su nombre es Esteban y no tiene 27 años')
}else if(!(nombre=="Esteban") && (edad==27)){
    console.log('Su nombre no es Esteban y tiene 27 años')
}else{
    console.log('No se llama Esteban ni tiene 27 años')
}
// condigo para ejecutar en consola: node "C:\Sena\Analisis y desarrollo de software\Ficha 3066478 segundo trimestre\Ejercicios JavaScript\5.Condicionales if else.js"