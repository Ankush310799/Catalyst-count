from django import forms
from .models import Company


class QueryForm(forms.Form):
    keyword = forms.CharField(max_length=255, required=False)
    industry = forms.ModelChoiceField(queryset=None, empty_label="Select Industry", required=False)
    year_founded = forms.ModelChoiceField(queryset=None, empty_label="Year Founded", required=False)
    city = forms.ModelChoiceField(queryset=None, empty_label="City", required=False)
    state = forms.ModelChoiceField(queryset=None, empty_label="State", required=False)
    country = forms.ModelChoiceField(queryset=None, empty_label="Country", required=False)
    employees_from = forms.ModelChoiceField(queryset=None, empty_label="Employees From", required=False)
    employees_to = forms.ModelChoiceField(queryset=None, empty_label="Employees To", required=False)


    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)
        
        # Set queryset for industry dynamically
        self.fields['industry'].queryset = Company.objects.values_list('industry', flat=True).distinct()
        self.fields['year_founded'].queryset = Company.objects.values_list('year_founded', flat=True).distinct()
        self.fields['city'].queryset = Company.objects.values_list('country', flat=True).distinct()
        self.fields['state'].queryset = Company.objects.values_list('country', flat=True).distinct()
        self.fields['country'].queryset = Company.objects.values_list('country', flat=True).distinct()
        self.fields['employees_from'].queryset = Company.objects.values_list('current_employee_estimate', flat=True).distinct()
        self.fields['employees_to'].queryset = Company.objects.values_list('total_employee_estimate', flat=True).distinct()


    def clean(self):
        cleaned_data = super(QueryForm, self).clean()
        keyword = cleaned_data.get('keyword')

        selected_fields = [field for field in ['industry', 'year_founded', 'city', 'state', 'country', 'employees_from', 'employees_to'] if cleaned_data.get(field)]
        
        if not keyword and not selected_fields:
            raise forms.ValidationError("Please enter a keyword or select other search criteria.")
        
        if keyword:
            # If keyword is present, ignore other fields and return only the keyword
            return {'keyword': keyword}
        else:
            # If keyword is not present, return the other fields
            return {field: cleaned_data.get(field) for field in selected_fields}


class UploadFileForm(forms.Form):
    file = forms.FileField()



