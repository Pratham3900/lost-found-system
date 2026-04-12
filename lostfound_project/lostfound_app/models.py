from django.db import models

class LostItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    lost_date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    status = models.CharField(max_length=20, default='Lost')

    def __str__(self):
        return self.item_name


class FoundItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    found_date = models.DateField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    finder_name = models.CharField(max_length=100)
    finder_email = models.EmailField()
    status = models.CharField(max_length=20, default='Found')

    def __str__(self):
        return self.item_name


class ClaimRequest(models.Model):
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    claimant_name = models.CharField(max_length=100)
    claimant_email = models.EmailField()
    proof_details = models.TextField()
    claim_status = models.CharField(max_length=20, default='Pending')
    handover_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.claimant_name


class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]