from django.db import models

class Item(models.Model):
    text = models.TextField(default='')


# Pick this up with "Our First Database Migration" from
# URL: http://www.obeythetestinggoat.com/book/chapter_05.html
