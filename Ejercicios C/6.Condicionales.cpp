#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int main(){
int Figura, Area;
cout<<"\n\n 1 para rombo: \n\n 2 para rectangulo: \n\n 3 para cuadrado: \n\n 4 para trapecio: \n\nSelecione la figura a calcular su area:  ";
cin>>Figura;
const int pi = 3.1416;
switch (Figura)
{
case 1:
    int Dmayor;
    cout<<"ingresa el valor de la diagonal mayor: "<<endl;
    cin>>Dmayor;
    int Dmenor;
    cout<<"ingresa el valor de la diagonal menor: "<<endl;
    cin>>Dmenor;
    Area=((Dmayor*Dmenor)/2);
    cout<<"El area del rombo es: "<<endl;
    break;
case 2:
    int Largo; 
    cout<<"ingresa el valor del largo del rectangulo: "<<endl;
    cin>>Largo;
    int Ancho;
    cout<<"ingresa el valor del ancho del rectangulo: "<<endl;
    cin>>Ancho;
    Area=Largo*Ancho;
    cout<<"El area del rectangulo es: "<<Area<<endl;
    break;
case 3:
    int Lado;
    cout<<"ingresa el valor del lado del cuadrado: "<<endl;
    cin>>Lado;
    Area=Lado*Lado;
    cout<<"El area del cuadrado es: "<<Area<<endl;
    break;
case 4:
    int Bmayor;
    cout<<"ingresa el valor de la base mayor: "<<endl;
    cin>>Bmayor;
    int Bmenor;
    cout<<"ingresa el valor de la base menor: "<<endl;
    cin>>Bmenor;
    int H;
    cout<<"ingrese la altura del trapecio: "<<endl;
    cin>>H;
    Area=(((Bmayor+Bmenor)*H)/2);
    cout<<"El area del trapecio es: "<<Area<<endl;
    break;  
default:
    break;
}
}