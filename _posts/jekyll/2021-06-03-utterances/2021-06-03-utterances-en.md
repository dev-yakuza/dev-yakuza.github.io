---
layout: 'post'
permalink: '/jekyll/utterances/'
paginate_path: '/jekyll/:num/utterances/'
lang: 'en'
categories: 'jekyll'
comments: true

title: Comment feature in Jekyll blog
description: Let's see how to use utterances service to add a comment feature to Jekyll project.
image: '/assets/images/category/jekyll/2021/utterances/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Connect utterances](#connect-utterances)
- [Create script](#create-script)
- [Apply it to Jekyll blog](#apply-it-to-jekyll-blog)
- [Completed](#completed)

</div>

## Outline

I've used [Disqus](https://disqus.com/){:rel="nofollow noreferrer" target="_blank"} for the comment service in Jekyll blog. You can see how to use `Disqus` to make a comment feature in Jekyll blog on the linke below.

- [Disqus comment]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}

However, `Disqus` adds the advertisement recently, and if we want to remove the advertisement, we need to pay. So I was looking for the other comment services, and I've found `utterances` which uses `GitHub` feature for the comment feature.

- [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

In this blog post, I will show you how to use `utterances` for the comment feature in Jekyll blog.

## Connect utterances

utterances basically create a GitHub issue to make a comment. So, we need to connect utterances to GitHub, and give the permission to utterances. Click the link below to go to the utterances GitHub App page.

- GitHub App: [utterances](https://github.com/apps/utterances){:rel="nofollow noreferrer" target="_blank"}

You can see the page like the blow when you go to the utterances GitHub App page.

![utterances GitHub App page](/assets/images/category/jekyll/2021/utterances/utterances-github-app-configure.jpg)

Click the `Configure` button on the right of the screen.

![utterances select organization](/assets/images/category/jekyll/2021/utterances/utterances-connect-organization.jpg)

Next, select the account which utterances can make the GitHub issue.

![utterances select repository](/assets/images/category/jekyll/2021/utterances/utterances-select-repository.jpg)

After selecting the account, select the Repository that utterances can access.

{% include in-feed-ads.html %}

## Create script

Now, utterances can make the GitHub issue. To show the GitHub issue which utterances creates on the screen, we need to create an utterances script.

To create the utterances script. Click the link below to go to the official page.

- Official page: [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

When you go to the official page and scroll down a little bit, you can find the screen below to insert the repository.

![utterances insert repository](/assets/images/category/jekyll/2021/utterances/utterances-insert-repository.jpg)

In the input box at the bottom of the `Repo`, write the repository, that you have given permission to create issues, in the form of `[User Name]/[Repository]`.

![utterances mapping repository](/assets/images/category/jekyll/2021/utterances/utterances-mapping-repository.jpg)

This is an option to display only the page comments in GitHub issues. I selected `Issue title contains page URL`, but you can select any options.

When you scroll down a little bit, you can find the `Issue Label` section.

![utterances issue label](/assets/images/category/jekyll/2021/utterances/utterances-issue-label.jpg)

When utterances creates a GitHub issue, this is an option to label the issue to distinguish it from other issues. I didn't configure it.

Next, you can see an option to select the theme of the comments.

![utterances select theme](/assets/images/category/jekyll/2021/utterances/utterances-select-theme.jpg)

Select the theme that matches the your blog theme. I selected the `GitHub Light` theme. After all, you can see the script which utterances creates.

![utterances script](/assets/images/category/jekyll/2021/utterances/utterances-script.jpg)

{% include in-feed-ads.html %}

## Apply it to Jekyll blog

Let's see add the script to Jekyll blog to show the comments. I used [Clean Blog](http://jekyllthemes.org/themes/clean-blog/){:rel="nofollow noreferrer" target="_blank"} theme for my Jekyll blog. If you want to know how to use the theme in Jekyll blog, see the link below.

- [Theme settings]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}

find the template that shows the blog post in your theme, and copy-paste the script to it. I added the script to the `_layouts/post.html` file like the below.

```html
<div class="col-lg-8 col-md-10 mx-auto">
  <hr />
  {% if page.comments %}
  <script src="https://utteranc.es/client.js"
    repo="dev-yakuza/dev-yakuza.github.io"
    issue-term="url"
    label="comment"
    theme="github-light"
    crossorigin="anonymous"
    async>
  </script>
  {% endif %}
</div>
```

Done! we've added the the `utterances` comment feature to Jekyll blog. Execute the command below to start the Jekyll blog to check the comment feature is working well.

```bash
bundle exec jekyll serve
```

After Jekyll blog is opened, you can see the utterances comment feature on the blog post like the below.

![utterances comment on jekyll](/assets/images/category/jekyll/2021/utterances/utterances-comment-on-jekyll.jpg)

## Completed

In this blog post, We've seen how to implement the comment feature by using utterances in Jekyll blog. If you use the Jekyll blog, try to use utterances for the comment feature!
