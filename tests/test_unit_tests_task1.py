import unittest
import accounting


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp --> work")

    def tearDown(self) -> None:
        print("tearDown --> work")

    def test_get_the_person_name(self):
        self.assertAlmostEqual(accounting.get_the_person_name(document_id="11-2"), "Геннадий Покемонов")

    def test_find_store_place(self):
        self.assertAlmostEqual(accounting.find_store_place(document_id="2207 876234"), "1")

    def test_withdraw_all_documents(self):
        self.assertAlmostEqual(accounting.withdraw_all_documents(), len(accounting.documents))

    def test_add_new_document(self):
        self.assertIn(accounting.add_new_document(shelf="3", type="passport", number="1337", name="Daniil"),
                               accounting.output_document_list())

    def test_dell_document(self):
        self.assertNotIn(accounting.dell_document(document_id="10006"), accounting.output_document_list())


if __name__ == '__main__':
    unittest.main()
