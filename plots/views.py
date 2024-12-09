from django.shortcuts import render
import pandas as pd
import plotly.express as px
from .forms import PlotForm


data = pd.read_csv(r"C:\Users\KALYAN\Downloads\metadata.csv")

def plot_view(request):
    plot_html = None  
    if request.method == "POST":
        form = PlotForm(request.POST)
        if form.is_valid():
            battery_id = form.cleaned_data['battery_id']
            metric = form.cleaned_data['metric']
            plot_type = form.cleaned_data['plot_type']

            
            filtered_data = data[data['battery_id'] == battery_id]

       
            if plot_type == 'line':
                fig = px.line(
                    filtered_data,
                    x='test_id',
                    y=metric,
                    title=f"{plot_type.capitalize()} Plot of {metric} for {battery_id}",
                    markers=True,
                    line_shape='spline'
                )
            elif plot_type == 'bar':
                fig = px.bar(
                    filtered_data,
                    x='test_id',
                    y=metric,
                    title=f"{plot_type.capitalize()} Plot of {metric} for {battery_id}",
                    orientation='v',
                )

            fig.update_layout(template='plotly_white')
            plot_html = fig.to_html(full_html=False)
    else:
        form = PlotForm()

    return render(request, 'plots/plot.html', {'form': form, 'plot_html': plot_html})
