"explicit is better than implicit"


## class based views

- class based views
  - sempre procurar usar as class based views
  - classes view base providas pelo Django sempre sao posicionadas a direita 
  - mixins sempre são posicionadas a esquerda da classe view base
  - mixins sempre devem herdar de object do python


### class based views integradas do Django

Temos 4 categorias:
 - base generic views
   - django.views.generic.View
   - django.views.generic.TemplateView
   - django.views.generic.RedirectView
 - list generic views
   - django.views.generic.list.ListView
 - detail generic views
   - django.views.generic.detail.DetailView
 - edit generic views
   - django.views.generic.FormView
   - django.views.generic.CreateView
   - django.views.generic.UpdateView
   - djanog.views.generic.DeleteView



