# Son bunas para regression testing o mocks

import unittest

def es_mayor_de_edad(edad):
	if edad >= 18:
		return True
	else:
		return False

class PruebaDeCristalTest(unittest.TestCase):
	
	def test_mayor(self):
		edad = 18
		resultado = es_mayor_de_edad(edad)
		self.assertEqual(resultado ,True)
	
	def test_menos(self):
		edad = 17
		resultado = es_mayor_de_edad(edad)
		self.assertEqual(resultado ,False)

if __name__ == "__main__":
	unittest.main()