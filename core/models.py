from django.db import models




class Category(models.Model):
    category_name =  models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='categories', blank=True)

   
    

    # def get_url(self):
    #     return reverse('category_name',  args=[self.slug])

    def __str__(self):
        return self.category_name