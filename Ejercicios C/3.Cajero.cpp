#include<iostream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;

class Usuario{
    private://private para que los atributos de la clase no puedan ser modificados directamente desde fuera de la clase
    string nombre;// propiedad para almacenar nombre//String: texto
    int pin;//int:numero entero
    double saldo;//double: numero con decimales
    public:
    // Constructor: Inicializa las propiedades del objeto
    Usuario(string nombre, int pin, double saldo){
    this->nombre = nombre; // Asigna el parámetro 'nombre' a la propiedad 'nombre'
    this->pin = pin; // Asigna el parámetro 'pin' a la propiedad 'pin'
    this->saldo = saldo; // Asigna el parámetro 'saldo' a la propiedad 'Saldo'
    }
    // Métodos para acceder a los atributos
    string getNombre() { return nombre; }
    int getPin() { return pin; }
    double getSaldo(){return saldo;}
    // Método para modificar el saldo
    void setSaldo(double nuevoSaldo) {
        saldo = nuevoSaldo;
    }
};

class SistemaUsuarios{
    private:
    vector<Usuario>Usuarios;// Lista de objetos Usuario
    public:
    SistemaUsuarios(vector<Usuario>Usuarios={}){
        this->Usuarios = Usuarios;// Guarda la lista de usuarios
    }
     // Método para obtener la lista de usuarios
     vector<Usuario>& getUsuarios() {
        return Usuarios;
    }
    // Método de autenticación
    Usuario* Autenticar(string nombre, int pin) {
        for (auto& usuario : Usuarios) {
            if (usuario.getNombre() == nombre && usuario.getPin() == pin) {
                return &usuario; // Devuelve un puntero al usuario autenticado
            }
        }
        cout<<"Nombre o pin incorrectos"<<endl;
        return nullptr; // Si no se encuentra, devuelve nullptr
    }
};
class Sacar_dinero{
    public:
    Sacar_dinero(Usuario& usuario, double cantidad){
        if(usuario.getSaldo() < cantidad){
            cout<<"Saldo insuficiente"<<endl;
        } else {
            usuario.setSaldo(usuario.getSaldo() - cantidad);//set para modificar el dato Saldo
            cout<<"El saldo disponible es: "<<usuario.getSaldo()<<endl;
        }
    }
};
int main(){
Usuario u1("Alejandra", 9711, 450.11);
Usuario u2("Esteban", 9707, 500.07);
Usuario u3("Andres", 2734, 980.27);

SistemaUsuarios banco({u1, u2 , u3});

string nombre, opcion;
int pin;
double saldo, cantidad;
while (true)
{
    cout<<"Bienvenido al Banco, por favor, identifíquese."<<endl;
    cout<<"Introduzca su nombre:"<<endl;
    cin>>nombre;
    cout<<"Introduzca su pin:"<<endl;
    cin>>pin;

    Usuario* usuarioAutenticado = banco.Autenticar(nombre, pin);
    if(usuarioAutenticado){ 
        while(true){
            cout<<"Por favor, elija una de estas opciones:\n 1. Sacar dinero\n 2. Terminar sesión."<<endl;
            cin>>opcion;
            if(opcion=="1"){
                cout<<"Introduzca la cantidad a retirar"<<endl;
                cin>>cantidad;
                Sacar_dinero(*usuarioAutenticado, cantidad);
            } else if (opcion=="2") {
                cout<<"Saliendo del sistema"<<endl;
                break;
            } else {
                cout<<"Usuario no autenticado. Por favor, introduzca nombre y pin correctos."<<endl;
            }
        }
    }
}
};




   