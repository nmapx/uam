# -*- coding: utf-8 -*-

"""
Zadanie 602

Napisz funkcję `featprob(bayes, feature, category)`, która oblicza
prawdopodobieństwo P(F=f|C=c) dla danej cechy (`feature`) i danej
kategorii (`category`). Prawodpodobieństwo warunkowe obliczamy,
dzieląc liczbę współwystępowania cechy `feature` z kategorią
`category` przez liczbę występowania kategorii `category`. Funkcja
zwraca prawdopodobieństwo w postaci logarytmu. Jeżeli dana kategoria
nie istnieje, zwracamy -1e300 (liczba możliwie bliska log(0) = -inf).
Jeśli nie istnieje dana cecha (dla danej kategorii), to zwracamy
logarytm ilorazu liczby 0.001 oraz liczby występowania kategorii
(wygładzanie).

NAME: featprob
PARAMS: NaiveBayes, string, string
RETURN: float
POINTS: 5
"""

import unittest
import NaiveBayes
from Task602 import featprob

class Task602Test(unittest.TestCase):
    """Testy do zadania Task602."""

    def test(self):
        """Test na sztucznych danych."""

        def getfeatures(text):
            """Funkcja do testów."""
            return list(set(text.split()))

        bayes = NaiveBayes.NaiveBayes(getfeatures)

        bayes.feature_count = {('terms,', 'C1'): 1, ('considers', 'C2'): 1,
                    ('independently', 'C3'): 1, ('each', 'C1'): 1,
                    ('that', 'C1'): 1, ('the', 'C3'): 1, ('on', 'C1'): 1,
                    ('features', 'C1'): 1, ('and', 'C3'): 1, ('is', 'C2'): 1,
                    ('feature.', 'C2'): 1, ('For', 'C2'): 1, ('fruit', 'C2'): 1,
                    ('features,', 'C2'): 1, ('classifier', 'C2'): 1,
                    ('(or', 'C2'): 2, ('these', 'C1'): 1, ('the', 'C2'): 2,
                    ('particular', 'C2'): 1, ('may', 'C2'): 1,
                    ('Bayes', 'C2'): 1, ('all', 'C2'): 1, ('feature', 'C2'): 1,
                    ('apple', 'C3'): 1, ('naive', 'C2'): 1, ('depend', 'C1'): 1,
                    ('other', 'C2'): 2, ('if', 'C3'): 1,
                    ('contribute', 'C3'): 1, ('any', 'C2'): 1,
                    ('these', 'C2'): 1, ('4"', 'C3'): 1,
                    ('classifier', 'C1'): 1, ('other', 'C1'): 1,
                    ('of', 'C1'): 1, ('assumes', 'C1'): 1,
                    ('Bayes', 'C1'): 1, ('Even', 'C1'): 1,
                    ('presence', 'C1'): 1, ('the', 'C1'): 2,
                    ('a', 'C2'): 3, ('upon', 'C1'): 1,
                    ('that', 'C3'): 1, ('example,', 'C2'): 1,
                    ('properties', 'C3'): 1, ('this', 'C3'): 1,
                    ('to', 'C2'): 1, ('In', 'C1'): 1,
                    ('round,', 'C3'): 1, ('about', 'C3'): 1,
                    ('absence)', 'C2'): 2, ('of', 'C2'): 3,
                    ('diameter.', 'C3'): 1,
                    ('existence', 'C1'): 1, ('be', 'C3'): 1,
                    ('considered', 'C3'): 1, ('a', 'C1'): 1,
                    ('it', 'C3'): 1, ('an', 'C3'): 1,
                    ('or', 'C1'): 1, ('if', 'C1'): 1,
                    ('presence', 'C2'): 1, ('is', 'C3'): 1,
                    ('to', 'C3'): 2, ('unrelated', 'C2'): 1,
                    ('red,', 'C3'): 1, ('probability', 'C3'): 1,
                    ('naive', 'C1'): 1, ('class', 'C2'): 1,
                    ('in', 'C3'): 1, ('simple', 'C1'): 1}

        bayes.class_count = {'C1': 2, 'C2': 3, 'C3': 2}

        feat_cats = [
            ('of', 'C2'), ('to', 'C3'), ('features', 'C1'),
            ('Bayes', 'C1'), ('of', 'C1'),
            ('to', 'C5'), ('features', 'C3'), ('Bayes', 'C2')]
        probs = [0.0, 0.0, -0.6931,
                 -0.6931, -0.6931,
                 -1e+300, -7.6009, -1.0986]

        for idx in range(len(feat_cats)):
            self.assertAlmostEqual(
                featprob(bayes, feat_cats[idx][0], feat_cats[idx][1]),
                probs[idx], 4)

if __name__ == '__main__':
    unittest.main()
