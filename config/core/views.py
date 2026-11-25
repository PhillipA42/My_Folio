from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        d = form.cleaned_data
        send_mail(
            subject=f"[Portfolio] {d['subject']}",
            message=f"From:{d['name']} <{d['email']}>\n\n{d['message']}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        messages.success(self.request, "Thanks - message sent.-")
        return super().form_valid(form)