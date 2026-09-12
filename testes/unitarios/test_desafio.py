"""
Testes Unitários — Comando /desafio
Arquivo: testes/unitarios/test_desafio.py

Valida a estrutura, regras de negócio e integridade de um desafio simulado
gerado pelo comando /desafio.
Cobertura alvo: >= 70%
"""

import unittest

# ── Objeto simulado do comando /desafio Python Iniciante ────────────────────

DESAFIO_SIMULADO = {
    'titulo':      'Missão de Código — Python | Nível: Iniciante',
    'tipo':        'Algoritmo',
    'tecnologia':  'Python',
    'nivel':       'Iniciante',
    'tema':        'Aventura',
    'tempo':       '30 minutos',
    'dificuldade': '⭐☆☆☆☆',
    'xp':          400,
    'narrativa': (
        'Em uma floresta de dados binários, o jovem explorador encontrou um mapa '
        'cifrado. Para decifrar o próximo ponto da jornada, precisará escrever um '
        'programa que leia uma lista de números inteiros e retorne apenas os pares, '
        'em ordem crescente. O Oráculo da Floresta aguarda sua solução.'
    ),
    'entrada': [2, 7, 4, 1, 8, 3, 6],
    'saida_esperada': [2, 4, 6, 8],
    'pistas': [
        'Use uma estrutura de repetição para percorrer a lista.',
        'O operador % (módulo) indica se um número é par quando o resultado for 0.',
        'A função sorted() pode ordenar a lista resultante.',
    ],
    'casos_de_teste': [
        {'entrada': [1, 2, 3, 4],     'saida': [2, 4]},
        {'entrada': [1, 3, 5, 7],     'saida': []},
        {'entrada': [10, 20, 30],     'saida': [10, 20, 30]},
        {'entrada': [],               'saida': []},
    ],
    'criterios': [
        'Filtro correto de números pares',
        'Ordenação crescente do resultado',
        'Tratamento de lista vazia',
        'Código limpo e legível',
    ],
    'desafio_lendario': (
        'Estenda a solução para aceitar também strings numéricas na entrada '
        'e converta-as antes de filtrar.'
    ),
}


# ── Testes ───────────────────────────────────────────────────────────────────

class TestCamposObrigatorios(unittest.TestCase):

    def setUp(self):
        self.d = DESAFIO_SIMULADO

    def test_objeto_nao_nulo(self):
        self.assertIsNotNone(self.d)

    def test_titulo_string(self):
        self.assertIsInstance(self.d['titulo'], str)

    def test_tipo_string_nao_vazio(self):
        self.assertIsInstance(self.d['tipo'], str)
        self.assertGreater(len(self.d['tipo']), 0)

    def test_tecnologia_python(self):
        self.assertEqual(self.d['tecnologia'], 'Python')

    def test_nivel_iniciante(self):
        self.assertEqual(self.d['nivel'], 'Iniciante')

    def test_narrativa_longa(self):
        self.assertGreaterEqual(len(self.d['narrativa']), 80)

    def test_pistas_lista(self):
        self.assertIsInstance(self.d['pistas'], list)

    def test_casos_lista(self):
        self.assertIsInstance(self.d['casos_de_teste'], list)

    def test_criterios_lista(self):
        self.assertIsInstance(self.d['criterios'], list)


class TestRegrasNegocio(unittest.TestCase):

    def setUp(self):
        self.d = DESAFIO_SIMULADO

    def test_pelo_menos_2_pistas(self):
        self.assertGreaterEqual(len(self.d['pistas']), 2)

    def test_pelo_menos_3_casos(self):
        self.assertGreaterEqual(len(self.d['casos_de_teste']), 3)

    def test_casos_tem_entrada_e_saida(self):
        for i, c in enumerate(self.d['casos_de_teste']):
            self.assertIn('entrada', c, f"caso {i} sem 'entrada'")
            self.assertIn('saida',   c, f"caso {i} sem 'saida'")

    def test_pelo_menos_1_criterio(self):
        self.assertGreaterEqual(len(self.d['criterios']), 1)

    def test_xp_positivo(self):
        self.assertGreater(self.d['xp'], 0)

    def test_titulo_menciona_tecnologia(self):
        self.assertIn('Python', self.d['titulo'])

    def test_titulo_menciona_nivel(self):
        self.assertIn('Iniciante', self.d['titulo'])

    def test_dificuldade_iniciante_1_estrela(self):
        self.assertIn('⭐', self.d['dificuldade'])
        # Iniciante: apenas 1 estrela preenchida
        self.assertEqual(self.d['dificuldade'].count('⭐'), 1)


class TestTiposDeMissao(unittest.TestCase):

    TIPOS_VALIDOS = {
        'Algoritmo', 'Estrutura de Dados', 'API/Integração',
        'Lógica', 'Mini-Projeto', 'Refatoração', 'Caça ao Bug'
    }

    def test_tipo_valido(self):
        self.assertIn(DESAFIO_SIMULADO['tipo'], self.TIPOS_VALIDOS)


class TestEntradaSaida(unittest.TestCase):

    def setUp(self):
        self.d = DESAFIO_SIMULADO

    def test_entrada_nao_vazia(self):
        self.assertGreater(len(self.d['entrada']), 0)

    def test_saida_esperada_correta(self):
        self.assertEqual(self.d['saida_esperada'], [2, 4, 6, 8])

    def test_saida_e_lista(self):
        self.assertIsInstance(self.d['saida_esperada'], list)

    def test_saida_ordenada_crescente(self):
        s = self.d['saida_esperada']
        self.assertEqual(s, sorted(s))


class TestDesafioLendario(unittest.TestCase):

    def setUp(self):
        self.d = DESAFIO_SIMULADO

    def test_desafio_lendario_string(self):
        self.assertIsInstance(self.d['desafio_lendario'], str)
        self.assertGreater(len(self.d['desafio_lendario']), 0)

    def test_desafio_lendario_diferente_narrativa(self):
        self.assertNotEqual(self.d['desafio_lendario'], self.d['narrativa'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
