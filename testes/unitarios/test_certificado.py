"""
Testes Unitários — Comando /certificado
Arquivo: testes/unitarios/test_certificado.py

Valida a geração, estrutura e integridade do certificado de explorador.
Cobertura alvo: >= 70%
"""

import json
import os
import random
import re
import string
import unittest
from datetime import datetime

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(BASE_DIR, 'dados', 'geo_trilhas.json')


# ── Lógica simulada do comando /certificado ──────────────────────────────────

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
        'id':           cert_id,
        'explorador':   nome,
        'trilha':       trilha['nome'],
        'tecnologia':   trilha['tecnologia'],
        'nivel':        trilha['nivel'],
        'tema':         trilha['tema'],
        'horas':        trilha['duracao_horas'],
        'xp':           trilha['xp_total'],
        'badges':       trilha['badges'],
        'recompensa':   trilha['recompensa_final'],
        'data':         datetime.today().strftime('%d/%m/%Y'),
        'url':          f"https://geo-explorer.dev/certificado/{cert_id}",
    }


# ── Testes ───────────────────────────────────────────────────────────────────

class TestGeracaoCertificado(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.cert  = gerar_certificado('Ada Lovelace', 'Python', self.dados)

    def test_nao_nulo(self):
        self.assertIsNotNone(self.cert)

    def test_nome_explorador(self):
        self.assertEqual(self.cert['explorador'], 'Ada Lovelace')

    def test_trilha_contem_python(self):
        self.assertIn('Python', self.cert['trilha'] + self.cert['tecnologia'])

    def test_tecnologia_python(self):
        self.assertEqual(self.cert['tecnologia'], 'Python')

    def test_nivel_iniciante(self):
        self.assertEqual(self.cert['nivel'], 'Iniciante')

    def test_tema_presente(self):
        self.assertIsInstance(self.cert['tema'], str)
        self.assertGreater(len(self.cert['tema']), 0)


class TestCalculosCertificado(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.cert  = gerar_certificado('Ada Lovelace', 'Python', self.dados)
        self.trilha = buscar_trilha('Python', self.dados)

    def test_horas_corretas(self):
        self.assertEqual(self.cert['horas'], self.trilha['duracao_horas'])

    def test_xp_correto(self):
        self.assertEqual(self.cert['xp'], self.trilha['xp_total'])

    def test_horas_positivas(self):
        self.assertGreater(self.cert['horas'], 0)

    def test_xp_positivo(self):
        self.assertGreater(self.cert['xp'], 0)


class TestBadgesRecompensa(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.cert  = gerar_certificado('Ada Lovelace', 'Python', self.dados)
        self.trilha = buscar_trilha('Python', self.dados)

    def test_badges_lista(self):
        self.assertIsInstance(self.cert['badges'], list)
        self.assertGreater(len(self.cert['badges']), 0)

    def test_badges_iguais_trilha(self):
        self.assertEqual(sorted(self.cert['badges']), sorted(self.trilha['badges']))

    def test_recompensa_string(self):
        self.assertIsInstance(self.cert['recompensa'], str)
        self.assertGreater(len(self.cert['recompensa']), 0)

    def test_recompensa_igual_trilha(self):
        self.assertEqual(self.cert['recompensa'], self.trilha['recompensa_final'])


class TestIdUrl(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.cert  = gerar_certificado('Ada Lovelace', 'Python', self.dados)

    def test_id_string(self):
        self.assertIsInstance(self.cert['id'], str)

    def test_id_comeca_geo(self):
        self.assertTrue(self.cert['id'].startswith('GEO-'))

    def test_id_tamanho_14(self):
        self.assertEqual(len(self.cert['id']), 14)  # GEO- + 10

    def test_url_contem_id(self):
        self.assertIn(self.cert['id'], self.cert['url'])

    def test_url_contem_dominio(self):
        self.assertIn('geo-explorer.dev', self.cert['url'])

    def test_ids_distintos(self):
        c2 = gerar_certificado('Ada Lovelace', 'Python', self.dados)
        self.assertNotEqual(self.cert['id'], c2['id'])


class TestData(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.cert  = gerar_certificado('Ada Lovelace', 'Python', self.dados)

    def test_data_string(self):
        self.assertIsInstance(self.cert['data'], str)
        self.assertGreater(len(self.cert['data']), 0)

    def test_data_formato_br(self):
        self.assertRegex(self.cert['data'], r'^\d{2}/\d{2}/\d{4}$')


class TestEntradasInvalidas(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()

    def test_nome_vazio(self):
        self.assertIsNone(gerar_certificado('', 'Python', self.dados))

    def test_tecnologia_vazia(self):
        self.assertIsNone(gerar_certificado('Ada', '', self.dados))

    def test_tecnologia_inexistente(self):
        self.assertIsNone(gerar_certificado('Ada', 'CobolXPTO', self.dados))

    def test_nome_none(self):
        self.assertIsNone(gerar_certificado(None, 'Python', self.dados))

    def test_tecnologia_none(self):
        self.assertIsNone(gerar_certificado('Ada', None, self.dados))


class TestOutrasTrilhas(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()

    def test_certificado_java(self):
        # Usa o nome completo da trilha para evitar ambiguidade com JavaScript
        c = gerar_certificado('Alan Turing', 'Galáxia Java', self.dados)
        self.assertIsNotNone(c)
        self.assertEqual(c['nivel'], 'Intermediário')

    def test_certificado_devops(self):
        c = gerar_certificado('Grace Hopper', 'DevOps', self.dados)
        self.assertIsNotNone(c)
        self.assertEqual(c['nivel'], 'Avançado')

    def test_certificado_sql(self):
        c = gerar_certificado('Linus Torvalds', 'SQL', self.dados)
        self.assertIsNotNone(c)
        self.assertEqual(c['nivel'], 'Iniciante')


if __name__ == '__main__':
    unittest.main(verbosity=2)
