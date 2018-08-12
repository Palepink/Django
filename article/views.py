from django.shortcuts import render, get_object_or_404from django.views.decorators.csrf import csrf_exemptfrom django.contrib.auth.decorators import login_requiredfrom django.views.decorators.http import require_POSTfrom django.http import HttpResponsefrom django.core.paginator import Paginator, EmptyPage, PageNotAnIntegerfrom . import forms, modelsimport jsondef articles(request, username=None):    if username:        user = models.User.objects.get(username=username)        articles_title = models.ArticlePost.objects.filter(author=user)        try:            userInfo = user.userinfo        except:            userInfo = None    else:        articles_title = models.ArticlePost.objects.all()    paginator = Paginator(articles_title, 5)    page = request.GET.get('page')    try:        current_page = paginator.page(page)        article_a = current_page.object_list    except PageNotAnInteger:        current_page = paginator.page(1)        article_a = current_page.object_list    except EmptyPage:        current_page = paginator.page(paginator.num_pages)        article_a = current_page.object_list    if username:        return render(request, 'article/articles.html', {'articles': article_a,                                                         'page': current_page,                                                                    'userinfo': userInfo,                                                                    'user': user})    return render(request, 'article/articles.html', {'articles': article_a, 'page': current_page})@login_required(login_url='account/login')@csrf_exemptdef article_column(request):    if request.method == 'GET':        columns = models.ArticleColumn.objects.filter(user=request.user)        column_form = forms.ArticleColumnForm()        return render(request, 'article/article_column.html', {'columns': columns, 'column_form': column_form})    if request.method == 'POST':        column_name = request.POST['column']        columns = models.ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)        if columns:            return HttpResponse('2')        else:            models.ArticleColumn.objects.create(user=request.user, column=column_name)            return HttpResponse('1')@login_required(login_url='/account/login')@csrf_exempt@require_POSTdef rename_article_column(request):    column_name = request.POST["column_name"]    column_id = request.POST['column_id']    try:        line = models.ArticleColumn.objects.get(id=column_id)        line.column = column_name        line.save()        return HttpResponse('1')    except:        return HttpResponse('0')@login_required(login_url='/account/login')@csrf_exempt@require_POSTdef del_article_column(request):    column_id = request.POST['column_id']    try:        column = models.ArticleColumn.objects.get(id=column_id)        column.delete()        return HttpResponse('1')    except:        return HttpResponse('2')@login_required(login_url='/account/login')@csrf_exemptdef article_post(request):    if request.method == 'GET':        article_post_form = forms.ArticlePostForm()        article_columns = request.user.article_column.all()        article_tags = request.user.tag.all()        return render(request, 'article/article_post.html',                      {'article_post_form': article_post_form, 'article_columns': article_columns,                       'article_tags': article_tags})    else:        article_post_form = forms.ArticlePostForm(data=request.POST)        if article_post_form.is_valid():            try:                new_article = article_post_form.save(commit=False)                new_article.author = request.user                new_article.column = request.user.article_column.get(id=request.POST['column_id'])                new_article.save()                tags = request.POST['tags']                if tags:                    for atag in json.loads(tags):                        tag = request.user.tag.get(tag=atag)                        new_article.article_tag.add(tag)                return HttpResponse('1')            except:                return HttpResponse('2')        else:            return HttpResponse('3')@login_required(login_url='/account/login')def article_list(request):    articles_list = models.ArticlePost.objects.filter(author=request.user)    paginator = Paginator(articles_list, 10)    page = request.GET.get('page')    try:        current_page = paginator.page(page)        article = current_page.object_list    except PageNotAnInteger:        current_page = paginator.page(1)        article = current_page.object_list    except EmptyPage:        current_page = paginator.page(paginator.num_pages)        article = current_page.object_list    return render(request, 'article/article_list.html', {'articles': article, 'page': current_page})@login_required(login_url='/account/login')@require_POST@csrf_exemptdef del_article(request):    article_id = request.POST['article_id']    try:        article = models.ArticlePost.objects.get(id=article_id)        article.delete()        return HttpResponse('1')    except:        return HttpResponse('2')@login_required(login_url='/account/login')def article_detail(request, id, slug):    article = get_object_or_404(models.ArticlePost, id=id, slug=slug)    tags_ids = article.article_tag.values_list("id", flat=True)    return render(request, 'article/article_detail.html', {'article': article, 'tags_ids':tags_ids})@login_required(login_url='/account/login')@csrf_exemptdef edit_article(request, article_id):    if request.method == 'GET':        article_columns = request.user.article_column.all()        article = models.ArticlePost.objects.get(id=article_id)        this_article_form = forms.ArticlePostForm(initial={"title": article.title})        this_article_column = article.column        return render(request, 'article/edit_article.html', {'article': article, 'article_columns': article_columns,                                                             'this_article_form': this_article_form,                                                             'this_article_column': this_article_column})    else:        ed_article = models.ArticlePost.objects.get(id=article_id)        try:            ed_article.column = request.user.article_column.get(id=request.POST['column_id'])            ed_article.title = request.POST['title']            ed_article.body = request.POST['body']            ed_article.save()            return HttpResponse('1')        except:            return HttpResponse('2')@login_required(login_url='/account/login')@csrf_exemptdef article_tag(request):    if request.method == 'GET':        article_tags = models.ArticleTag.objects.filter(author=request.user)        article_tags_form = forms.ArticleTagForm()        return render(request, 'article/tag.html', {'article_tags': article_tags,                                                    'article_tags_form': article_tags_form})    if request.method == 'POST':        tag_post_form = forms.ArticleTagForm(data=request.POST)        if tag_post_form.is_valid():  # 使用unique保证不重复            new_tag = tag_post_form.save(commit=False)            new_tag.author = request.user            new_tag.save()            return HttpResponse('1')        else:            return HttpResponse('空白或标签已经存在')@login_required(login_url='/account/login')@csrf_exempt@require_POSTdef edit_tag(request):    tag_name = request.POST["tag_name"]    tag_id = request.POST['tag_id']    try:        line = models.ArticleTag.objects.get(id=tag_id)        line.tag = tag_name        line.save()        return HttpResponse('1')    except:        return HttpResponse('0')@login_required(login_url='/account/login')@csrf_exempt@require_POSTdef del_tag(request):    tag_id = request.POST['tag_id']    try:        tag = models.ArticleTag.objects.get(id=tag_id)        tag.delete()        return HttpResponse('1')    except:        return HttpResponse('2')def detail(request, id, slug):    article = get_object_or_404(models.ArticlePost, id=id, slug=slug)    tags_ids = article.article_tag.values_list("id", flat=True)    return render(request, 'article/article_detail_user.html', {'article': article, 'tags_ids':tags_ids})