from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse_lazy
from .models import Passenger, PredictionRecord
from .forms import PredictionForm

def home(request):
    return render(request, 'webapp/home.html',{'title':'home'})
class PredictionFormView(FormView):
    """
    View for the prediction form with SibSp dropdown
    """
    template_name = 'webapp/prediction_form.html'
    form_class = PredictionForm
    success_url = reverse_lazy('prediction_list')
    
    def form_valid(self, form):
        # Save the form data to database
        prediction = form.save(commit=False)
        
        # TODO: Integrate with ML model here
        # For now, set mock prediction values
        prediction.survived_prediction = prediction.sex == 'female'  # Mock logic
        prediction.probability = 0.72 if prediction.sex == 'female' else 0.18
        
        prediction.save()
        #return super().form_valid(form)
        return render(self.request, 'webapp/results.html', {
        'prediction': prediction
})
        
    
    def submit_rating(request, pk):
        prediction = PredictionRecord.objects.get(pk=pk)

        if request.method == "POST":
         rating = request.POST.get("rating")
         prediction.rating = rating
         prediction.save()

        return render(request, 'webapp/results.html', {
          'prediction': prediction,
          'message': "Thank you for your rating!"
    })

    

    
    