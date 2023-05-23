from django import forms
from .models import Title, SubTitle, Template, Cover, BoardTitle, BoardElement



class CoverForm(forms.ModelForm):
    template = forms.ModelChoiceField(queryset=Template.objects.all(), help_text="Vérifier les différents template dans l'onglet Template afin de faire un choix.", widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Cover
        fields = [
            'template', 
            'theme',
            'logo',
        ]



class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = [
            'title', 
        ]



class SubTitleForm(forms.ModelForm):
    title = forms.ModelChoiceField(queryset=Title.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = SubTitle
        fields = [ 
            'title', 
            'subtitle',
            'description', 
            'image',
        ]



class RangeTitleForm(forms.Form):
    title = forms.ModelChoiceField(queryset=Title.objects.all())



class RangeSubTitleForm(forms.Form):
    subtitle = forms.CharField(max_length=100)
    description = forms.CharField(max_length=20000)
    image = forms.ImageField()
    title = forms.ModelChoiceField(queryset=Title.objects.all())



class BoardTitleForm(forms.ModelForm):
    subtitle = forms.ModelChoiceField(queryset=SubTitle.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = BoardTitle
        fields = [
            'subtitle',
            'title', 
        ]



class BoardElementForm(forms.ModelForm):
    boardtitle = forms.ModelChoiceField(queryset=BoardTitle.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = BoardElement
        fields = [
            'boardtitle',
            'element', 
        ]



class RangeBoardTitleForm(forms.Form):
    subtitle = forms.ModelChoiceField(queryset=SubTitle.objects.all())
    title = forms.ModelChoiceField(queryset=BoardTitle.objects.all())



class RangeBoardElementForm(forms.Form):
    boardtitle = forms.ModelChoiceField(queryset=BoardTitle.objects.all())
    element = forms.CharField(max_length=100)