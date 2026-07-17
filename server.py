import logging
from mcp.server.fastmcp import FastMCP # Importa a classe FastMCP da biblioteca (SDK) MCP
from pathlib import Path

PASTA_PROJETO = Path(__file__).parent
FICHEIRO_LOG = PASTA_PROJETO / "server.log"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename=FICHEIRO_LOG,
encoding="utf-8")

mcp = FastMCP("Calculadora MCP") #O fastMCP é uma classe que cria um servidor, estamos a criar o servidor

@mcp.tool()
def calcular(operacao: str, a: float,b: float) -> str:#Calcula soma, subtracao, multiplicacao ou divisao entre a e b.

    logging.info("Tool calcular chamada: operacao=%s, a=%s,b=%s", operacao,a,b)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): # MCP já valida automaticamente.
        return "Erro: os valores a e b devem ser números."

    if operacao == "soma":
        resultado = a + b

    elif operacao == "subtracao":
        resultado = a - b

    elif operacao == "multiplicacao":
        resultado = a * b

    elif operacao == "divisao":
        if b == 0:
            return "Não é possível dividir por zero."
        resultado = a / b

    else:
        return "Operação inválida. Use somente soma, subtracao, multiplicacao ou divisao "

    return f"O resultado é: {resultado}."

#Nova tool para conversao de celsius para fahrenheit e vice-versa.
@mcp.tool()
def converter_temperatura(conversao: str, valor: float) -> str:

    logging.info("Tool conversao chamada: conversao=%s, valor=%s", conversao, valor)

    if not isinstance(valor,(int,float)): # MCP já valida automaticamente.
        return "Erro: O valor deve ser um número."

    if conversao == "celsius_para_fahrenheit":
        resultado = (valor * 1.8) + 32
        return f"{valor} °C equivale a {resultado:.1f} °F"

    elif conversao == "fahrenheit_para_celsius":
        resultado = (valor - 32) / 1.8
        return f"{valor} °F equivale a {resultado:.1f} °C"

    else:
        return (f"Erro: A conversão '{conversao}' não é válida. Por favor, escolhe entre: "
                f"'celsius_para_fahrenheit' ou 'fahrenheit_para_celsius'.")


if __name__ == "__main__":
    mcp.run()