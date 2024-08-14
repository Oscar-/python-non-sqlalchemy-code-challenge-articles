class Article:

    all = [] 

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property 
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        if (isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title')):
            self._title = value 

    @property
    def author(self):
        return self._author 
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value 

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine): 
            self._magazine = value

    def __repr__(self):
        return f'<Article author={self.author} magazine={self.magazine} title={self.title} /> ' 
        
class Author:
    
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self) 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name')):
            self._name = value
    
    def __repr__(self): 
        return f'<Author name={self.name} />'
           
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
         if not self.articles():
            return None
         return list(set([article.magazine.category for article in self.articles()]))


class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if (isinstance(value, str) and 2 <= len(value) <= 16): 
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if (isinstance(value, str) and len(value) > 0): 
            self._category = value 

    def __repr__(self):
        return f'<Magazine name={self.name} category={self.category} />'

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if not self.articles():
            return None 
        return [article.title for article in self.articles()]

    def contributing_authors(self):
       if len([article.author for article in self.articles()]) <= 2:
            return None
       return [article.author for article in self.articles()]