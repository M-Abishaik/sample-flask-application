from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('abishaik', '1234')

        self.assertEqual(user.username, 'abishaik', "Username doesn't match with the constructor argument.")
        self.assertEqual(user.password, '1234', "Password doesn't match with the constructor argument.")

