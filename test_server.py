from server import calcular, converter_temperatura


def test_soma():
    resultado = calcular("soma", 5, 3)
    assert resultado == "O resultado é: 8."


def test_subtracao():
    resultado = calcular("subtracao", 10, 4)
    assert resultado == "O resultado é: 6."


def test_multiplicacao():
    resultado = calcular("multiplicacao", 7, 8)
    assert resultado == "O resultado é: 56."


def test_divisao():
    resultado = calcular("divisao", 10, 2)
    assert resultado == "O resultado é: 5.0."


def test_divisao_por_zero():
    resultado = calcular("divisao", 10, 0)
    assert resultado == "Não é possível dividir por zero."


def test_operacao_invalida():
    resultado = calcular("potencia", 2, 3)
    assert resultado == (
        "Operação inválida. Use somente soma, subtracao, multiplicacao ou divisao "
    )


def test_celsius_para_fahrenheit():
    resultado = converter_temperatura("celsius_para_fahrenheit", 0)
    assert resultado == "0 °C equivale a 32.0 °F"


def test_fahrenheit_para_celsius():
    resultado = converter_temperatura("fahrenheit_para_celsius", 32)
    assert resultado == "32 °F equivale a 0.0 °C"