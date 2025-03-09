#include <iostream>
using namespace std;

int main() {
    double Voltaje, Resistencia, Intensidad;  // Usamos tipo double para mayor precisión en los cálculos

    // Solicitar entradas del usuario
    cout << "Ingrese el valor del voltaje del circuito: ";
    cin >> Voltaje;

    cout << "Ingrese el valor de la resistencia del circuito: ";
    cin >> Resistencia;

    // Calcular la intensidad (amperaje)
    Intensidad = Voltaje / Resistencia;

    // Mostrar el resultado
    cout << "Al conectar un resistor de: " << Resistencia << " ohm, a una fuente de: "
         << Voltaje << " V, El voltaje circulara una corriente de " << Intensidad << " amperios." << endl;

    return 0;
}
