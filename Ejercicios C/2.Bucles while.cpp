#include <iostream>
#include <math.h>

using namespace std;

int main ()
{
    int contador, a;
    contador=0;
    while (contador<30)
    {
        contador+=1;
        cout<<"iteracion"<<contador<<endl;
    }
    while (true){
        cout<<"introduzca  un valor mayor a 10"<<endl;
        cin>>a;
        if (a>10){
            cout<<"Es correcto"<<endl;
            break;    
        }else{
        cout<<"Es incorrecto, pruebe de nuevo"<<endl;
        }
    }
    return 0;   
}
