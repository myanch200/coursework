from django.shortcuts import render
import json
import requests
# Create your views here.


def dashboard(request):
    url = "https://covid-19-tracking.p.rapidapi.com/v1/uk"

    headers = {
        'x-rapidapi-key': "a3bcc4cfa4msh2be91c4f5e035c7p148e2ejsn9dd71f8cb55a",
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()
    total_cases = response['Total Cases_text']
    total_deaths = response['Total Deaths_text']
    active_cases = response['Active Cases_text']
    recovered_cases = response['Total Recovered_text']
    new_cases = response['New Cases_text']
    last_updated = response['Last Update']
    context = {
        'total_cases': total_cases,
        'total_deaths': total_deaths,
        'active_cases': active_cases,
        'recovered':recovered_cases,
        'new_cases': new_cases,
        'last_updated': last_updated
    }
    print(response)
    return render(request, 'tracker/dashboard.html',context)
