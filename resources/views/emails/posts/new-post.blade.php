<!DOCTYPE html>
<html>
<head>
    <title>New Post Created</title>
</head>
<body>
    <h1>A new post has been created!</h1>
    <p>Title: {{ $post->title }}</p>
    <p>Content: {{ $post->content }}</p>
    <p>You can view the post <a href="{{ url('/posts/' . $post->id) }}">here</a>.</p>
</body>
</html>
