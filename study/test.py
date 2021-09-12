import unittest
from example import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_sigle_response(self):
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

# import unittest
# from example import get_formatted_name


# class NamesTestCase(unittest.TestCase):
#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')

#     def test_first_last_middle_name(self):
#         formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
