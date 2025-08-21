class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title,str):
            return "title must be a string"
        if (2<= len(title) <= 16):
            return "title must have characters between 2 and 16"

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if hasattr(self,"_title"):
            return "title cannot be changed after instanciation"
        if not isinstance(value,str):
            return "title must be a string"
        if (2 <= len(value) <= 16):
            return "title must be a string of characters between 2 an 16"
        
        self._title = value
        
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            return "name must be of type str"
        if len(name) == 0:
            return "name must be longer than 0 characters"
        
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def title(self,value):
        if hasattr(self,"_name"):
            return "name cannot be changed after instanciation"
        if not isinstance(value,str):
            return "name must be a string"
        if (2 <= len(value) <= 16):
            return "name must be a string of more than one character"
        
        self._name = value
    

    def articles(self):
        [article for article in Article.all if article.author == self]
        return 

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass