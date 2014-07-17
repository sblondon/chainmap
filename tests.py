import unittest

import chainmap

class TestInit(unittest.TestCase):
    def test_accept_n_dicts(self):
        chainmap.ChainMap()
        chainmap.ChainMap({})
        chainmap.ChainMap({}, {})
        chainmap.ChainMap({}, {}, {})

    def test_get_item(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEqual(1, cm["a"])
        self.assertEqual(3, cm["b"])
        with self.assertRaises(KeyError):
            cm["d"]


class TestMapsAttribute(unittest.TestCase):
    def test_slice(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEqual({'a': 1}, cm.maps[0])
        self.assertEqual({'a': 2, 'b': 3}, cm.maps[1])
        self.assertEqual({'a': 2, 'b': 3}, cm.maps[-1])

        with self.assertRaises(IndexError):
            cm.maps[2]

    def test_index_0_always_exists(self):
        cm = chainmap.ChainMap()

        self.assertEqual({}, cm.maps[0])


class TestNewChild(unittest.TestCase):
    def test_no_param(self):
        cm = chainmap.ChainMap({'brian': "wanda"})

        cm_copy = cm.new_child()

        self.assertEqual(({}, {"brian": "wanda"}), cm_copy.maps)
        self.assertNotEqual(id(cm), id(cm_copy))

    def test_with_param(self):
        cm = chainmap.ChainMap({'brian': "wanda"})

        cm_copy = cm.new_child({"spam": "SPAM"})

        self.assertEqual(({"spam": "SPAM"}, {"brian": "wanda"}), cm_copy.maps)
        self.assertNotEqual(id(cm), id(cm_copy))


class TestParents(unittest.TestCase):
    def test_empty(self):
        cm = chainmap.ChainMap()

        cm_parent = cm.parents

        self.assertEqual([{}], cm_parent.maps)
        self.assertNotEqual(id(cm), id(cm_parent))

    def test_with_param(self):
        cm = chainmap.ChainMap({'brian': "wanda"}, {"spam": "SPAM"}, {'holy': "graal"})

        cm_parent = cm.parents

        self.assertEqual(({"spam": "SPAM"}, {'holy': "graal"}), cm_parent.maps)
        self.assertNotEqual(id(cm), id(cm_parent))


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
        self.assertIn("a", cm)

    def test_does_not_exist(self):
        cm = chainmap.ChainMap()

        with self.assertRaises(KeyError):
            del cm["a"]


class TestInOperator(unittest.TestCase):
    def test_success(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertIn("a", cm)
        self.assertIn("b", cm)

    def test_failure(self):
        cm = chainmap.ChainMap()

        self.assertNotIn("a", cm)


class TestCastToList(unittest.TestCase):
    def test_success(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3}, {"c": "monty"})

        l = list(cm)

        self.assertEqual(set(["a", "b", "c"]), set(l)) #ordre important?
        self.assertIn("b", cm)


class TestLength(unittest.TestCase):
    def test_empty(self):
        cm = chainmap.ChainMap()

        self.assertEqual(0, len(cm))

    def test_filled(self):
        cm = chainmap.ChainMap({"a": 1}, {"a": 2, "b": 3})

        self.assertEqual(2, len(cm))


class TestCastToBool(unittest.TestCase):
    def test_empty(self):
        cm = chainmap.ChainMap()

        self.assertFalse(bool(cm))

    def test_filled(self):
        cm = chainmap.ChainMap({"a": 1})

        self.assertTrue(bool(cm))


class TestItems(unittest.TestCase):
    def test(self):
        cm = chainmap.ChainMap({'d': 567, 'a': 'e'}, {'d': 34}, {'f': 45})

        for k, v in cm.items():
            self.assertIn((k, v), (("d", 567), ("a", 'e'), ("f", 45)))
            self.assertFalse((k == "d" and v == 34))


if __name__ == '__main__':
    unittest.main()

