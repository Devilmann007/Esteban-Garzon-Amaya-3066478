#include <iostream>
using namespace std;

int main() {
    // Variables booleanas
    bool a = true;
    bool b = false;
    
    // Operador AND (&&)
    cout << "Resultado de a && b: " << (a && b) << endl;
    // El resultado será "false" porque b es false.

    // Variables numéricas
    int x = 2, y = 3, z = 4, w = 10;

    // Operador AND (&&) con comparaciones
    cout << "Resultado de (x == y && z < w): " << ((x == y) && (z < w)) << endl;
    // Resultado: (x == y) es false, por lo tanto, el operador && devuelve "false".

    // Operador NOT (!) en una expresión
    cout << "Resultado de !a == (y && z > w): " << (!(a == (y && z > w))) << endl;
    // El operador NOT invierte el valor de la comparación de "a" con el resultado de la comparación (y && z > w).
    // Aquí, (y && z > w) es false, entonces el operador "!" invierte el valor de "true".

    return 0;
}
