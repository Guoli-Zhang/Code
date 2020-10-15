def mydecorator(func):
    def wrapper(request, *args, **kwargs):
        return func(request, *args, **kwargs)
    return wrapper

class FirstMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return mydecorator(view)

# class DemoView(FirstMixin, View):
#     pass



# user = User.object.filter(age__gt=F("id"))
# and:  User.objects.filter(id__gt=1).filter(age__gt=10)
# or:  User.objects.filter(Q(id__gt=1) | Q(age__lt=10))
# not:  User.object.filter(~Q(id__gt=1))
# User.objects.order_by("age") 默认升序
# User.objects.order_by("-age") 降序
# user = User.objects.get(id=1) user.books_set.all()

# from django.core.cache import cache
# cache.set(key, alue, 有效期)