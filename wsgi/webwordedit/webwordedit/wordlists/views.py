# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from wordselect import WordListSelect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.forms.models import modelformset_factory
from webwordedit.wordlists.models import *
from webwordedit.wordlists.forms import *
from django.core.paginator import *
import simplejson

'''
class  Verified_bn_in_form(ModelForm):
     class Meta:
         model = Verified_bn_in
         exclude = ['author','time','verified_by_usr','verified_by_admin','discard_word','alternate_phrase',]
'''

def wordlists(request,list_type):
    if request.method == 'POST': # If the form has been submitted...
        lang = request.POST['language']
        locale = request.POST['locale']
        new_url = lang+"/"+locale+"/"
        return HttpResponseRedirect(new_url) # Redirect after POST
    return render_to_response('wordlist.html',context_instance=RequestContext(request))


def verified(request,lang,locale):
    db_table_name = "Verified_"+locale
    objects = get_verified_table_object(db_table_name)
    if objects == None:
        raise Http404
    return render(request, "verified.html", {"query_results": objects })


def get_verified_table_object(table_name):
    return globals()[table_name].objects.all()
    '''
    if table_name == "Verified_bn_in":
        from webwordedit.wordlists.models import Verified_bn_in
        objects = Verified_bn_in.objects.all()     
    elif table_name == "Verified_mr_in":
        from webwordedit.wordlists.models import Verified_mr_in
        objects = Verified_mr_in.objects.all()    
    elif table_name == "Verified_de_de":
        from webwordedit.wordlists.models import Verified_de_de
        objects = Verified_de_de.objects.all()    
    elif table_name == "Verified_da_dk":
        from webwordedit.wordlists.models import Verified_da_dk
        objects = Verified_da_dk.objects.all()    
    return objects
    '''

def get_un_verified_table_object(table_name,admin_cond=True):
    if admin_cond:
        return globals()[table_name].objects.all().filter(verified_by_usr=False).filter(verified_by_admin=False)
    return globals()[table_name].objects.all().filter(verified_by_admin=False)
    '''
    if table_name == "Un_Verified_bn_in":
        from webwordedit.wordlists.models import Un_Verified_bn_in
        if admin_cond:
            objects = Un_Verified_bn_in.objects.all().filter(verified_by_usr=False).filter(verified_by_admin=False)
        else:
            objects = Un_Verified_bn_in.objects.all().filter(verified_by_admin=False)
    elif table_name == "Un_Verified_mr_in":
        from webwordedit.wordlists.models import Un_Verified_mr_in
        if admin_cond:
            objects = Un_Verified_mr_in.objects.all().filter(verified_by_usr=False).filter(verified_by_admin=False)
        else:
            objects = Un_Verified_mr_in.objects.all().filter(verified_by_admin=False)
    elif table_name == "Un_Verified_de_de":
        from webwordedit.wordlists.models import Un_Verified_de_de
        if admin_cond:
            objects = Un_Verified_de_de.objects.all().filter(verified_by_usr=False).filter(verified_by_admin=False)
        else:
            objects = Un_Verified_de_de.objects.all().filter(verified_by_admin=False)
    elif table_name == "Un_Verified_da_dk":
        from webwordedit.wordlists.models import Un_Verified_da_dk
        if admin_cond:
            objects = Un_Verified_da_dk.objects.all().filter(verified_by_usr=False).filter(verified_by_admin=False)
        else:
            objects = Un_Verified_da_dk.objects.all().filter(verified_by_admin=False)
    return objects
    '''
def verify(request,lang,locale):
    user = request.user
    if str(request.user) == "AnonymousUser":
        return HttpResponseRedirect('/accounts/login')
    if request.user.is_superuser:
        return admin_page(request,lang,locale)
    else:
        return user_page(request,lang,locale)

def get_form_set_object(db_table_name):
    return modelformset_factory(globals()[db_table_name],form=globals()[db_table_name+"_form"],extra=0) 
    '''
    if db_table_name == "Un_Verified_bn_in":
        from webwordedit.wordlists.forms import Un_Verified_bn_in_form
        from webwordedit.wordlists.models import Un_Verified_bn_in
        formset = modelformset_factory(Un_Verified_bn_in,form=Un_Verified_bn_in_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_mr_in":
        from webwordedit.wordlists.forms import Un_Verified_mr_in_form
        from webwordedit.wordlists.models import Un_Verified_mr_in
        formset = modelformset_factory(Un_Verified_mr_in,form=Un_Verified_mr_in_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_da_dk":
        from webwordedit.wordlists.forms import Un_Verified_da_dk_form
        from webwordedit.wordlists.models import Un_Verified_da_dk
        formset = modelformset_factory(Un_Verified_da_dk,form=Un_Verified_da_dk_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_de_de":
        from webwordedit.wordlists.forms import Un_Verified_de_de_form
        from webwordedit.wordlists.models import Un_Verified_de_de
        formset = modelformset_factory(Un_Verified_de_de,form=Un_Verified_de_de_form,extra=0)
        return formset
    '''
