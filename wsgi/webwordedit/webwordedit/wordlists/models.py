from django.db import models

# Create your models here.

class Verified_bn_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True)

class Verified_mr_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True)

class Verified_de_de(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True)

class Verified_da_dk(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_hi_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_or_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_gu_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_ml_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_kn_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_pa_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_ta_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_te_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Verified_as_in(models.Model):
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(null=True) 

class Un_Verified_bn_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)
 
class Un_Verified_mr_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_de_de(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_da_dk(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_hi_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)


class Un_Verified_gu_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_or_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)


class Un_Verified_pa_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_ta_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Un_Verified_te_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)


class Un_Verified_ml_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)


class Un_Verified_as_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)


class Un_Verified_kn_in(models.Model):
    id = models.IntegerField(primary_key=True)
    phrase =  models.CharField(max_length=250)
    author =  models.CharField(max_length=30,null=True)
    time = models.DateField(auto_now=True,null=True)
    replacement_phrase = models.CharField(max_length=250,null=True)
    verified_by_usr =  models.BooleanField()
    verified_by_admin =  models.BooleanField()
    discard_word =  models.BooleanField()
    valid_word =  models.BooleanField()
    author_email = models.EmailField(null=True)
    admin_name =  models.CharField(max_length=30,null=True)
    admin_email = models.EmailField(null=True)
    admin_time = models.DateField(auto_now=True,null=True)

class Langauges(models.Model):
    language = models.CharField(max_length=30)
    lang_code = models.CharField(max_length=30)

class Locales(models.Model):
    #lang_code = models.ForeignKey(Langauges)
    lang_code = models.CharField(max_length=30)
    locale = models.CharField(max_length=30)
    
