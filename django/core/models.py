from django.db import models
from django.utils.timezone import now

# Create your models here.
class email_data(models.Model):
    r"""DB table to store all e-mail communication.

    In this table I will store the followin
    sender     -- Sender's email address
    receiver   -- Receiver's email address
    subject    -- Subject of the Message
    body       -- Body of the message
    send_time  -- Timestamp when the message was sent
    email_tag  -- Tag used for this message. Can be used for email. threads
    id         -- Primary Key field which will be Big-Auto
    """
    sender  = models.EmailField()
    recipient  = models.EmailField()
    subject = models.CharField(max_length=70)
    body = models.TextField()
    send_time = models.DateTimeField(default=now, blank=True)
    cc_myself = models.BooleanField()
    email_tag = models.CharField(max_length=32)
    id = models.BigAutoField(primary_key=True)