def user_page(request,lang="bn",locale="bn_in"):
    db_table_name = "Un_Verified_"+locale
    FormSet = get_form_set_object(db_table_name)
    query = get_un_verified_table_object(db_table_name)
    paginator = Paginator(query, 10)
    page = request.GET.get('page')
    usr_name = request.user
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    page_query = query.filter(id__in=[object.id for object in objects])
    if request.method == 'POST':
        form_with_post = FormSet(request.POST,queryset=page_query)
        if form_with_post.is_valid():
            instances = form_with_post.save(commit=True)
            for instance in instances:
                #obj = Un_Verified_bn_in.objects.get(pk=instance.id)
                instance.author = str(usr_name)
                instance.verified_by_usr = True
                instance.author_email = str(request.user.email)
                instance.save()
            if page:
                page=int(page)+1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)
            page_query = query.filter(id__in=[object.id for object in objects])
            formset = FormSet(queryset=page_query)
            context = {'objects': objects, 'formset': formset}
            return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))
        else:
            print "errors in the page"
        context = {'objects':objects,'formset': form_with_post}
        return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))
    else:
        formset = FormSet(queryset=page_query)
        context = {'objects': objects, 'formset': formset}
        return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))


def get_formset_admin_object(db_table_name):
    return modelformset_factory(globals()[db_table_name],form=globals()[db_table_name+"_admin_form"],extra=0) 
    '''
    if db_table_name == "Un_Verified_bn_in":
        from webwordedit.wordlists.forms import Un_Verified_bn_in_admin_form
        from webwordedit.wordlists.models import Un_Verified_bn_in
        formset = modelformset_factory(Un_Verified_bn_in,form=Un_Verified_bn_in_admin_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_mr_in":
        from webwordedit.wordlists.forms import Un_Verified_mr_in_admin_form
        from webwordedit.wordlists.models import Un_Verified_mr_in
        formset = modelformset_factory(Un_Verified_mr_in,form=Un_Verified_mr_in_admin_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_da_dk":
        from webwordedit.wordlists.forms import Un_Verified_da_dk_admin_form
        from webwordedit.wordlists.models import Un_Verified_da_dk
        formset = modelformset_factory(Un_Verified_da_dk,form=Un_Verified_da_dk_admin_form,extra=0)
        return formset
    elif db_table_name == "Un_Verified_de_de":
        from webwordedit.wordlists.forms import Un_Verified_de_de_admin_form
        from webwordedit.wordlists.models import Un_Verified_de_de
        formset = modelformset_factory(Un_Verified_de_de,form=Un_Verified_de_de_admin_form,extra=0)
        return formset
    '''
def admin_page(request,lang,locale):
    db_table_name = "Un_Verified_"+locale
    FormSet = get_formset_admin_object(db_table_name)
    query = get_un_verified_table_object(db_table_name,admin_cond=False)
    paginator = Paginator(query, 10)
    page = request.GET.get('page')
    usr_name = request.user
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    page_query = query.filter(id__in=[object.id for object in objects])
    if request.method == 'POST':
        form_with_post = FormSet(request.POST,queryset=page_query)
        if form_with_post.is_valid():
            instances = form_with_post.save(commit=True)
            if instances == []:
                for form in form_with_post.forms:
                    model_instance = form.save(commit=False)
                    model_instance.admin_name = str(usr_name)
                    model_instance.verified_by_admin = True
                    model_instance.admin_email = str(request.user.email)
                    model_instance.save()
            for instance in instances:
                instance.admin_name = str(usr_name)
                instance.verified_by_admin = True
                instance.admin_email = str(request.user.email)
                instance.save()
            if page:
                page=int(page)+1
            try:
                objects = paginator.page(page)
            except PageNotAnInteger:
                objects = paginator.page(1)
            except EmptyPage:
                objects = paginator.page(paginator.num_pages)
            page_query = query.filter(id__in=[object.id for object in objects])
            formset = FormSet(queryset=page_query)
            context = {'objects': objects, 'formset': formset}
            return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))
        else:
            print "errors in the page"
        context = {'objects':objects,'formset': form_with_post}
        return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))
    else:
        formset = FormSet(queryset=page_query)
        context = {'objects': objects, 'formset': formset}
        return render_to_response('unverified.html', context,
                                  context_instance=RequestContext(request))

def language_list():
    from webwordedit.wordlists.models import Langauges
    langs = Langauges.objects.all().values(
        'language',
        'lang_code')
    lang_list = []
    try:
        map(lambda x: lang_list.append(x),langs)
        json = simplejson.dumps(lang_list)
        return HttpResponse(json, mimetype='application/json')
    except TypeError:
        print "Can't convert language to Json \n"
        raise Http404
        

def languages(request):
    if request.method == u'GET':
        return language_list()
    else:
        raise Http404


def locale_list(lang):
    from webwordedit.wordlists.models import Locales
    all_objects = Locales.objects.all().values(
        'lang_code','locale')
    locales = filter(lambda x: True if x['lang_code'] == lang else False ,all_objects)
    locale_list = []
    try:
        map(lambda x: locale_list.append(x),locales)
        json = simplejson.dumps(locale_list)
        return HttpResponse(json, mimetype='application/json')
    except TypeError:
        print "Can't convert language to Json \n"
        raise Http404

def locales(request,lang="mr"):
    if request.method == u'GET':
        return locale_list(lang)
    else:
        raise Http404
    
