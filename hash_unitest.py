import unittest


def hash(num):
    s = ""
    refer = "acdegilmnoprstuw"
    for i in range(0, 9):
        if num > 37:
            k = num % 37
            s = refer[k] + s
            num = num / 37
        else:
            return s
    return s


class TestHash(unittest.TestCase):

    def test_hash1(self):
        res = hash(680131659347)
        self.assertEqual(res, "leepadg")

    def test_hash2(self):
        res = hash(485770598)
        self.assertEqual(res, "amlee")

    def test_hash3(self):
        res = hash(664596389836)
        self.assertEqual(res, "acdegil")

if __name__ == '__main__':
    unittest.main()
