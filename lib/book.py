#!/usr/bin/env python3
#Setting the class
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    #Using the property decorator to come up with the getter and setter
    @property    
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
