#include <iostream>
#include <typeinfo>  // Para obtener el tipo de la variable
#include<math.h>
using namespace std;

int main() {
    // Declaramos las variables
    int a = 10, b = 4;
    int c;  // Variable para el resultado

    // Multiplicación
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: * " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = a * b;
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;  // Mostrar el tipo de c

    // División
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: / " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = a / b;
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;

    // Suma
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: + " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = a + b;
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;

    // Resta
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: - " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = a - b;
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;

    // Potenciación (usamos el `pow` para potencia en C++)
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: ** " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = static_cast<int>(pow(a, b));  // Convertimos el resultado a int
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;

    // Porcentaje
    cout << "La primera variable es: " << a << endl;
    cout << "El signo de la operacion es: % " << endl;
    cout << "La segunda variable es: " << b << endl;
    c = a % b;
    cout << "El resultado es: " << c << endl;
    cout << "Tipo de c: " << typeid(c).name() << endl;

    return 0;
}
