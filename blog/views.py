from django.shortcuts import render

def blog(request):
    return render(request, 'blog/news_list.html')



# def post(request, pk):
#     post = Post.objects.get(pk=pk)
#     comments = Comment.objects.filter(post_id=pk)
#     categories = Category.objects.annotate(num_posts=Count('post'))
#     context = {
#         'post': post,
#         'comments': comments,
#         'categories': categories
#     }
#     return render(request, 'blog/post.html', context)
