from django.db.models import fields
from seonjoo.pinProject.ahnlaber.profileapp.models import Profile
from django.forms.models import ModelForm


# class Meta: 까지 기본 형식
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = {'image', 'nickname', 'message'}  #user 라는 필드도 있지만, 그건 서버에서 처리할 것임
