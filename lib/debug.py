#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

# Creating 5 instances of the Author class
author1 = Author("Jane Austen")
author2 = Author("Mark Twain")
author3 = Author("Charles Dickens")
author4 = Author("George Orwell")
author5 = Author("Virginia Woolf")

# Creating 5 instances of the Magazine class
magazine1 = Magazine("National Geo", "Science")
magazine2 = Magazine("Time", "News")
magazine3 = Magazine("Vogue", "Fashion")
magazine4 = Magazine("The New Yorker", "Culture")
magazine5 = Magazine("Forbes", "Business")

# Creating instances of Article
article1 = Article(author1, magazine1, "Exploring the Natural World")
article2 = Article(author2, magazine2, "The Changing Times")
article3 = Article(author3, magazine3, "The Fashion of the Past")
article4 = Article(author4, magazine4, "Cultural Shifts")
article5 = Article(author5, magazine5, "The Business of Writing")



if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
