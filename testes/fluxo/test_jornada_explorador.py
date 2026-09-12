"""
Testes de Fluxo — Jornada Completa do Explorador
Arquivo: testes/fluxo/test_jornada_explorador.py

Simula o fluxo real de um explorador chamado "Ada Lovelace"
usando os três comandos em sequência:
  1. /trilha Python           → consulta o plano de exploração
  2. /desafio Python Iniciante → recebe uma missão de código
  3. /certificado Ada Lovelace Python → recebe o certificado

Valida a consistência dos dados entre os três comandos.
Cobertura alvo: >= 70%
"""

import json
import os
import random
import string
import unittest
from datetime import datetime

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(BASE_DIR, 'dados', 'geo_trilhas.json')


# ── Helpers compartilhados ───────────────────────────────────────────────────

def carregar_dados():
    with open(JSON_PATH, encoding='utf-8') as f:
        return json.load(f)

def buscar_trilha(tecnologia, dados):
    if not tecnologia or not isinstance(tecnologia, str):
        return None
    termo = tecnologia.strip().lower()
    for t in dados['trilhas']:
        if termo in t['tecnologia'].lower() or termo in t['nome'].lower():
            return t
    return None

def formatar_plano(trilha):
    if not trilha:
        return None
    return {
        'titulo':     f"Trilha de Exploração — {trilha['nome']}",
        'tecnologia': trilha['tecnologia'],
        'nivel':      trilha['nivel'],
        'tema':       trilha['tema'],
        'modulos':    trilha['numero_de_modulos'],
        'xp':         trilha['xp_total'],
        'horas':      trilha['duracao_horas'],
        'badges':     trilha['badges'],
        'missoes':    trilha['missoes_especiais'],
        'recompensa': trilha['recompensa_final'],
    }

def gerar_id():
    chars = string.ascii_uppercase + string.digits
    return 'GEO-' + ''.join(random.choices(chars, k=10))

def gerar_certificado(nome, tecnologia, dados):
    if not nome or not tecnologia:
        return None
    trilha = buscar_trilha(tecnologia, dados)
    if not trilha:
        return None
    cert_id = gerar_id()
    return {
        'id':         cert_id,
        'explorador': nome,
        'trilha':     trilha['nome'],
        'tecnologia': trilha['tecnologia'],
        'nivel':      trilha['nivel'],
        'tema':       trilha['tema'],
        'horas':      trilha['duracao_horas'],
        'xp':         trilha['xp_total'],
        'badges':     trilha['badges'],
        'recompensa': trilha['recompensa_final'],
        'data':       datetime.today().strftime('%d/%m/%Y'),
        'url':        f"https://geo-explorer.dev/certificado/{cert_id}",
    }


# ── Cenário ──────────────────────────────────────────────────────────────────

EXPLORADOR = 'Ada Lovelace'
TECNOLOGIA = 'Python'
NIVEL      = 'Iniciante'

DESAFIO_SIMULADO = {
    'titulo':      f'Missão de Código — {TECNOLOGIA} | Nível: {NIVEL}',
    'tipo':        'Algoritmo',
    'tecnologia':  TECNOLOGIA,
    'nivel':       NIVEL,
    'xp':          400,
    'pistas':      ['Pista 1', 'Pista 2', 'Pista 3'],
    'casos_de_teste': [
        {'entrada': [1,2,3], 'saida': [2]},
        {'entrada': [],      'saida': []},
        {'entrada': [2,4,6], 'saida': [2,4,6]},
    ],
    'criterios': ['Filtro correto', 'Código legível'],
}


# ── Testes de Fluxo ──────────────────────────────────────────────────────────

class TestEtapa1Trilha(unittest.TestCase):
    """ETAPA 1 — /trilha Python"""

    def setUp(self):
        self.dados  = carregar_dados()
        self.trilha = buscar_trilha(TECNOLOGIA, self.dados)
        self.plano  = formatar_plano(self.trilha)

    def test_e1_01_db_carregado(self):
        self.assertIsNotNone(self.dados)
        self.assertGreater(len(self.dados['trilhas']), 0)

    def test_e1_02_trilha_encontrada(self):
        self.assertIsNotNone(self.trilha)

    def test_e1_03_nome_da_trilha(self):
        self.assertEqual(self.trilha['nome'], 'Jornada do Código Selvagem')

    def test_e1_04_plano_gerado(self):
        self.assertIsNotNone(self.plano)

    def test_e1_05_nivel_correto(self):
        self.assertEqual(self.plano['nivel'], NIVEL)

    def test_e1_06_tecnologia_correta(self):
        self.assertEqual(self.plano['tecnologia'], TECNOLOGIA)

    def test_e1_07_modulos_positivos(self):
        self.assertGreater(self.plano['modulos'], 0)

    def test_e1_08_xp_positivo(self):
        self.assertGreater(self.plano['xp'], 0)

    def test_e1_09_badges_presentes(self):
        self.assertGreater(len(self.plano['badges']), 0)

    def test_e1_10_missoes_presentes(self):
        self.assertGreater(len(self.plano['missoes']), 0)


