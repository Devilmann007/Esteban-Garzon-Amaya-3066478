#include<iostream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;

// Declaraciones de las funciones
void mostrar_texto();
void multiplicacion_1();
void multiplicacion_2();
int multiplicar();
bool validar_dato(int a);

int main() {
    // Definir los arreglos
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = {6, 7, 8, 9, 10};
    vector<int> c;

    // Bucle for que recorre los índices de los arrays a y b
    for (size_t contador = 0; contador < a.size(); contador++) {
        c.push_back(a[contador] * b[contador]);
    }

    // Imprimir el contenido del array c
    cout << "Resultado de la multiplicación de los arrays a y b: ";
    for (int val : c) {
        cout << val << " ";
    }
    cout << endl;

    // Llamar a las funciones
    mostrar_texto();
    multiplicacion_1();
    multiplicacion_2();

    // Función que devuelve un valor con return
    int resultado = multiplicar();
    cout << resultado + 5 << endl; // Multiplica a y b luego le suma 5

    // Llamar la función validar_dato
    bool dato = validar_dato(5);
    cout << dato << endl; // Imprime el valor booleano después de validar el dato

    return 0;
}

// Definición de las funciones fuera de main()
void mostrar_texto() {
    cout << "Hola mundo" << endl;
}

void multiplicacion_1() {
    int x = 5;
    int y = 8;
    cout << x * y << endl;
}

void multiplicacion_2() {
    int x = 5;
    int y = 8;
    cout << x * y << endl;
}

int multiplicar() {
    int a = 5;
    int b = 8;
    return a * b;
}

bool validar_dato(int a) {
    if (a == 5) {
        return true;
    } else {
        return false;
    }
}
