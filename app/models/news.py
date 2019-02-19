class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,author,url,urlToImage,publishedAt):
        self.title = title
        self.author =author
        self.url =url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt