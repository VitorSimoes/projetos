#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dados do candidato")
