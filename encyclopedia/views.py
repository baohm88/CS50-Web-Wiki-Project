from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def convert_md_to_html(title):
    content = util.get_entry(title)
    if content is None:
        return None
    else:
        markdowner = Markdown()
        return markdowner.convert(content)


def entry(request, title):
    content = convert_md_to_html(title)
    if content is None:
        return render(request, 'encyclopedia/error.html', {
            "message": "The entry you entered doesn't exist. Please try another one."
        })
    else:
        return render(request, 'encyclopedia/entry.html', {
            "title": title,
            "content": content,
        })


def search(request):
    if request.method == 'POST':
        search_entry = request.POST['q']
        content = convert_md_to_html(search_entry)
        if content is not None:
            return render(request, 'encyclopedia/entry.html', {
                "title": search_entry,
                "content": content,
            })
        else:
            allEntries = util.list_entries()
            recommended_entries = []
            for entry in allEntries:
                if search_entry.lower() in entry.lower():
                    recommended_entries.append(entry)

            return render(request, 'encyclopedia/search.html', {
                "recommended_entries": recommended_entries,
                "title": search_entry
            })


def new(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/new.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, 'encyclopedia/error.html', {
                "message": 'The entry you have entered already exists.'
            })
        else:
            util.save_entry(title, content)
            return render(request, 'encyclopedia/entry.html', {
                "title": title,
                "content": convert_md_to_html(title)
            })


def edit(request):
    if request.method == 'POST':
        title = request.POST['edit_title']
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            "title": title,
            "content": content
        })


def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, 'encyclopedia/entry.html', {
            "title": title,
            "content": convert_md_to_html(title)
        })


def rand_page(request):
    entries = util.list_entries()
    rand_entry = random.choice(entries)
    return render(request, 'encyclopedia/entry.html', {
        "title": rand_entry,
        "content": convert_md_to_html(rand_entry)
    })



