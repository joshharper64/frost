from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Report
from .forms import ReportForm

def allreports(request):
    """ Show list of all reports, regardless of topic """
    reports = Report.objects.order_by('-date_added')
    context = {'reports': reports}
    return render(request, 'resident_reports/allreports.html', context)

@login_required
def new_report(request):
    """ Add new report """
    if request.method != 'POST':
        form = ReportForm()
    else:
        form = ReportForm(user=request.user, data=request.POST)
        User = get_user_model()
        if form.is_valid():
            new_entry = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('resident_reports:allreports'))

    context = {'form': form}
    return render(request, 'resident_reports/new_report.html', context)

@login_required
def edit_report(request, entry_id):
    """ Edit an existing report """
    report = Report.objects.get(id=entry_id)
    if report.owner != request.owner:
        return HttpResponseRedirect(reverse('resident_reports:allreports'))
    if request.method != 'POST':
        form = ReportForm(instance=report)
    else:
        form = ReportForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('resident_reports:allreports'))

    context = {'report': report, 'form': form}
    return render(request, 'resident_reports/edit_report.html', context)
