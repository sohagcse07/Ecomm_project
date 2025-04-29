from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails  import send_account_activation_email
# Create your models here.



class Profile ( BaseModel):

    user = models.OneToOneField( User , on_delete= models.CASCADE , related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField( max_length= 100 , null= True , blank= True)
    profile_image = models.ImageField( upload_to= "Profile" , null=True , blank=True)



@receiver ( post_save , sender = User)

def send_email_token ( sender , instance , created , **kwargs):

    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create( user = instance , email_token = email_token)
            send_account_activation_email (instance.email , email_token)
            
    except Exception as e:
        print(f"Error sending email: {str(e)}")