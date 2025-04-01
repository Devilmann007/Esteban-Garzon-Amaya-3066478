#include <iostream>
#include <string>
#include <vector> // Agregar esta librería para usar vectores
using namespace std;

int main() {
    // Definir los arreglos
    string Lista1[] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
    string Lista2[] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
    string Lista3[] = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
    
    // Mostrar el valor en la posición 4 de Lista1
    cout << "Elemento en la posición 4 de Lista1: " << Lista1[4] << endl;

    // Mostrar la lista completa (Lista2)
    cout << "Lista2 completa: ";
    for (int i = 0; i < 6; i++) {
        cout << Lista2[i] << " ";
    }
    cout << endl;

    // Mostrar los elementos de la posición 0 y 3 de Lista3
    cout << "Elemento en la posición 0 y 3 de Lista3: " << Lista3[0] << ", " << Lista3[3] << endl;

    // Definir un vector que contiene los días de la semana
    vector<string> Lista4 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"};
    
    // Definir un vector con diferentes detalles en formato de string
    vector<string> Lista4_detalles = {"Esteban", "0.2", "2.25", "true"};
    
    // Mostrar elementos de Lista4
    cout << "Elemento en la posición 0 y 4 de Lista4: " << Lista4[0] << ", " << Lista4[4] << endl;

    // Mostrar detalles de Lista4_detalles
    cout << "Detalles de Lista4: ";
    for (const string& detalle : Lista4_detalles) {
        cout << detalle << " ";
    }
    cout << endl;

    return 0;
}
