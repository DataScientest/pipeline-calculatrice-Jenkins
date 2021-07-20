import unittest 
import calc 

class Test(unittest.TestCase):
    """
    Tests pour les fonctions de calc
    """

    def test_add(self):
        """
        L'addition entre 2 et 6 doit donner 8.
        """
        self.assertEqual(calc.add("2","6"),8)    

    def test_add_str(self):
        """
        L'addition entre 2 et add ne doit rien retourner.
        """
        self.assertIsNone(calc.add("2","add"))    

    def test_add_float(self):
        """
        L'addition entre 2 float ne doit rien retourner.
        """
        self.assertIsNone(calc.add("2.2","4.5"))

    def test_sous(self):
        """
        La soustraction de 144 par 12 doit retourner 132.
        """
        self.assertEqual(calc.sous("144","12"),132)

    def test_sous_str(self):
        """
        La soustraction de 31 par - ne doit rien retourner.
        """
        self.assertIsNone(calc.sous("31","-"))

    def test_sous_float(self):        
        """
        La soustraction entre 2 float ne doit rien retourner.
        """
        self.assertIsNone(calc.sous("31.12","42.1"))

    def test_mult(self):
        """
        La multiplication de 13 par 13 doit retourner 169.
        """
        self.assertEqual(calc.mult("13","13"),169)

    def test_mult_str(self):
        """
        La multiplication entre mult et 18 ne doit rien retourner.
        """
        self.assertIsNone(calc.mult("mult","18"))

    def test_mult_float(self):
        """
        La multiplication entre 2 float ne doit rien retourner.
        """
        self.assertIsNone(calc.sous("0.5","2.8"))

    def test_div(self):
        """
        La division de 12 par 2 doit retourner 6.
        """
        self.assertEqual(calc.div("12","2"),6)

    def test_div_str(self):
        """
        La division de douze par deux ne doit rien retourner.
        """
        self.assertIsNone(calc.div("douze","deux"))

    def test_div_float(self):
        """
        La division entre 2 float ne doit rien retourner.
        """
        self.assertIsNone(calc.div("31.0","7.0"))

    def test_div_zero(self):
        """
        Une division par 0.
        """
        self.assertIsNone(calc.div("2","0"))

    def test_ope(self):
        """        
        La soustraction entre 12 et 2 doit retourner 10.
        """
        self.assertEqual(calc.sous("12","2"),10)

    def test_ope_erreur(self):
        """
        L'opérateur factoriel n'est pas pris en compte.
        """
        self.assertIsNone(calc.ope("!","2","3"))

    if __name__ == '__main__':
        unittest.main()