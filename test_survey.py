#coding = utf-8

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """
            创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What's your hobblies?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Hiking', 'Fishing', 'Basketball', 'Football']

    def test_store_single_response_new(self):
        """测试单个答案会被妥善地处理"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_more_response_new(self):
        """测试多个答案会被妥善地处理"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_more_response(self):
        """测试多个答案会被妥善地存储"""
        question = "I want more than 2 words to store:"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('one')
        my_survey.store_response('two')
        my_survey.store_response('three')

        self.assertIn('one', my_survey.responses)
        self.assertIn('two', my_survey.responses)
        self.assertIn('three', my_survey.responses)

    

if __name__ == '__main__':
    unittest.main()
