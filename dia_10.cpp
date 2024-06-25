#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

bool esPalindromo(const std::string& str) {
    std::string original, reverso;
    
    
    for (char ch : str) {
        if (std::isalnum(ch)) {
            original += std::tolower(ch);
        }
    }

    reverso = original;
    std::reverse(reverso.begin(), reverso.end());

    return original == reverso;
}

int main() {
    std::string cadena;
    
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, cadena);

    if (esPalindromo(cadena)) {
        std::cout << "La cadena es un palíndromo." << std::endl;
    } else {
        std::cout << "La cadena no es un palíndromo." << std::endl;
    }

    return 0;
}
