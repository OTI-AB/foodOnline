from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **bwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile created')
    else:
        try:            
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # no user profile...create it!
            UserProfile.objects.create(user=instance)
            print('no user profile, so created it')
        print('user profile not created...maybe updated')

# post_save.connect(post_save_create_profile_receiver, User)

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'user being saved')