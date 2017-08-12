from django.test import TestCase
from upload import utils


class TestCalls(TestCase):
    def test_csv_validate_uploaded_fields_correct_ordered(self):
        fields_read_in_ordered = ('first_value', 'second_value', 'third_value')
        required_fields = ('first_value', 'second_value', 'third_value')

        self.assertTrue(utils.csv_validate_uploaded_fields(fields_read_in_ordered, required_fields))

    def test_csv_validate_uploaded_fields_correct_unordered(self):
        fields_read_in_unordered = ('second_value', 'first_value', 'third_value')
        required_fields = ('first_value', 'second_value', 'third_value')

        self.assertTrue(utils.csv_validate_uploaded_fields(fields_read_in_unordered, required_fields))

    def test_csv_validate_uploaded_fields_incorrect(self):
        field_read_in_wrong = ('second_value', 'first_value', 'foo')
        required_fields = ('first_value', 'second_value', 'third_value')

        self.assertFalse(utils.csv_validate_uploaded_fields(field_read_in_wrong, required_fields))

    def test_validate_file_extension(self):
        read_in_extension = 'test.csv'
        expected = ('csv', 'txt')

        self.assertTrue(utils.validate_file_extension(read_in_extension, expected))



