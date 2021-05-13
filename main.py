"""
Programa em Python 3 para converter Celsius para kelvin e fahrnheit

"""

from helpers import celsius_para_fahrenheit, celsius_para_kelvin

if __name__ == '__main__':
    while True:
        mensagem = "\Por favor insira a temperatura em Celsius."
        mensagem += "\n Se desejar sair , pressione 'q': "


        try:
            celsius = input(mensagem)
            if celsius.lower() != 'q':
                print(f"\nTemperatura em Kelvin(K) = {celsius_para_kelvin(float(celsius))}")
                print(f"Temperatura em fahrenheit(F) = {celsius_para_fahrenheit(float(celsius))}")
            else:
                print("\nAté a pròxima!")
                break
        except ValueError:
            print("\nVoce digitou um caracter invalido.  \nPor favor insira um numero ou a letra 'q'. ")

