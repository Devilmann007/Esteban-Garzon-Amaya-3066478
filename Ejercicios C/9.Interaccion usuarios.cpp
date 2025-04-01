#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, c;  // Variables para los nombres, apellidos y profesión
    int d, e;         // Variable para el año de nacimiento y edad

    // Solicitar datos del usuario
    cout << "Escriba sus nombres completos: ";
    getline(cin, a);  // Usamos getline para capturar toda la cadena de texto

    cout << "Escriba sus apellidos completos: ";
    getline(cin, b);  // Usamos getline para capturar toda la cadena de texto

    cout << "Escriba su profesion: ";
    getline(cin, c);  // Usamos getline para capturar toda la cadena de texto

    cout << "Escriba su año de nacimiento: ";
    cin >> d;  // Capturamos el año de nacimiento como un número entero

    // Calculamos la edad
    e = 2025 - d;

    // Imprimir la información
    cout << "El (La) " << c << " " << a << " " << b << " tiene " << e << " años." << endl;

    return 0;
}
