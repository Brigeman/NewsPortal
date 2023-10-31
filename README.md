Models:
Commands for Django shell

#create users
from django.contrib.auth.models import User
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

#create 2 objects - author
from portal.models import Author
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

#add 4 category
from portal.models import Category
category1 = Category.objects.create(name='Категория 1')
category2 = Category.objects.create(name='Категория 2')
category3 = Category.objects.create(name='Категория 3')
category4 = Category.objects.create(name='Категория 4')

#add 2 article & 1 news
from portal.models import Post
article1 = Post.objects.create(author=author1, post_type='article', title='Статья 1', content='Содержание статьи 1', rating=0)
article1.categories.add(category1, category2)
article1.save()

article2 = Post.objects.create(author=author2, post_type='article', title='Статья 2', content='Содержание статьи 2', rating=0)
article2.categories.add(category2, category3)
article2.save()

news1 = Post.objects.create(author=author1, post_type='news', title='Новость 1', content='Содержание новости 1', rating=0)
news1.categories.add(category3, category4)
news1.save()

#create 4 comments
from portal.models import Comment
comment1 = Comment.objects.create(post=article1, user=user1, text='Комментарий к статье 1', rating=0)
comment2 = Comment.objects.create(post=article2, user=user2, text='Комментарий к статье 2', rating=0)
comment3 = Comment.objects.create(post=news1, user=user1, text='Комментарий к новости 1', rating=0)
comment4 = Comment.objects.create(post=news1, user=user2, text='Другой комментарий к новости 1', rating=0)

#change rating with like/dislike
article1.like()
article1.like()
article2.like()
news1.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment4.like()

#update rating
author1.update_rating()
author2.update_rating()

#check
best_author = Author.objects.order_by('-rating').first()
print(f"Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating}")
Лучший пользователь: user1, Рейтинг: 9


best_article = Post.objects.filter(post_type='article').order_by('-rating').first()
print(f"Дата добавления: {best_article.created_at}")
print(f"Автор: {best_article.author.user.username}")
print(f"Рейтинг: {best_article.rating}")
print(f"Заголовок: {best_article.title}")
print(f"Превью: {best_article.preview()}")
Дата добавления: 2023-10-31 10:34:56.705866+00:00
Автор: user1
Рейтинг: 2
Заголовок: Статья 1
Превью: Содержание статьи 1


comments_to_best_article = Comment.objects.filter(post=best_article)
for comment in comments_to_best_article:
    print(f"Дата: {comment.created_at}")
    print(f"Пользователь: {comment.user.username}")
    print(f"Рейтинг: {comment.rating}")
    print(f"Текст: {comment.text}")
Дата: 2023-10-31 10:36:29.874156+00:00
Пользователь: user1
Рейтинг: 1
Текст: Комментарий к статье 1
