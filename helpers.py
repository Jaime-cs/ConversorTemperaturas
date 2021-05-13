def celsius_para_kelvin(temperatura_celsius):
    """
    teste para converter temperaturas de celscius para kelvin
    :param temperatura_celsius:
    :return : temperatura.celsius:
    Formula = c + 275.15
     
    """
    temperatura_kelvin = temperatura_celsius + 275.15
    return temperatura_kelvin

def celsius_para_fahrenheit(temperatura_celsius):
    """"
    Funcao para converter temperatura de celsius para fahrenheit
    :param temperatura_celsius:
    :return : temperatura em fahrenheit
    Formula = c * 9 /5 + 32
    """
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5 + 32)
    return temperatura_fahrenheit
