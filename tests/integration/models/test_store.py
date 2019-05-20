from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):

        store = StoreModel('Test')

        self.assertListEqual(store.items.all(), [], "Number of items weren't zero.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'),
                              "Found a store with name {}, but expected not to.".format('test'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('test', 20.00, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test')

    def test_store_empty_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(
            store.json(),
            expected,
            "The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))

    def test_store_json(self):
        with self.app_context():
            store = StoreModel('Test Store')
            item = ItemModel('test', 20.00, 1)
            item2 = ItemModel('test2', 19.00, 1)

            store.save_to_db()
            item.save_to_db()
            item2.save_to_db()


            expected = {
                'name': 'Test Store',
                'items': [{'name':'test', 'price':20.00}, {'name':'test2', 'price':19.00}]
            }

            self.assertDictEqual(store.json(), expected,
            "The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))

