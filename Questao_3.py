# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json
import xml.etree.ElementTree as ET

class faturamento:
    def __init__(self, dia, valor):
        self.dia = dia
        self.valor = valor

def processarFaturamento(faturamentos, fonte):
    faturamentosValidos = [f for f in faturamentos if f.valor > 0]

    if not faturamentosValidos:
        print(f"Não foram encontrados dados validos em {fonte}.")
        return

    soma = sum(f.valor for f in faturamentosValidos)
    menor = min(f.valor for f in faturamentosValidos)
    maior = max(f.valor for f in faturamentosValidos)
    media = soma / len(faturamentosValidos)
    dias_acima_media = len([f for f in faturamentosValidos if f.valor > media])

    print(f"Resultados para os dados em {fonte}:")
    print(f"Menor valor de faturamento: {menor:.2f}")
    print(f"Maior valor de faturamento: {maior:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}\n")

def lerFaturamentoJSON(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            faturamentos = [faturamento(item['dia'], item['valor']) for item in dados]
            return faturamentos
    except FileNotFoundError:
        print(f"Arquivo JSON '{arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON '{arquivo}'.")
    except KeyError as e:
        print(f"Chave faltando no JSON: {e}")
    return []

def lerFaturamentoXML(arquivo):
    try:
        tree = ET.parse(arquivo)
        root = tree.getroot()
        faturamentos = []
        for row in root.findall('row'):
            dia = int(row.find('dia').text)
            valor = float(row.find('valor').text)
            faturamentos.append(faturamento(dia, valor))
        return faturamentos
    except FileNotFoundError:
        print(f"Arquivo XML '{arquivo}' não foi encontrado.")
    except ET.ParseError:
        print(f"Erro ao parsear o arquivo XML '{arquivo}'.")
    except AttributeError as e:
        print(f"Elemento faltando no XML: {e}")
    except ValueError as e:
        print(f"Erro na conversão de tipo: {e}")
    return []

def main():
    arquivo_json = 'dados.json'
    arquivo_xml = 'dados.xml'

    faturamentos_json = lerFaturamentoJSON(arquivo_json)
    faturamentos_xml = lerFaturamentoXML(arquivo_xml)

    if faturamentos_json:
        processarFaturamento(faturamentos_json, "JSON")
    
    if faturamentos_xml:
        processarFaturamento(faturamentos_xml, "XML")

if __name__ == "__main__":
    main()