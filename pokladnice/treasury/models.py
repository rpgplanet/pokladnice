from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

def get_file_path(instance, filename):
    from os.path import join
    return join(instance.user.username, filename)

class UploadedFile(models.Model):
    file = models.FileField(_('File path'), upload_to=get_file_path)
    user = models.ForeignKey(User)
    size = models.IntegerField()
