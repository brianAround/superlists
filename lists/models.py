from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
# Pick this up with "Our First Database Migration" from
# URL: http://www.obeythetestinggoat.com/book/chapter_05.html