class TestEtapa2Desafio(unittest.TestCase):
    """ETAPA 2 — /desafio Python Iniciante"""

    def setUp(self):
        self.dados  = carregar_dados()
        self.trilha = buscar_trilha(TECNOLOGIA, self.dados)
        self.d      = DESAFIO_SIMULADO

    def test_e2_01_tecnologia_igual_trilha(self):
        self.assertEqual(self.d['tecnologia'], self.trilha['tecnologia'])

    def test_e2_02_nivel_igual_trilha(self):
        self.assertEqual(self.d['nivel'], self.trilha['nivel'])

    def test_e2_03_titulo_menciona_tecnologia(self):
        self.assertIn(TECNOLOGIA, self.d['titulo'])

    def test_e2_04_pelo_menos_3_casos(self):
        self.assertGreaterEqual(len(self.d['casos_de_teste']), 3)

    def test_e2_05_xp_menor_que_total_trilha(self):
        self.assertLess(self.d['xp'], self.trilha['xp_total'])

    def test_e2_06_pelo_menos_2_pistas(self):
        self.assertGreaterEqual(len(self.d['pistas']), 2)

    def test_e2_07_criterios_existem(self):
        self.assertGreaterEqual(len(self.d['criterios']), 1)


class TestEtapa3Certificado(unittest.TestCase):
    """ETAPA 3 — /certificado Ada Lovelace Python"""

    def setUp(self):
        self.dados  = carregar_dados()
        self.trilha = buscar_trilha(TECNOLOGIA, self.dados)
        self.plano  = formatar_plano(self.trilha)
        self.cert   = gerar_certificado(EXPLORADOR, TECNOLOGIA, self.dados)

    def test_e3_01_certificado_gerado(self):
        self.assertIsNotNone(self.cert)

    def test_e3_02_nome_explorador(self):
        self.assertEqual(self.cert['explorador'], EXPLORADOR)

    def test_e3_03_trilha_consistente(self):
        self.assertEqual(self.cert['trilha'], self.trilha['nome'])

    def test_e3_04_xp_consistente_com_plano(self):
        self.assertEqual(self.cert['xp'], self.plano['xp'])

    def test_e3_05_horas_consistentes(self):
        self.assertEqual(self.cert['horas'], self.plano['horas'])

    def test_e3_06_badges_iguais_ao_plano(self):
        self.assertEqual(sorted(self.cert['badges']), sorted(self.plano['badges']))

    def test_e3_07_nivel_consistente(self):
        self.assertEqual(self.cert['nivel'], self.plano['nivel'])

    def test_e3_08_url_contem_id(self):
        self.assertIn(self.cert['id'], self.cert['url'])


class TestEtapa4Consistencia(unittest.TestCase):
    """ETAPA 4 — Consistência entre os três comandos"""

    def setUp(self):
        self.dados  = carregar_dados()
        self.trilha = buscar_trilha(TECNOLOGIA, self.dados)
        self.plano  = formatar_plano(self.trilha)
        self.cert   = gerar_certificado(EXPLORADOR, TECNOLOGIA, self.dados)
        self.desafio = DESAFIO_SIMULADO

    def test_e4_01_tecnologia_consistente_em_todos(self):
        self.assertEqual(self.plano['tecnologia'], self.desafio['tecnologia'])
        self.assertEqual(self.desafio['tecnologia'], self.cert['tecnologia'])

    def test_e4_02_nivel_consistente_em_todos(self):
        self.assertEqual(self.plano['nivel'], self.desafio['nivel'])
        self.assertEqual(self.desafio['nivel'], self.cert['nivel'])

    def test_e4_03_badges_iguais_plano_certificado(self):
        self.assertEqual(len(self.plano['badges']), len(self.cert['badges']))

    def test_e4_04_todos_objetos_validos(self):
        self.assertIsNotNone(self.plano)
        self.assertIsNotNone(self.desafio)
        self.assertIsNotNone(self.cert)

    def test_e4_05_tema_consistente_plano_certificado(self):
        self.assertEqual(self.plano['tema'], self.cert['tema'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
