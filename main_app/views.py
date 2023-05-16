import json
from django.shortcuts import render, redirect
from .models import Funko, Profile
# from .forms import ReviewForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
class FunkoList(ListView):
  model= Funko
class FunkoCreate(CreateView):
  model= Funko
  fields= ['name', 'association', 'series', 'number', 'image']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
class FunkoUpdate(UpdateView):
  model= Funko
  fields= '__all__'
class FunkoDelete(DeleteView):
  model=Funko
  success_url='/funko/'
class FunkoDetail(DetailView):
  model=Funko
  def get_context_data(self, **kwargs):
    # review_form = ReviewForm()
    context = super().get_context_data(**kwargs)
    # context["review_form"] = review_form
    return context

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('funko_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_to_collection(request, funko_id, profile_id):
  Profile.objects.get(id=profile_id).collection.add(funko_id)
  return redirect('/funko/', funko_id, profile_id,)

def add_to_wishlist(request, funko_id, profile_id):
  Profile.objects.get(id=profile_id).wishlist.add(funko_id)
  return redirect('/funko/', funko_id, profile_id,)

def profile(request):
  profile = Profile.objects
  return render(request, 'profile.html', {profile:profile} )

# def load_json_file():
#     with open('funko_pop.json', 'r') as file:
#         data = json.load(file)

#     for item in data:
#         handle = item['handle']
#         image = item['image']
#         title = item['title']
#         series = item['series']

#         funko = Funko(handle=handle, image=image, title=title, series=series)
#         funko.save()

# def add_review(request, pk):
#   form=ReviewForm(request.POST)
#   if form.is_valid():
#     new_review=form.save(commit=False)
#     new_review.funko_id=pk
#     new_review.save()
#   return redirect('funko_detail', pk=pk)
        

