from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=60)
	birth_date = models.DateField()
	email = models.EmailField(blank=True)
	
	def __str__(self):
		return("{} {}".format(self.first_name, self.last_name))

class Publisher(models.Model):
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	website = models.URLField()
	
	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	date = models.DateField()
	
	def __str__(self):
		return self.title
