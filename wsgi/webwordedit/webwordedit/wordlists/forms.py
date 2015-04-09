from webwordedit.wordlists.models import *
from django.forms.models import *
from django.forms.models import BaseModelFormSet

class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['phrase'].required = False
            self.fields['phrase'].widget.attrs['readonly'] = True
            self.fields['id'].widget.attrs['readonly'] = True
            self.fields['id'].required = False
            self.fields['replacement_phrase'].required = False
            self.fields['valid_word'].required = False

    def clean(self):
        from django.core.exceptions import ValidationError
        cleaned_data = self.cleaned_data
        replace_phrase = cleaned_data.get("replacement_phrase")
        discard_word_val = False
        try:
            discard_word_val= self.data[self.prefix+'-discard_word']
        except:
            discard_word_val = False
        if discard_word_val == u'on':
            discard_word_val = True
        valid_word = False
        try:
            valid_word = self.data[self.prefix+'-valid_word']
        except:
            valid_word = False
        if valid_word == u'on':
            valid_word = True
        # All fields are empty
        if (replace_phrase == u'' or replace_phrase == None) and (not discard_word_val)and (not valid_word ):
            raise ValidationError('You need to select atleast one field')
        # All fields are checked 
        if (replace_phrase) and (discard_word_val)and (valid_word ):
            raise ValidationError('You can not selet all fields')
        if (replace_phrase) and (discard_word_val):
            raise ValidationError('You can not select Replacement field and Discard word field at the same time')
        if (replace_phrase) and  (valid_word ):
            raise ValidationError('You can not select  Replacement field and Valid word field at the same time')
        if (discard_word_val)and (valid_word ):
            raise ValidationError('You can not select Discard Word and Valid word field at the same time')
        return cleaned_data


class Un_Verified_bn_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_bn_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_bn_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')


class Un_Verified_mr_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_mr_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_mr_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_da_dk_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_da_dk_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_da_dk
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_de_de_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_de_de_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_de_de
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')


class Un_Verified_te_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_te_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_te_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_ta_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_ta_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_ta_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_hi_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_hi_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_hi_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')


class Un_Verified_as_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_as_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_as_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_pa_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_pa_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_pa_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_gu_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_gu_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_gu_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_kn_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_kn_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_kn_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_ml_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_ml_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_ml_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class Un_Verified_or_in_form(BaseForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_or_in_form, self).__init__(*args, **kwargs)

    class Meta:
        model = Un_Verified_or_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word')
        exclude = ('time','verified_by_usr','verified_by_admin',
                   'author','author_email','admin_name','admin_email','admin_time')

class BaseAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseAdminForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['phrase'].required = False
            self.fields['phrase'].widget.attrs['readonly'] = True
            self.fields['id'].widget.attrs['readonly'] = True
            self.fields['id'].required = False
            self.fields['replacement_phrase'].required = False
            self.fields['valid_word'].required = False
            self.fields['author'].required = False
            self.fields['author_email'].required = False

    def clean(self):
        from django.core.exceptions import ValidationError
        cleaned_data = self.cleaned_data
        replace_phrase = cleaned_data.get("replacement_phrase")
        discard_word_val = False
        try:
            discard_word_val= self.data[self.prefix+'-discard_word']
        except:
            discard_word_val = False
        if discard_word_val == u'on':
            discard_word_val = True
        valid_word = False
        try:
            valid_word = self.data[self.prefix+'-valid_word']
        except:
            valid_word = False
        if valid_word == u'on':
            valid_word = True
        if (replace_phrase == u'' or replace_phrase == None) and (not discard_word_val) and (not valid_word):
            raise ValidationError('You need to select atleast one field')
        if (replace_phrase) and (discard_word_val)and (valid_word ):
            raise ValidationError('You can not select all fields')
        if (replace_phrase) and (discard_word_val):
            raise ValidationError('You can not select Replacement field and Discard word field at the same time')
        if (replace_phrase) and  (valid_word ):
            raise ValidationError('You can not select  Replacement field and Valid word field at the same time')
        if (discard_word_val)and (valid_word ):
            raise ValidationError('You can not select Discard Word and Valid word field at the same time')
        return cleaned_data


class Un_Verified_bn_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_bn_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_bn_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_mr_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_mr_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_mr_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_da_dk_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_da_dk_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_da_dk
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_de_de_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_de_de_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_de_de
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')


class Un_Verified_te_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_te_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_te_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')


class Un_Verified_ta_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_ta_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_ta_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_as_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_as_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_as_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_gu_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_gu_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_gu_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_hi_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_hi_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_hi_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')


class Un_Verified_pa_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_pa_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_pa_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_or_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_or_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_or_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_ml_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_ml_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_ml_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')

class Un_Verified_kn_in_admin_form(BaseAdminForm):
    def __init__(self, *args, **kwargs):
        super(Un_Verified_kn_in_admin_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Un_Verified_kn_in
        fields = ('id','phrase','replacement_phrase','discard_word','valid_word','author','author_email')
        exclude = ('time','verified_by_usr','verified_by_admin','admin_name','admin_email','admin_time')
