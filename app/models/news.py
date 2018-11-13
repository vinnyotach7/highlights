class News:
    def __init__(self,name,url,description,urlToImage,publishedAt,content):
        self.name = name
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content =content
        self.url =url


class Articles:
    def __init__(self,name,description,url,category):
        self.name = name
        self.description = description
        self.url = url
        self.category = category