
#include <iostream>   
using namespace std;
int auxiliar=0;
int main() {
    // El compilador infiere el tamaño del array
    int miArray[5] ;

    // Imprimir los elementos del array
    for (int i = 0; i < 5; i++) {
        cout << "Ingrese un numero: " ;
        cin>>miArray[i];
    }
    cout << "Los numeros ingresados son: " ;
    for (int i = 0; i < 5; i++) {
        cout<<miArray[i]<<" ";
        
    }
    cout<<endl;


    for(int j = 0; j < 5; j++ ){
        for(int i = 0; i < 4; i++){
            if (miArray[i]<miArray[i+1])
            {
                auxiliar=miArray[i];
                miArray[i]=miArray[i+1]; 
                miArray[i+1]=auxiliar;         }
            
        }
    }
    cout << "El array ordenado es: " ;
    for (int i = 0; i < 5; i++) {
        cout<<miArray[i]<<" ";
    }
    return 0;
}


