---
layout: 'post'
permalink: '/django/custom-user-model/'
paginate_path: '/django/:num/custom-user-model/'
lang: 'en'
categories: 'django'
comments: true

title: 'django Customm User Model'
description: let's see how to make Custom User Model in django.
image: '/assets/images/category/django/2019/custom-user-model/background.jpg'
---

## Outline
when we try to login via django basic User Model, we should login with username. also, sometimes, we develop the service, we want to store user's gender, birthday or profile image. in this blog post, we'll see how to create Custom User Model in django. this blog post contents is based on `django officail site`.

- django official site: [https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example){:rel="nofollow noreferrer" target="_blank"}

you can see full code of this blog post on github. see the link below.

- github: [https://github.com/dev-yakuza/django_custom_user_model](https://github.com/dev-yakuza/django_custom_user_model){:target="_blank"}

## Prepare django project
execute the command below to create django project.

```bash
django-admin startproject django_custom_user_model
```

connect database only by seeing the blog below.(don't execute `python manage.py migrate`.)

- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

execute the command below to create new django app named `account`.

```bash
python manage.py startapp account
```

and then open `django_custom_user_model/settgins.py` file and modify it to add new app like below.

```python
...
INSTALLED_APPS = [
    ...
    'account',
]
...
```

{% include in-feed-ads.html %}

## Create Custom User Model
open and modify `account/models.py` to create Custom User Model like below.

```python
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
```

let's see more details.

```python
...
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
...
class UserManager(BaseUserManager):
...
class User(AbstractBaseUser):
...
```

we need to implement 2 classes (`BaseUserManager`, `AbstractBaseUser`) to create Custom User Model. `BaseUserManager` is a helper class to create an user, and Custom User Model class should be inherited `AbstractBaseUser` class.

the helper class(`class UserManager(BaseUserManager):`) has 2 functions.

- `create_user(*username_field*, password=None, **other_fields)`
- `create_superuser(*username_field*, password, **other_fields)`

as you can see, first parameter is username. we want to use email not username, so we pass email instead of username. other parts are just storing the data, so skip to introduce.

let's see Custom User Model(`class User(AbstractBaseUser):`).

```python
...
email = models.EmailField(
    verbose_name='email',
    max_length=255,
    unique=True,
)
date_of_birth = models.DateField()
is_active = models.BooleanField(default=True)
is_admin = models.BooleanField(default=False)
...
```

this model has `email`, `date_of_birth`, `is_active`, `is_admin` fields. `is_active`, `is_admin` fields are required fields for User Model in django.

```python
...
objects = UserManager()

USERNAME_FIELD = 'email'
...
```

this is required parts to create User Model. we set the model uses our helper class (`objects = UserManage()`), and username field is `email`(`USERNAME_FIELD = 'email'`).

```python
def has_perm(self, perm, obj=None):
    return True

def has_module_perms(self, app_label):
    return True

@property
def is_staff(self):
    return self.is_admin
```

we need to implement this part to make Custom USer Model for base Use Model.

- `def has_perm(self, perm, obj=None):`: return True for having permission. if return Ojbect, we need to check the permission by the object.
- `def has_module_perms(self, app_label):`: return True for accessing the app models.
- `def is_staff(self):`: return True to make user login django administrator page.

{% include in-feed-ads.html %}

## Modify Administrator Page
we need to modify the administrator page to manage the user in django admin page.

### Create Form
we need to make new forms for Custom User Model to manage user informations in django admin page. create and modify `account/forms.py` like below.

```python
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
```

let's see more details.

```python
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
...
class UserChangeForm(forms.ModelForm):
...
```

we need to make user creation form and user data modification form.

```python
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
```

user creation form has `password1`, `paasword2`,

```python
class Meta:
    model = User
    fields = ('email', 'date_of_birth')
```

and `email`, `date_of_birth` of our `User` Model. check `password2` is matching `password1` via `def clean_password2(self):` function. lastly, store the data via `def save(self, commit=True):`.

user data modification form is more simple.

```python
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
```

get user password via `ReadOnlyPasswordHashField()` and show it.(can not modify).

```python
class Meta:
    model = User
    fields = ('email', 'password', 'date_of_birth',
                'is_active', 'is_admin')
```

get user's `email`, `password`, `date_of_birth`, `is_activate`, `is_admin` fields, and when store the data, password will be kept because of `def clean_password(self):` function.


### Apply Form to Admin Page
let's apply Forms we've created above to django administrator page. open and modify `account/admin.py` like below.

```python
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
```

let's see more details.

```python
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
```

we set django admin page use our user creation form and user data modification form.

```python
list_display = ('email', 'date_of_birth', 'is_admin')
list_filter = ('is_admin',)
fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal info', {'fields': ('date_of_birth',)}),
    ('Permissions', {'fields': ('is_admin',)}),
)

add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
)
```

we set how our Custom User Model show  in django admin page.

```python
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
```

we register our Custom User Model and Admin Form, and unregister Group that dajngo basically provides.

{% include in-feed-ads.html %}

## Configure Custom User Model
we need to configure to make our Custom User Model be basic authentication user model in django. open and modify `django_custom_user_model/settings.py` like below.

```python
...
AUTH_USER_MODEL = 'account.User'
```

## Create Table
we've not created tables in `Prepare django project` section above. because we want django to use our Custom User Model instead of basic user model. execute the command below to prepare Custom User Model table.

```python
python manage.py makemigrations account
```

and execute the command below to create tables.

```python
python manage.py migrate
```

## Check
let's see our Custom User Model is applied well. first, check the tables we've created above via database tool.

![django Customm User Model - check tables via database tool](/assets/images/category/django/2019/custom-user-model/check-tables.jpg)

we can see there is no `auth_user` table. execute the command below to create django `superuser`.

```bash
python manage.py createsuperuser
```

and then, we can see new process to create `superuser` like below.

```bash
Email: dev.yakuza@gmail.com
Date of birth: 2019-06-06
Password:
Password (again):
Superuser created successfully.
```

execute the command below to start django test server and open django admin page(`http://127.0.0.1:8000/admin`).

```python
python manage.py runserver
```

you can see `email` is required when we login.

![django Customm User Model - django admin page email login](/assets/images/category/django/2019/custom-user-model/check-django-admin.jpg)

lastly, when we add new user or modify user information, we can see the forms like below.

![django Customm User Model - django admin page create new user ](/assets/images/category/django/2019/custom-user-model/django-admin-create-user.jpg)


## Completed
we've seen how to create and use Custom User Model in django. now, we can use Custom User Model instead of basic user model to store more user information for our service!


## Reference
- [django installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Models in django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [django Administrator Page]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [django Routing]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [django ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [django View]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [django Form]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [Upload django project to Heroku]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}
- [https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example){:rel="nofollow noreferrer" target="_blank"}