---
layout: 'post'
permalink: '/jekyll/utterances/'
paginate_path: '/jekyll/:num/utterances/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: Jekyll 블로그에 댓글 기능 넣기
description: utterances 서비스를 이용하여 Jekyll 프로젝트에 댓글 기능을 추가해 보자.
image: '/assets/images/category/jekyll/2021/utterances/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

지금까지 Jekyll 블로그의 댓글 서비스로 [Disqus](https://disqus.com/){:rel="nofollow noreferrer" target="_blank"}를 사용하였습니다. `Disqus`를 사용하여 Jekyll 블로그에 댓글 기능을 추가하는 방법은 아래에 링크를 참고하시기 바랍니다.

- [Disqus 댓글]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}

하지만, 최근 `Disqus`에서 광고를 달기 시작했고, 광고를 제거하기 위해서는 유료로 전환을 해야 했습니다. 이에 다른 댓글 서비스를 찾기 시작했고, `GitHub`의 기능을 이용하여 댓글 서비스를 구현한 `utterances`를 발견하게 되었습니다.

- [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트에서는 `utterances`을 사용하여 Jekyll 블로그에 댓글 기능을 구현하는 방법에 대해서 알아봅시다.

## utterances 연동

utterances는 기본적으로 GitHub의 이슈를 만듬으로써, 댓글을 생성합니다. utterances가 GitHub의 이슈를 만들 수 있도록 GitHub와 연동을하고, 권한을 부여해야 합니다. 아래에 링크를 클릭하여 utterances의 GitHub App 페이지로 이동합니다.

- GitHub App: [utterances](https://github.com/apps/utterances){:rel="nofollow noreferrer" target="_blank"}

utterances의 GitHub App 페이지로 이동하면 다음과 같은 화면을 볼 수 있습니다.

![utterances GitHub App page](/assets/images/category/jekyll/2021/utterances/utterances-github-app-configure.jpg)

오른쪽에 보이는 `Configure` 버튼을 선택합니다.

![utterances select organization](/assets/images/category/jekyll/2021/utterances/utterances-connect-organization.jpg)

이제 utterances가 GitHub의 이슈를 생성하도록 허용하기 위한 계정을 선택합니다.

![utterances select repository](/assets/images/category/jekyll/2021/utterances/utterances-select-repository.jpg)

계정을 선택하였다면, 이제 utterances가 접근 가능한 저장소(Repository)를 선택합니다.

{% include in-feed-ads.html %}

## 스크립트 생성

이렇게 utterances가 GitHub의 이슈를 생성할 수 있게 만들었습니다. 이제 이렇게 생성된 GitHub의 이슈를 화면에 표시하기 위해 utterances의 스크립트를 생성해 봅시다.

utterances의 스크립트를 생성하기 위해, 아래에 링크를 통해 공식 페이지로 이동합니다.

- 공식 페이지: [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

공식 페이지로 이동한 후, 조금 스크롤을 하면 다음과 같이 저장소(Repository)를 입력하는 화면을 찾을 수 있습니다.

![utterances insert repository](/assets/images/category/jekyll/2021/utterances/utterances-insert-repository.jpg)

`Repo` 하단 입력창에 앞에서 이슈를 생성할 수 있게 권한을 부여한 저장소를 `[User Name]/[Repository]` 형식으로 작성합니다. 작성을 완료하였다면, 하단에 `Blog Post ↔️ Issue Mapping` 항목을 찾을 수 있습니다.

![utterances mapping repository](/assets/images/category/jekyll/2021/utterances/utterances-mapping-repository.jpg)

GitHub 이슈에 작성된 내용중 해당 페이지에 관한 댓글만 표시하기 위한 방법을 선택하는 항목입니다. 저는 `Issue title contains page URL`을 선택했지만, 자신에게 편한 선택을 하면 됩니다.

다시 조금 스크롤하면 `Issue Label` 항목을 찾을 수 있습니다.

![utterances issue label](/assets/images/category/jekyll/2021/utterances/utterances-issue-label.jpg)

GitHub에 이슈가 생성될 때, 다른 이슈와 구별하기 위해 해당 이슈에 라벨링을 하기 위한 옵션입니다. 저는 설정을 하지 않고 진행하였습니다.

다음은 표시될 댓글의 테마를 설정하는 항목이 나옵니다.

![utterances select theme](/assets/images/category/jekyll/2021/utterances/utterances-select-theme.jpg)

자신의 블로그의 테마에 맞게 옵션을 선택합니다. 저는 `GitHub Light` 테마를 선택하고 진행하였습니다. 이렇게 모든 항목을 자신의 블로그에 맞게 선택하였다면, 하단에 다음과 같이 utterances 스크립트가 생성된 것을 확인할 수 있습니다.

![utterances script](/assets/images/category/jekyll/2021/utterances/utterances-script.jpg)

{% include in-feed-ads.html %}

## Jekyll 블로그에 적용

이제 이렇게 생성된 스크립트를 Jekyll 블로그에 추가하여 화면에 표시해 봅시다. 저는 [Clean Blog](http://jekyllthemes.org/themes/clean-blog/){:rel="nofollow noreferrer" target="_blank"} 테마를 사용하고 있습니다. Jekyll 블로그에 테마를 설정하는 방법에 대해서는 다음 링크를 참고하시기 바랍니다.

- [테마 설정]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}

자신의 테마에서 블로그에 내용을 표시하는 템플릿을 찾아 복사한 스크립트를 추가해 줍니다. 저는 `_layouts/post.html` 파일에 다음과 같이 추가하였습니다.

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

이것으로 `utterances`을 사용하여 Jekyll 블로그에 댓글 기능을 추가해 보았습니다. 이제 추가한 내용이 잘 적용되었는지 확인하기 위해 다음 명령어를 실행하여 Jekyll 블로그를 실행합니다.

```bash
bundle exec jekyll serve
```

문제없이 잘 실행되었다면, 블로그 페이지에 다음과 같이 utterances 댓글 기능이 표시되는 것을 확인할 수 있습니다.

![utterances comment on jekyll](/assets/images/category/jekyll/2021/utterances/utterances-comment-on-jekyll.jpg)

## 완료

이것으로 Jekyll 블로그에 utterances을 사용하여 댓글 기능을 구현하는 방법에 대해서 살펴보았습니다. 여러분도 Jekyll 블로그를 사용하신다면, utterances를 사용하여 댓글 기능을 구현해 보시기 바랍니다.
