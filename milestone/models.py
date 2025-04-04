from django.db import models

class Milestone(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='milestones/', null=True, blank=True)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class MilestoneImage(models.Model):
    milestone = models.ForeignKey(Milestone, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='milestone_images/')

    def __str__(self):
        return f"Image for {self.milestone.title}"
