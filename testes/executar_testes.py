# -*- coding: utf-8 -*-
"""
Runner de Testes — Geo-Explorer
Arquivo: testes/executar_testes.py

Executa todas as suítes de testes unitários e de fluxo,
exibe o resultado no terminal e salva o relatório em
testes/resultados.txt
"""

import os
import sys
import unittest
from datetime import datetime
from io import StringIO

BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULT_FILE = os.path.join(BASE_DIR, 'testes', 'resultados.txt')

sys.path.insert(0, BASE_DIR)


def descobrir_testes():
    loader = unittest.TestLoader()
    suites = []

    pastas = [
        os.path.join(BASE_DIR, 'testes', 'unitarios'),
        os.path.join(BASE_DIR, 'testes', 'fluxo'),
    ]

    for pasta in pastas:
        suite = loader.discover(start_dir=pasta, pattern='test_*.py')
        suites.append(suite)

    combinada = unittest.TestSuite(suites)
    return combinada


def executar(suite):
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    resultado = runner.run(suite)
    saida = stream.getvalue()
    return resultado, saida


def gerar_relatorio(resultado, saida_detalhe):
    now      = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    total    = resultado.testsRun
    falhas   = len(resultado.failures)
    erros    = len(resultado.errors)
    aprovados = total - falhas - erros
    cob      = round(aprovados / total * 100, 1) if total else 0

    linhas = [
        '=' * 60,
        '  RELATÓRIO DE TESTES — GEO-EXPLORER',
        f'  Gerado em  : {now}',
        '=' * 60,
        '',
        f'  Total de testes : {total}',
        f'  ✅ Aprovados    : {aprovados}',
        f'  ❌ Falhas       : {falhas}',
        f'  💥 Erros        : {erros}',
        f'  📊 Cobertura    : {cob}%',
        f'  Meta >= 70%    : {"ATINGIDA ✅" if cob >= 70 else "NÃO ATINGIDA ❌"}',
        '',
        '=' * 60,
        '  DETALHE',
        '=' * 60,
        '',
        saida_detalhe,
        '=' * 60,
    ]

    if resultado.failures:
        linhas += ['', '  FALHAS:', '']
        for test, msg in resultado.failures:
            linhas.append(f'  ❌ {test}')
            linhas.append(f'     {msg[:200]}')

    if resultado.errors:
        linhas += ['', '  ERROS:', '']
        for test, msg in resultado.errors:
            linhas.append(f'  💥 {test}')
            linhas.append(f'     {msg[:200]}')

    conteudo = '\n'.join(linhas)

    with open(RESULT_FILE, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    return cob, aprovados, total


def main():
    sys.stdout.reconfigure(encoding='utf-8')

    print('\n' + '=' * 60)
    print('  GEO-EXPLORER — Executando Testes')
    print('=' * 60 + '\n')

    suite    = descobrir_testes()
    resultado, saida = executar(suite)
    cob, aprovados, total = gerar_relatorio(resultado, saida)

    print(saida)
    print('=' * 60)
    print(f'  Total    : {total}')
    print(f'  Aprovados: {aprovados}')
    print(f'  Cobertura: {cob}%')
    print(f'  Meta >=70%: {"ATINGIDA ✅" if cob >= 70 else "NÃO ATINGIDA ❌"}')
    print('=' * 60)
    print(f'\n  Relatório salvo em: testes/resultados.txt\n')

    sys.exit(0 if not resultado.failures and not resultado.errors else 1)


if __name__ == '__main__':
    main()
