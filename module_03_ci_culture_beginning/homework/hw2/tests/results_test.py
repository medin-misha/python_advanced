import unittest
#TODO
from ..decrypt import decrypt

class test_decoder(unittest.TestCase):
    def test_all_variants(self):
        variantsDict:dict = { #словарь в котором храняться все варианты ввода и все варианты вывода как ввод: вывод
            'абра-кадабра.': 'абра-кадабра',
            'абраа..-кадабра':'абра-кадабра',
            'абраа..-.кадабра':'абра-кадабра',
            "абра--..кадабра":'абра-кадабра',
            "абрау...-кадабра":'абра-кадабра',
            "абра........":'',
            'абр......a.':'a',
            '1..2.3':'23',
            '.':'',
            '1.......................':''
        }

        for input, output in variantsDict.items():
            function_res = decrypt(encryption = str(input))
            self.assertEqual(output, function_res)
