from django.db import models,connection


class BooksDetails(models.Model):
    bk_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'book_db'

    def __str__(self):
        return self.bk_name,self.author_name,self.quantity






# Create your models here.
