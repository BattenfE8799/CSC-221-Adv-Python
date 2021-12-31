# -*- coding: utf-8 -*-
"""
Notes 
v 1.1 added notes on dataclasses (frorm https://www.youtube.com/watch?v=vBH6GRJ1REM&t=86s )
"""

from dataclasses import dataclass, astuple, asdict, field
import inspect
from pprint import pprint

@dataclass(frozen=True, order=True) #immutable with frozen =true
class Comment:
    id: int
    text: str
    replies: list[int] = field(default_factory=list, compare=False)
    #^feild function takes other arguements to modify to how each attribute acts with respect to things like hash or order
    
    
    
    
def main():
    comment = Comment(1, "I just subscribed!")
    print(comment)
    #print(astuple(comment))
    #print(asdict(comment))
    pprint(inspect.getmembers(Comment, inspect.isfunction))
    
if __name__ == '__main__':
    main()
    
#attrs library is same but with slightly different names.
#addrs allow you to specifieces validators or converters, and slots (instead of instance dictionaries)
#not built into python


