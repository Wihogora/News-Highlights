import unittest
from models import newsArticle
News = news.News

class newstest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("null","Flybmi won't be the last airline failure, say analysts",
        "Bbc.com",
        "https://www.bbc.com/news/business-47278322",
        "https://ichef.bbci.co.uk/news/1024/branded_news/14D8B/production/_105678358_baafb154-e8e3-4a58-b9d8-300a28470404.jpg",
        "2019-02-18T13:40:30Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()