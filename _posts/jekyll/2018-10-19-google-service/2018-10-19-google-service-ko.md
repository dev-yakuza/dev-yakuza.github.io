---
layout: 'post'
permalink: '/jekyll/google-service/'
paginate_path: '/jekyll/:num/google-service/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: 'google 서비스'
description: 'google search console / analytics / adsense를 연동하는 방법에 대해서 알아보자.'
image: '/assets/images/category/jekyll/google-service.jpg'
---

## 개요
자신에 블로그에서 수익을 내거나 더 많은 인사이트를 얻기 위해서는 역시 구글 서비스와 연동이 중요한거 같습니다. 여기에서는 블로그를 더욱 잘 활용할 수 있도록 구글 서비스와 연동해 보도록 하겠습니다.

우리가 여기서 연동할 서비스는 아래와 같습니다.
- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

## Google Analytics
사이트 분석을 위해서는 기본적으로 Google Analytics를 이용합니다. 아래에 링크를 통해 Google Analytics 사이트로 이동하고 구글 계정으로 로그인 합니다.

- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}

로그인을 하면 아래와 같은 화면을 볼 수 있습니다. ```sign up```을 눌러 다음으로 진행하세요.

![google analytics signup](/assets/images/category/jekyll/google/analytics/signup.png)

아래에 사이트 정보를 입력하고 ```Get Tracking ID```를 선택하여 트래킹 코드를 발급받습니다.

![google analytics register site](/assets/images/category/jekyll/google/analytics/register-site.png)

트래킹 코드가 발급되면 ```Global Site Tag (gtag.js)```에 있는 코드를 복사하여 ```_include/head.html```에 붙여넣습니다. 테마에 따라 파일 위치/이름이 다를 수 있습니다.

![google analytics tracking code](/assets/images/category/jekyll/google/analytics/tracking-code.png)

주의: 위에 보이는 코드는 테스트용 코드임으로 붙여 넣으시면 안됩니다. 자신에 트래킹 코드를 복사 붙여넣기 하시기 바랍니다.

Google Analytics 연동이 완료되었습니다. 이제 데이터를 분석하여 블로그를 관리해보세요.

## Google Search Console
Google Search Console은 구글 검색 엔진에 사이트를 등록하여 구글에서 검색이 가능하다록 합니다. 아래에 링크를 눌러 Google Search Console로 이동합니다.

- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}

아래와 같은 화면에서 ```Start now```를 눌러 Google Search Console을 시작합니다.

![google search console start](/assets/images/category/jekyll/google/search-console/start.png)

사이트 URL을 입력하여 Google Search Console에 사이트를 등록합니다.

![google search console start](/assets/images/category/jekyll/google/search-console/register.png)

아래와 같은 화면이 나오면 ```Google Analytics```를 선택하고 ```VERIFY```를 눌러 자신의 사이트임을 증명합니다.

![google search console verify](/assets/images/category/jekyll/google/search-console/verify.png)

이제 사이트맵을 등록시켜 구글봇이 사이트를 크롤링할 수 있도록 안내합니다.

![google search console sitemap](/assets/images/category/jekyll/google/search-console/sitemap.png)

Google Search Console 연동이 완료되었습니다. 이제 구글봇이 사이트를 크롤링할 것입니다. 우리는 기다리는 일만 남았습니다.

구글봇이 사이트를 크롤링하지 못하거나 시간이 많이 걸리면 직접 크롤링 요청할 수 있습니다.

![google search console request](/assets/images/category/jekyll/google/search-console/request.png)

상단에 검색바에 크롤링을 요청하고 싶은 URL을 넣습니다. 위와 같은 화면에서 ```REQUEST INDEXING```을 눌러 직접 크롤링을 요청할 수 있습니다.

Google Search Console 연동이 끝났습니다. 이제 우리 사이트가 구글에서 검색이 가능하게 됩니다.

## Google Adsense
우리가 블로그로 엄청난 부자가 될 일은 없지만 Google Adsense 연동 연습도 할겸 돈도 벌어 볼겸 jekyll에 Google Adsense를 연동해 봅시다.

아래에 링크를 통해 Google Adsense 사이트로 이동합니다.

- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

Google Adsense 사이트에서 ```sign up```을 눌러 가입합니다.

![google adsense signup](/assets/images/category/jekyll/google/adsense/signup.png)

사이트 등록이 완료되면 payment를 등록해야합니다. Google Adsense에서 돈을 받을 분에 정보를 입력합니다.

![google adsense payment](/assets/images/category/jekyll/google/adsense/payment.png)

그리고 Google Adsense가 우리 사이트를 등록해 줄때까지 기다리면 됩니다. 보통 하루면 등록이 된다고 하지만, 우리 사이트는 2~3주정도 걸렸습니다. 처음 블로그를 만들때 등록해서 컨텐츠(페이지)가 별로 없어서 등록을 안시켜준게 아닌가 싶습니다.

![google adsense get](/assets/images/category/jekyll/google/adsense/get.png)

많은 유저들이 페이지를 보거나 클릭하면 이렇게 Google Adsense로부터 돈이 들어옵니다. 실제로 우리 통장에 입금하기 위해서는 일정 금액(¥8,000)이상이 되어야 입금이 가능합니다. 입금이 가능한 날이 오면 입금 절차도 블로그에 작성하도록 하겠습니다.

## 참고
- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}