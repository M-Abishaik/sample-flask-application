from tests.unit.unit_base_test import UnitBaseTest
from models.item import ItemModel


class ItemTest(UnitBaseTest):

    def test_create_item(self):
        item_object = ItemModel("mobile", 1000.25, 1)

        self.assertEqual("mobile", item_object.name,  "Names of the items don't equal the constructor argument.")
        self.assertEqual(1000.25, item_object.price, "Price of the items don't equal the constructor argument.")
        self.assertEqual(1, item_object.store_id, "ID's of the items don't equal the constructor argument.")
        self.assertIsNone(item_object.store)

    def test_create_json(self):
        item_object = ItemModel("mobile", 1000.25, 1)

        expected_item = {'name' : 'mobile', 'price' : 1000.25}
        self.assertDictEqual(expected_item, item_object.json())



