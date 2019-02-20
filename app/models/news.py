class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        # self.urlToImage = urlToImage
        # self.publishedAt = publishedAt

class Articles:
    '''
    Article class to define article objects
    '''

    def __init__(self,id,title,name,url,urlToImage,publishedAt):
        self.id = id
        self.title = title
        self.name =name
        self.url =url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt