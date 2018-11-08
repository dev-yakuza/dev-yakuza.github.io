---
layout: 'post'
permalink: '/jekyll/github-page/'
paginate_path: '/jekyll/:num/github-page/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'github page'
description: 'upload jekyll project to github page and start blog service.'
image: '/assets/images/category/jekyll/github-page.jpg'
---

## outline
let's start blog service by uploading jekyll project to github page.
we manage basic source code by [bitbucket](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"} and upload static page which is built by jekyll to [github](https://github.com/){:rel="nofollow noreferrer" :target="_blank"} for the blog service.

if you don't know how to make jekyll project, check my previous blogs.

### create jekyll blog
- [jekyll installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Theme settings]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}
- [Directory Structure]({{site.url}}/{{page.categories}}/directory_structure/){:target="_blank"}
- [jekyll settings]({{site.url}}/{{page.categories}}/configuration/){:target="_blank"}

### jekyll project optionals
- [Multi-languages plugin]({{site.url}}/{{page.categories}}/multi-languages-plugin/){:target="_blank"}
- [SEO support]({{site.url}}/{{page.categories}}/seo/){:target="_blank"}
- [pagination plugin]({{site.url}}/{{page.categories}}/pagination-plugin/){:target="_blank"}
- [Disqus comments]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}
- [Send Email]({{site.url}}/{{page.categories}}/send-email/){:target="_blank"}
- [google service]({{site.url}}/{{page.categories}}/google-service/){:target="_blank"}

## bitbucket
bitbucket is source control(version control) service like github. there are many features but we focus to introduce how to manage source code for uploading github. if you don't mind revealing the your source to people, it's better to skip this section.

click below link to go to bitbucket.

- bitbucket: [https://bitbucket.org/](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"}

### signup and signin
we don't introduce how to signup and signin. it's same process to signup and signin to normal service.

![bitbucket login](/assets/images/category/jekyll/github-page/bitbucket-login.png)

### create repository
after login, you can see the menu on the screen. click ```+``` button.

![bitbucket menu](/assets/images/category/jekyll/github-page/bitbucket-menu.png){:class="narrow-image"}

if you see the menu like below, click ```Repository``` for creating new repository.

![bitbucket menu repository](/assets/images/category/jekyll/github-page/bitbucket-menu-repository.png){:class="narrow-image"}

input repository informations.

![bitbucket menu repository information](/assets/images/category/jekyll/github-page/bitbucket-menu-repository-information.png)

completed to create the repository.

### clone repository to local PC
clone the created repository to local pc for developing. if you don't know how to install git or use it, check my another blog.([git]({{site.url}}/git/){:target="_blank"})

![bitbucket git clone](/assets/images/category/jekyll/github-page/bitbucket-git-clone.png)

when repository is created, you can see the above screen. there is the detail about how to clone it. let's do it.

{% include_relative common/git-clone.md %}

clone the repository with the above command. copy jekyll project to the created folder.(or create new jekyll project on there.)

{% include_relative common/git-add-push.md %}

push the local(pc) source to bitbucket repository with the above command.

go to the [bitbucket site](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"} and check the source which you pushed.

## integrate github page
let's upload the static files built by jekyll to github page for starting blog service.

### signup and signin
click the below link to go to the github site and signup and signin. we don't introduce how to signup and signin. it's same process to signup and signin to normal service.

warning: when you sigup, be careful to make ```username```. we make github blog service with ```https://username.github.io```.

- github site: [https://github.com/](https://github.com/){:rel="nofollow noreferrer" :target="_blank"}

![github login](/assets/images/category/jekyll/github-page/github-login.png)

### create Repository
after login, you can see the below screen. click ```Start a project``` button to create new repository.

![github repository](/assets/images/category/jekyll/github-page/github-repository.png)

input ```username + github.io``` that username is when you created on signup and click ```Create repository``` button for creating the repository.

![github crete repository](/assets/images/category/jekyll/github-page/github-create-repository.png)

### clone Repository to PC
there are the detail about how to clone it kindly, but we don't do it because we already clone bitbucket to local(pc). we will do another way.

![github clone repository](/assets/images/category/jekyll/github-page/github-clone-repository.png)

add remote repository with the below command.

{% include_relative common/add-remote.md %}

completed to clone it. push only the source built by jekyll to the repository with the below command.

{% include_relative common/push-subtree.md %}

if the source is not built by jekyll, build it first.

{% include jekyll/build_command.md %}

check the blog site on github page.

```
https://dev-yakuza.github.io
```

## completed
we looked how to integrate the source to github and bitbucket. we integrated the source which is before being built to bitbucket and integrated static pages built by jekyll to github page for the blog service. now, you can start own your blog.