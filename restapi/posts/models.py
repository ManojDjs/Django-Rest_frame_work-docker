from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import generics
from datetime import datetime
from django.utils.timezone import timezone


class PPosts(models.Model):
    author = models.ForeignKey(User, to_field='username', related_name='author', on_delete=models.CASCADE)
    post_text = models.CharField(max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to='\media')
    post_time = models.DateTimeField(default=datetime.now(), blank=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes', null=True,blank=True)

    def __str__(self):
        return self.post_text


class PComments(models.Model):
    comment_post = models.ForeignKey(PPosts, on_delete=models.CASCADE, related_name='post_comment')
    commentor = models.ForeignKey(User, to_field='username', related_name='commentor', on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_time = models.DateTimeField(default=datetime.now(), blank=True)
    comment_likes = models.ManyToManyField(User, related_name='likes_post', null=True)

    def __str__(self):
        return self.comment_text


class PReplyComment(models.Model):
    reply_to_comment = models.ForeignKey(PComments, on_delete=models.CASCADE, related_name='reply_to_comment')
    reply_commentor = models.ForeignKey(User, to_field='username', related_name='reply_commentor',
                                        on_delete=models.CASCADE)
    reply_text = models.TextField()
    reply_time = models.DateTimeField(default=datetime.now(), blank=True)
    reply_likes = models.ManyToManyField(User, related_name='comment_likes_post', null=True)

    def __str__(self):
        return self.reply_text
