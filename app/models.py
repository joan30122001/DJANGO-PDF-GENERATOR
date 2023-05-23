from django.db import models



class Template(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='template', null=True, blank=True)

    def __str__(self):
        return self.name



class Cover(models.Model):
    template = models.ForeignKey('Template', on_delete=models.CASCADE)
    theme = models.CharField(max_length=1000, blank=True)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)

    def __str__(self):
        return self.theme



class Title(models.Model):
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title



class SubTitle(models.Model):
    title = models.ForeignKey('Title', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.subtitle



class BoardTitle(models.Model):
    subtitle = models.ForeignKey('SubTitle', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title



class BoardElement(models.Model):
    boardtitle = models.ForeignKey('BoardTitle', on_delete=models.CASCADE)
    element = models.CharField(max_length=200, blank=True)