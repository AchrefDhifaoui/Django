from django.db import models


# Create your model


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Partenaire(models.Model):
    nom = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='PartenairePhoto/', blank=True)
    Partenaire_url = models.URLField(null=True)

    def __str__(self):
        return self.nom


class Service(models.Model):
    Services = [
        ("graphic design", "graphic design"),
        ("Web Design", "Web Design"),
        ("Vaudiovisual production", "audiovisual production"),
        (" Animation 3D ", "Animation 3D ")
    ]
    ServiceName = models.CharField(
        choices=Services, default=" Animation 3D", max_length=50)
    Ser_description = models.TextField(null=True)
    img = models.ImageField(upload_to='servicesPhoto/', blank=True)
    tag = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.ServiceName


class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    DONE = [
        ("Planning", "Planning"),
        ("In progress", "In progress"),
        ("Reviewing", "Reviewing"),
        ("Completed", "Completed"),
        ("Required", "Required"),
    ]
    libelle = models.CharField(max_length=50)
    type = models.ManyToManyField(Service, blank=True)
    description = models.TextField()

    image = models.ImageField(upload_to="photos/")
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True)
    dateD = models.DateField(auto_now_add=True)
    dateF = models.DateField(blank=True, null=True)
    status = models.CharField(choices=DONE, max_length=50, default="Required")

    def __str__(self):
        return self.libelle


class Personel(models.Model):
    POSTS = [
        ('Graphic Designer', 'Graphic Designer'),
        ('Web Designer', 'Web Designer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Creative Director', 'Creative Director'),
        ('Art Director', 'Art Director'),
        ('Copywriter', 'Copywriter'),
        ('Web Developer', 'Web Developer'),
    ]
    nom = models.CharField(max_length=50)
    file_cv = models.FileField(
        upload_to='cv/', max_length=100, blank=True)
    post = models.CharField(choices=POSTS, max_length=50,
                            default='Graphic Designer')
    photo = models.ImageField(upload_to='perPhoto/', blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)
    linkedin_url = models.URLField(null=True)
    fcb_url = models.URLField(null=True)
    github_url = models.URLField(null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Personnels"
