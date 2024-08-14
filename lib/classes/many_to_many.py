
class Article:
    #class attribute 'all'
    all = [] 

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    #decorators for 'title'
    @property 
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        if (isinstance(value, str) and 5 <= len(value) <= 50 and not hasattr(self, 'title')):
            self._title = value 

    #decorators for 'author'
    @property
    def author(self):
        return self._author 
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value 

    #decorators for 'magazine'
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine): 
            self._magazine = value

    #repr for Article
    def __repr__(self):
        return f'<Article author={self.author} magazine={self.magazine} title={self.title} /> ' 
        
class Author:
    
    #class attribute 'all'
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self) 

    #decorators for 'name'
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and len(value) > 0 and not hasattr(self, 'name')):
            self._name = value
    
    #repr for Author
    def __repr__(self): 
        return f'<Author name={self.name} />'

    # method for articles
    # returning all articles associated with the author        
    def articles(self):
        return [article for article in Article.all if article.author == self]

    # method for magazines
    # returning a unique list of magazines matching the author 
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    #method for add_article 
    # returning a new instance of Article with 'name', 'magazine', 'title'
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # method for topic_areas
    # returning a unique list of categories that match the auther, if none, return None 
    def topic_areas(self):
         if not self.articles():
            return None
         return list(set([article.magazine.category for article in self.articles()]))


class Magazine:

    #class attribute 'all'
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    #decorators for name 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if (isinstance(value, str) and 2 <= len(value) <= 16): 
            self._name = value

    #decorators for category
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if (isinstance(value, str) and len(value) > 0): 
            self._category = value 

    #repr for Magazine
    def __repr__(self):
        return f'<Magazine name={self.name} category={self.category} />'

    # method for articles
    # returning all magazines associated with the author 
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # method for contributors 
    # return a unique list of authors that match magazine 
    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    # method for articles_titles
    # return a list of titles that were written by the magazine, if none, return None
    def article_titles(self):
        if not self.articles():
            return None 
        return [article.title for article in self.articles()]

    # method for contributing_authors
    # return a list of authors who have more than 2 articles, if less than 2, return None 
    def contributing_authors(self):
       if len([article.author for article in self.articles()]) <= 2:
            return None
       return [article.author for article in self.articles()]