from django.contrib import messages
if request.method == 'POST' and form.is_valid():
post = form.save(commit=False)
post.author = request.user
post.save()
form.save_m2m()
messages.success(request, 'Post created.')
return redirect(post.get_absolute_url())
return render(request, 'blog/post_form.html', {'form': form})




def post_detail(request, slug):
post = get_object_or_404(Post, slug=slug)
comment_form = CommentForm()
return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})


@login_required
def post_update(request, slug):
post = get_object_or_404(Post, slug=slug)
if not (post.author == request.user or request.user.has_perm('blog.change_post')):
return HttpResponseForbidden('Not allowed')
form = PostForm(request.POST or None, instance=post)
if request.method == 'POST' and form.is_valid():
form.save()
messages.success(request, 'Post updated.')
return redirect(post.get_absolute_url())
return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, slug):
post = get_object_or_404(Post, slug=slug)
if not (post.author == request.user or request.user.has_perm('blog.delete_post')):
return HttpResponseForbidden('Not allowed')
if request.method == 'POST':
post.delete()
messages.success(request, 'Post deleted.')
return redirect('post_list')
return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
@permission_required('blog.can_publish', raise_exception=True)
def post_publish(request, slug):
post = get_object_or_404(Post, slug=slug)
post.published = True
post.save()
messages.success(request, 'Post published.')
return redirect(post.get_absolute_url())


# HTMX endpoints
@login_required
def hx_post_title_inline(request, pk):
post = get_object_or_404(Post, pk=pk)
if not (post.author == request.user or request.user.has_perm('blog.change_post')):
return HttpResponseForbidden()
if request.method == 'POST':
title = request.POST.get('title', '').strip()
if title:
post.title = title
post.save()
return render(request, 'blog/_post_title_display.html', {'post': post})
return render(request, 'blog/_post_title_form.html', {'post': post})




def hx_search(request):
q = request.GET.get('q', '')
posts = Post.objects.filter(published=True)
if q:
posts = posts.filter(Q(title__icontains=q) | Q(body__icontains=q))
return render(request, 'blog/_post_list.html', {'posts': posts})


@login_required
def hx_comment_create(request, slug):
post = get_object_or_404(Post, slug=slug)
form = CommentForm(request.POST)
if form.is_valid():
Comment.objects.create(post=post, author=request.user, body=form.cleaned_data['body'])
messages.success(request, 'Comment added.')
return render(request, 'blog/_comments.html', {'post': post})
return render(request, 'blog/_comment_form.html', {'post': post, 'form': form}, status=400)
