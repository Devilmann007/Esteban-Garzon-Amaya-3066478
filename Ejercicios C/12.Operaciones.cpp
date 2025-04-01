#include <iostream>
using namespace std;

int main() {
    // Variables para almacenar los números introducidos por el usuario
    double A, B;

    // Solicitar los números al usuario
    cout << "Ingrese el valor de A: ";
    cin >> A;
    cout << "Ingrese el valor de B: ";
    cin >> B;

    // Realizar operaciones
    double suma = A + B;
    double resta = A - B;
    double multiplicacion = A * B;
    double division = A / B;

    // Mostrar los resultados de las operaciones
    cout << "La suma de los números es: " << suma << endl;
    cout << "La resta de los números es: " << resta << endl;
    cout << "La multiplicación de los números es: " << multiplicacion << endl;
    cout << "La división de los números es: " << division << endl;

    // Comparar los valores de A y B
    bool igual = (A == B);
    cout << "¿El número " << A << " es igual a " << B << "? " << (igual ? "Sí" : "No") << endl;

    // Determinar el mayor y el menor de los dos números
    double mayor = (A > B) ? A : B;
    double menor = (A < B) ? A : B;

    // Mostrar el número mayor y menor
    cout << "El número mayor es: " << mayor << endl;
    cout << "El número menor es: " << menor << endl;

    return 0;
}
