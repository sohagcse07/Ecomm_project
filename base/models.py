from django.db import models
import uuid

class BaseModel(models.Model):

      # প্রতিটি মডেলের জন্য একটি ইউনিক UUID
    uid = models.UUIDField(primary_key=True, editable=False , default=uuid.uuid4)

     # মডেল আপডেট হলেই created_at আপডেট হবে (actually updated_at er moto behave korche)
    created_at = models.DateTimeField(auto_now = True)

     # মডেল প্রথমবার তৈরি হলে updated_at সেট হবে
    updated_at = models.DateTimeField( auto_now_add = True)


    class Meta: #class Meta hocche Django model-er ekta control room – jekhane model-ta kibhabe behave korbe, seta specify kora jai
        abstract = True
