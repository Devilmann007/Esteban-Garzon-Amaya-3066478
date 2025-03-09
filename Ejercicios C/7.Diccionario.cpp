#include<iostream>
#include<string>
#include<map>

using namespace std;

int main(){
    map<string, string> Coche;
    Coche["marca"]="Ford";
    Coche["color"]="Rojo";
    Coche["modelo"]="Sedan";
    Coche["placa"]="ROS227";
    // Imprimir los valores del mapa
    cout <<"\nContenido del mapa (diccionario): " << endl;
    //auto& para que el compilador reconozca automaticamente el tipo de varible y que estamos usando una referencia.
    /*par: cada elemento del mapa contiene dos partes:
    par.first = clave
    par.second = valor
    */
    for (auto& par : Coche ){ 
        cout << par.first << " : " << par.second << endl;              
    }
    cout<<"\nModificaciones de valores en el mapa: "<<endl;
    Coche["color"]="Verde";
    cout<<"color: "<<Coche["color"]<<endl;
    Coche["marca"]="Renault";
    cout<<"marca: "<<Coche["marca"]<<endl;
    Coche["modelo"]="Deportivo";
    cout<<"modelo: "<<Coche["modelo"]<<endl;
    Coche["placa"]="ROS007";
    cout<<"placa: "<<Coche["placa"]<<endl;

cout<<"\nMapa modificado: "<<endl;
for (auto& par : Coche ){ 
    cout << par.first << " : " << par.second << endl;              
}
}