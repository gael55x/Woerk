from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model


class CustomUser(AbstractUser):
    # Add any additional fields related to the user here
    pass

# Freelancer model


class Freelancer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    RANK_CHOICES = (
        ('D', 'D'),
        ('C', 'C'),
        ('B', 'B'),
        ('A', 'A'),
        ('S', 'S'),
        ('S+', 'S+'),
        ('SS', 'SS'),
        ('SS+', 'SS+'),
        ('SSS', 'SSS'),
    )

    name = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.PositiveIntegerField()
    rank = models.CharField(choices=RANK_CHOICES, max_length=3)

# Portfolio model


class Portfolio(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_images = models.ImageField(upload_to='portfolios/')

# Collaborative Project model


class CollaborativeProject(models.Model):
    title = models.CharField(max_length=100)
    client = models.ForeignKey('ClientCompany', on_delete=models.CASCADE)
    freelancers = models.ManyToManyField(Freelancer)
    milestones = models.TextField()
    is_completed = models.BooleanField(default=False)

# Client Company model


class ClientCompany(models.Model):
    name = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

# Job Recommendation model


class JobRecommendation(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    recommended_jobs = models.ManyToManyField('JobOpportunity')

# Job Opportunity model


class JobOpportunity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField()
    client = models.ForeignKey(ClientCompany, on_delete=models.CASCADE)
    is_filled = models.BooleanField(default=False)

# Proposal model


class Proposal(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    job_opportunity = models.ForeignKey(
        JobOpportunity, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    documents = models.FileField(upload_to='proposals/')
    is_accepted = models.BooleanField(default=False)

# Discussion Forum model


class DiscussionForum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# Discussion Post model


class DiscussionPost(models.Model):
    forum = models.ForeignKey(DiscussionForum, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    content = models.TextField()

# Mentorship Program model


class MentorshipProgram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

# Mentorship Enrollment model


class MentorshipEnrollment(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    program = models.ForeignKey(MentorshipProgram, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField(default=False)

# Industry-specific Group model


class IndustryGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Freelancer)

# Client Verification model


class ClientVerification(models.Model):
    client = models.ForeignKey(ClientCompany, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)
