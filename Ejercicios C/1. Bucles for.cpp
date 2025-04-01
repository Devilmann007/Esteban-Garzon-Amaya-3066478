#include <iostream>
#include <string>

using namespace std;

int main ()
{

    string nombre[]= {"Esteban", "Alejandra", "Andres", "Jesus"};    //array de strings 

    for (const string& name: nombre){
     cout<<name<<endl;
    }
    return 0;
}
