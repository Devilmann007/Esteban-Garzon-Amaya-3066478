#include<iostream>
#include<string>

using namespace std;

int main(){
    int a;
    a=2;
    if (a=2){
        cout<<"A vale 2"<<endl;
    }
    else{
        cout<<"A es diferente a 2"<<endl;
    }
string nombre, pais;

nombre="Esteban";
int edad=27;
pais="Colombia";

if (nombre=="Esteban" && edad==27 && pais=="Colombia"){
    cout<<"Su nombre es "<< nombre <<" tiene "<< edad <<" y es de "<< pais <<endl;
}else if(nombre=="Esteban" && !(edad==27)){
    cout<<"Su nombre es Esteban y no tiene 27 años"<<endl;;
}else if(!(nombre=="Esteban") && (edad==27)){
    cout<<"Su nombre no es Esteban y tiene 27 años"<<endl;
}else{
    cout<<"No se llama Esteban ni tiene 27 años"<<endl;
}
}