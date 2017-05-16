from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, Report
from .forms import ReportForm

def rindex(request):
    """ Show the Resident Report index """
    return render(request, 'resident_reports/rindex.html')

def topics(request):
    """ Show a list of topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'resident_reports/topics.html', context)

def topic(request, topic_id):
    """ Show a single topic and all its reports """
    topic = Topic.objects.get(id=topic_id)
    reports = topic.report_set.order_by('-date_added')
    context = {'topic': topic, 'reports': reports}
    return render(request, 'resident_reports/topic.html', context)

def allreports(request):
    """ Show list of all reports, regardless of topic """
    reports = Report.objects.order_by('-date_added')
    context = {'reports': reports}
    return render(request, 'resident_reports/allreports.html', context)

def new_report(request, topic_id):
    """ Add new report """
    if request.method != 'POST':
        form = ReportForm
    else:
        form = ReportForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            form.save()
            return HttpResponseRedirect(reverse('homepage:index',
                                                args=[topic_id]))

    context = {'topic':topic, 'form': form}
    return render(request, 'residents_reports/new_report.html', context)

def edit_report(request, entry_id):
    """ Edit an existing report """
    report = Report.objects.get(id=entry_id)
    topic = report.topic

    if request.method != 'POST':
        form = ReportForm(instance=report)
    else:
        form = ReportForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('resident_reports:allreports'))

    context = {'report': report, 'topic': topic, 'form': form}
    return render(request, 'resident_reports/edit_report.html', context)
