import unittest
from yandex import YaUploader


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown --> work")

    def test_get_a_folder_response_status(self):
        self.assertAlmostEqual(yandex_user1.get_a_folder(), 201)
        self.assertAlmostEqual(yandex_user1.get_a_folder(), 409)

    def test_get_folders_list(self):
        self.assertIn('backup', yandex_user1.get_folders_list())


if __name__ == '__main__':
    yandex_user1 = YaUploader()
    unittest.main()