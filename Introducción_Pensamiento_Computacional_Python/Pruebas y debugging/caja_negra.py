import unittest
def suma(num1,num2):
	return num1 + num2

class CajaNegraTest(unittest.TestCase):
	def test_suma_dos_positivos(self):
		num1 = 10
		num2 = 5
		resultado = suma(num1 ,num2)
		self.assertEqual(resultado , 15)
	
	def test_suma_dos_negativos(self):
		num1 = -10
		num2 = -2
		resultado = suma(num1 ,num2)
		self.assertEqual(resultado , -12)
	
	def test_suma_negativo_positivo(self):
		num1 = -10
		num2 = 2
		resultado = suma(num1 ,num2)
		self.assertEqual(resultado , -8)

if __name__ == "__main__":
	unittest.main()
	