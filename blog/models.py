from django.db import models


class Category(models.Model):
    '''
    分类模型
    '''
    # 分类名
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    标签模型
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    文章模型
    '''
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章内容
    body = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 修改时间
    modify_time = models.DateTimeField(auto_now=True)
    # 文章分类
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # 文章标签
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
