from django import forms
from .models import Student


class StudentPlacedForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'programs',
			'placed',
			'company',
			'sector',
			'profile',	
			'day',
			'slot',
		]
