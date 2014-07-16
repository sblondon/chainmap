import unittest

import chainmap

class TestChainMap(unittest.TestCase):
    def test_accept_n_dicts(self):
        chainmap.ChainMap()
        chainmap.ChainMap({})
        chainmap.ChainMap({}, {})
        chainmap.ChainMap({}, {}, {})

    def test_get_item(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEqual(1, cm["a"])
        self.assertEqual(3, cm["b"])
        try:
            cm["d"]
            self.fail("'d' key does not exist.")
        except KeyError:
            pass


class TestMapsAttribute(unittest.TestCase):
    def test_slice(self):
        c = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEqual({'a': 1}, c.maps[0])
        self.assertEqual({'a': 2, 'b': 3}, c.maps[1])
        self.assertEqual({'a': 2, 'b': 3}, c.maps[-1])
        try:
            c.maps[2]
            self.fail("Index invalid")
        except IndexError:
            pass

    def test_index_0_always_exists(self):
        cm = chainmap.ChainMap()

        self.assertEqual({}, cm.maps[0])


class TestSetItem(unittest.TestCase):
    def test_in_first_mapping(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        cm["a"] = "blurp"

        self.assertEqual("blurp", cm["a"])
        self.assertEqual(2, cm.maps[1]['a'])

    def test_in_other_mapping(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        cm["b"] = "cheese"

        self.assertEqual("cheese", cm["b"])
        self.assertEqual("cheese", cm.maps[0]['b'])
        self.assertEqual(3, cm.maps[1]['b'])

    def test_new_value(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        cm["c"] = "spam"

        self.assertEqual("spam", cm["c"])


class TestDeleteItem(unittest.TestCase):
    def test_in_first_mapping(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        del cm["a"]

        self.assertEqual(2, cm["a"])
        self.assertTrue("a" in cm)

    def test_does_not_exist(self):
        cm = chainmap.ChainMap()
        try:
            del cm["a"]
            self.fail("Deleting an non-existant attribute is not possible.")
        except KeyError:
            pass


class TestInOperator(unittest.TestCase):
    def test_success(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertTrue("a" in cm)
        self.assertTrue("b" in cm)

    def test_failure(self):
        cm = chainmap.ChainMap()

        self.assertFalse("a" in cm)

class TestCastToList(unittest.TestCase):
    def test_success(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3}, {"c": "monty"})

        l = list(cm)

        self.assertEquals(set(["a", "b", "c"]), set(l)) #ordre important?
        self.assertTrue("b" in cm)


class TestLength(unittest.TestCase):
    def test_empty(self):
        cm = chainmap.ChainMap()

        self.assertEquals(0, len(cm))

    def test_filled(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEquals(2, len(cm))


class TestCastToBool(unittest.TestCase):
    def test_empty(self):
        cm = chainmap.ChainMap()

        self.assertFalse(bool(cm))

    def test_filled(self):
        cm = chainmap.ChainMap({"a": 1})

        self.assertTrue(bool(cm))


if __name__ == '__main__':
    unittest.main()

