#include<iostream>
#include<string>
#include<math.h>

using namespace std;


int main(){
    cout<<"Ingrese el primer valor"<<endl;
    int a, b;
    cin>>a;
    cout<<"Ingrese el segundo valor"<<endl;
    cin>>b;
    for (int i = 0; i <=5; i++){
        double c = pow(a,b);
        cout<< "La potencia de "<<a<<" elevado a " << b << " es: "<<c<<endl;

    }
}