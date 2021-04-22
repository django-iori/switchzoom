from django import forms

sex={
    ('男性','男性'),
    ('女性','女性')
}

event={
    ('５月７日','５月７日'),
    ('５月１４日','５月１４日'),
    ('５月２１日','５月２１日')
}

class RegisterForm(forms.Form):

    email = forms.EmailField(
        label='メールアドレス', 
        required=True    
    )

    gender = forms.ChoiceField(
        label='性別',
        widget=forms.RadioSelect,
        choices=sex, 
        required=True
        )

    age = forms.IntegerField(
        label='年齢',
        required=True
    )

    university = forms.CharField(
        label='大学名',
        max_length=50, 
        required=True
        )
    
    event = forms.ChoiceField(
        label='参加日程',
        widget=forms.RadioSelect,
        choices=event, 
        required=True
        )