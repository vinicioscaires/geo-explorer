"""
Testes Unitários — Comando /trilha
Arquivo: testes/unitarios/test_trilha.py

Valida a lógica de busca e estrutura de dados do comando /trilha
usando dados/geo_trilhas.json como fonte.
Cobertura alvo: >= 70%
"""

import json
import os
import sys
import unittest

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
JSON_PATH = os.path.join(BASE_DIR, 'dados', 'geo_trilhas.json')


# ── Lógica simulada do comando /trilha ───────────────────────────────────────

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
        'titulo':      f"Trilha de Exploração — {trilha['nome']}",
        'tecnologia':  trilha['tecnologia'],
        'nivel':       trilha['nivel'],
        'tema':        trilha['tema'],
        'modulos':     trilha['numero_de_modulos'],
        'xp':          trilha['xp_total'],
        'horas':       trilha['duracao_horas'],
        'badges':      trilha['badges'],
        'habilidades': trilha['habilidades'],
        'missoes':     trilha['missoes_especiais'],
        'recompensa':  trilha['recompensa_final'],
    }


# ── Testes ───────────────────────────────────────────────────────────────────

class TestCarregamentoDados(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()

    def test_arquivo_carregado(self):
        self.assertIsNotNone(self.dados)

    def test_trilhas_e_lista(self):
        self.assertIsInstance(self.dados['trilhas'], list)

    def test_pelo_menos_uma_trilha(self):
        self.assertGreater(len(self.dados['trilhas']), 0)

    def test_total_trilhas_bate(self):
        self.assertEqual(self.dados['total_trilhas'], len(self.dados['trilhas']))

    def test_campos_obrigatorios(self):
        campos = ['id','nome','tecnologia','nivel','tema','numero_de_modulos',
                  'xp_total','duracao_horas','badges','habilidades',
                  'missoes_especiais','recompensa_final','ativa']
        for t in self.dados['trilhas']:
            for c in campos:
                self.assertIn(c, t, f"Trilha id={t['id']} sem campo '{c}'")


class TestBuscaTrilha(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()

    def test_busca_python_minusculo(self):
        t = buscar_trilha('python', self.dados)
        self.assertIsNotNone(t)
        self.assertEqual(t['tecnologia'], 'Python')

    def test_busca_python_maiusculo(self):
        t = buscar_trilha('PYTHON', self.dados)
        self.assertIsNotNone(t)

    def test_busca_python_misto(self):
        t = buscar_trilha('PyThOn', self.dados)
        self.assertIsNotNone(t)

    def test_busca_parcial_java(self):
        t = buscar_trilha('java', self.dados)
        self.assertIsNotNone(t)

    def test_busca_react(self):
        t = buscar_trilha('react', self.dados)
        self.assertIsNotNone(t)
        self.assertEqual(t['tecnologia'], 'React')

    def test_tecnologia_inexistente(self):
        t = buscar_trilha('CobolXPTO9999', self.dados)
        self.assertIsNone(t)

    def test_string_vazia(self):
        t = buscar_trilha('', self.dados)
        self.assertIsNone(t)

    def test_none(self):
        t = buscar_trilha(None, self.dados)
        self.assertIsNone(t)


class TestEstruturaTrilhaPython(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()
        self.trilha = buscar_trilha('python', self.dados)

    def test_id_correto(self):
        self.assertEqual(self.trilha['id'], 1)

    def test_nome_correto(self):
        self.assertEqual(self.trilha['nome'], 'Jornada do Código Selvagem')

    def test_nivel_iniciante(self):
        self.assertEqual(self.trilha['nivel'], 'Iniciante')

    def test_tema_aventura(self):
        self.assertEqual(self.trilha['tema'], 'Aventura')

    def test_modulos_positivos(self):
        self.assertGreater(self.trilha['numero_de_modulos'], 0)

    def test_xp_positivo(self):
        self.assertGreater(self.trilha['xp_total'], 0)

    def test_badges_lista_nao_vazia(self):
        self.assertIsInstance(self.trilha['badges'], list)
        self.assertGreater(len(self.trilha['badges']), 0)

    def test_missoes_lista_nao_vazia(self):
        self.assertIsInstance(self.trilha['missoes_especiais'], list)
        self.assertGreater(len(self.trilha['missoes_especiais']), 0)

    def test_recompensa_string(self):
        self.assertIsInstance(self.trilha['recompensa_final'], str)
        self.assertGreater(len(self.trilha['recompensa_final']), 0)

    def test_trilha_ativa(self):
        self.assertTrue(self.trilha['ativa'])


class TestFormatacaoPlano(unittest.TestCase):

    def setUp(self):
        dados = carregar_dados()
        self.trilha = buscar_trilha('python', dados)
        self.plano  = formatar_plano(self.trilha)

    def test_plano_nao_nulo(self):
        self.assertIsNotNone(self.plano)

    def test_titulo_contem_nome(self):
        self.assertIn('Jornada do Código Selvagem', self.plano['titulo'])

    def test_tecnologia_python(self):
        self.assertEqual(self.plano['tecnologia'], 'Python')

    def test_tema_presente(self):
        self.assertIsNotNone(self.plano['tema'])

    def test_modulos_corretos(self):
        self.assertEqual(self.plano['modulos'], self.trilha['numero_de_modulos'])

    def test_xp_correto(self):
        self.assertEqual(self.plano['xp'], self.trilha['xp_total'])

    def test_badges_lista(self):
        self.assertIsInstance(self.plano['badges'], list)

    def test_missoes_lista(self):
        self.assertIsInstance(self.plano['missoes'], list)

    def test_formatar_none_retorna_none(self):
        self.assertIsNone(formatar_plano(None))


class TestIntegridadeJSON(unittest.TestCase):

    def setUp(self):
        self.dados = carregar_dados()

    def test_ids_unicos(self):
        ids = [t['id'] for t in self.dados['trilhas']]
        self.assertEqual(len(ids), len(set(ids)))

    def test_xp_positivos(self):
        for t in self.dados['trilhas']:
            self.assertGreater(t['xp_total'], 0, f"id={t['id']}")

    def test_modulos_inteiros_positivos(self):
        for t in self.dados['trilhas']:
            self.assertIsInstance(t['numero_de_modulos'], int)
            self.assertGreater(t['numero_de_modulos'], 0, f"id={t['id']}")

    def test_niveis_validos(self):
        niveis = {'Iniciante', 'Intermediário', 'Avançado'}
        for t in self.dados['trilhas']:
            self.assertIn(t['nivel'], niveis, f"id={t['id']}")

    def test_horas_positivas(self):
        for t in self.dados['trilhas']:
            self.assertGreater(t['duracao_horas'], 0, f"id={t['id']}")

    def test_badges_nao_vazias(self):
        for t in self.dados['trilhas']:
            self.assertGreater(len(t['badges']), 0, f"id={t['id']}")


if __name__ == '__main__':
    unittest.main(verbosity=2)
