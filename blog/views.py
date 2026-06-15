from .models import Post
from django.shortcuts import render , redirect
from .forms import PostForm
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


def home(request):
    query = request.GET.get('q', '')
    posts_list = Post.objects.filter(title__icontains=query).order_by('-created_at')
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'posts': posts, 'query': query})


def about(request):
    return render (request, 'blog/about.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'حذف شد'})
    return Response({'error': 'method not allowed'})