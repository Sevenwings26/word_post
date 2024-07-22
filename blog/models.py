from django.db import models

# models 
# preacher information
# category
# sermon content
# comment
# mediafile - for audio, video and transcript

# class Messaenger
class Preacher_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Sermon(models.Model):
    topic = models.CharField(max_length=120)
    preacher = models.ForeignKey(Preacher_info, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default='default-slug')
    content = models.TextField()
    image = models.ImageField(default='default.png', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    # transcript
    # duration

    def __str__(self):
        return self.topic


class Media_files(models.Model):
    pass # to add media files 


class Comment(models.Model):
    sermon = models.ForeignKey(Sermon, related_name='comments', on_delete=models.CASCADE)
    reader = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} commented on {self.sermon}"
    
