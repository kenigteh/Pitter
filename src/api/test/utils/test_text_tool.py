from django.test import SimpleTestCase
from .data.text_tool import POSITIVE_CASES
from api.utils.text_tool import reverse


class ReverseTestCase(SimpleTestCase):
    def test_positive_cases(self):
        for case, result in POSITIVE_CASES.items():
            self.assertEqual(
                reverse(case),
                result
            )

    def test_negative_cases(self):
        pass
