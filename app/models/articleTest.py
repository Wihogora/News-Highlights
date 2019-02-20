import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''Test class to test the behaviour of the Article class'''

    def setUp(self):
        '''method that will run before each test case'''
        self.new_articles = Articles("Samsung's Galaxy S10 may come with a cryptocurrency wallet",
        "Mashable",
        "https://mashable.com/article/samsung-galaxy-s10-cryptocurrency-wallet/",
        "https://mondrian.mashable.com/2019%252F01%252F24%252F07%252Fd88ec3acacbf4ece9690976e46226739.929b8.jpg%252F1200x630.jpg?signature=vZHMmpaeesKIQJm_5crpQH-GlIQ=,'https://cnet4.cbsistatic.com/img/ZBhDBbHH44bcXii1YC6Vkqf4p_U=/724x407/2018/12/11/e850b2b2-2ffc-4984-af8a-09a59cbffcb2/iphone-se-1.jpg",
        "2019-01-24T08:49:14Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
    unittest.main()