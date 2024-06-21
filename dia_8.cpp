#include <iostream>
int a,b;

int suma(int a,int b){
    return a+b; 
}

int main(){
    std::cout<<"Puedes introducir un numero: ";
    std::cin>>a;

    std::cout<<"Puedes introducir otro numero: ";
    std::cin>>b;
    
    std::cout<<"La suma de los numeros ingresados es:"<<suma(a,b);
}
