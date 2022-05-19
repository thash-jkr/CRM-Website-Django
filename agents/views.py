from asyncio import FastChildWatcher
import email
import random
from re import sub
from urllib import request
from django.shortcuts import render, reverse
from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin

# Create your views here.
class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        user.set_password(f"{user.username}@{random.randint(1000, 9999)}")
        user.save() 
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You have been invited as an Agent!",
            message="You have been added as an Agent in the website DJCRM, please login to work with us.",
            from_email="admin@gmail.com",
            recipient_list=[user.email]
        )
        # agent.organisation = self.request.user.userprofile
        # agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_objects_name=  "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.all(organisation=organisation)

class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.all(organisation=organisation)

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_objects_name = "agent"

    def get_quesryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.all(organisation=organisation)

    def get_success_url(self):
        return reverse("agents:list")
