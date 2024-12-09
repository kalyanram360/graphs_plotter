from django import forms
import pandas as pd

# Load the dataset (replace with your path or database query)
data = pd.read_csv(r'C:\Users\KALYAN\Downloads\metadata.csv')  # Ensure this is accessible

class PlotForm(forms.Form):
    battery_id_choices = [(battery_id, battery_id) for battery_id in data['battery_id'].unique()]
    metric_choices = [('Re', 'Re'), ('Rct', 'Rct')]
    plot_type_choices = [('line', 'Line Plot'), ('bar', 'Bar Plot')]

    battery_id = forms.ChoiceField(choices=battery_id_choices, label="Battery ID")
    metric = forms.ChoiceField(choices=metric_choices, label="Metric")
    plot_type = forms.ChoiceField(choices=plot_type_choices, label="Plot Type")
