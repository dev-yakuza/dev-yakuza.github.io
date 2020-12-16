---
layout: 'post'
permalink: '/clog/development-journal/'
paginate_path: '/clog/:num/development-journal/'
lang: 'en'
categories: 'clog'
comments: true

title: '「Clog」 service development journal(React Native, Laravel, Django)'
description: I've developed 「Clog」 based on React Native, Laravel, Django. This blog post shares my experience when I developed it.
image: '/assets/images/category/clog/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Contents](#contents)
- [Outline](#outline)
- [What is Clog](#what-is-clog)
- [Why make it](#why-make-it)
- [Plan the service](#plan-the-service)
- [Design](#design)
- [System structure](#system-structure)
- [DB design](#db-design)
- [API server development](#api-server-development)
- [Crawling server development](#crawling-server-development)
- [Application development](#application-development)
- [Issue on development](#issue-on-development)
  - [Dothome hosting](#dothome-hosting)
  - [Play video](#play-video)
  - [Reject](#reject)
- [Development period](#development-period)
- [Retrospective](#retrospective)

</div>

## Outline

This is my 16th toy project. You can see what I developed via the link below.

- [JeongHean's App List]({{site.url}}/app/list/en/){:target="_blank"}

There are development journals about the toy projects.

- [BlaBoo App development journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumoncho App development journal(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}
- [일단공부 App development journal(RN, React Native)]({{site.url}}/ildangongbu/development-journal/){:target="_blank"}

I get the information about the development, startup and trend via Facebook groups. However, Facebook is not a platform for this kind of sharing, so there is unnecessary information too.

So, I plan and develop this service that gathers this kind of information.

## What is Clog

Clog is gathering the development, startup and trend information and share them.

- Clog introduce page(Korean): [Clog - see all information of the world together]( https://dev-yakuza.posstree.com/app/clog/){:target="_blank"}

You can donwload via the link below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - see all information of the world together, ios download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - see all information of the world together, Android download"/>
    </a>
</div>

## Why make it

As I mentioned a little bit on the outline, I subscribe to the development, startup, and trend information via Facebook groups. Also, I search and see the personal blog posts like Medium and GitHub.

Getting the information like this way, it is difficult to find a good blog post and pick up the information that I like.

So I think it is helpful to develop the service that gathers and shares the development, startup, and trend information in one place.

![Clog - see all information of the world together](/assets/images/category/clog/background.jpg)


{% include in-feed-ads.html %}

## Plan the service

First, I think about the name of the service. `C` of Clog means the next of `B`log. Also, `C` pronunciation is similar to `See`, so Clog(`See log`) means seeing logs!

Clog's MVP(Minimum Viable Product) is below.

1. Gather information: gather the development/startup/trend information, especially blog.
1. Provide information API: serve API to provide the information.
1. Blog List: Get the blog list via API, and show them.
1. Blog detail: if the user clicks the item of the list, show the detail of the blog post.

MVP is versy simple. I just focus `Gather the articles, and show them`.

## Design

I was a developer who think the design is not my area, and the design is best difficult part for me. When I worked as the frontend developer on small companies, developers also solve the UI/UX problems, so I am familiar to use the design tool. However, the design is based on the sense unlike solving the problem clearly, I think. So I feel it is very hard.

However, I developed some toy projects and failed, so I think my design skill grew up. Practice is the most important thing.

![Clog - see all information of the world together. Logo design](/assets/images/category/clog/development-journal/logo.jpg)


I got the logo idea from `See log`. I designed `C` looks like `Eye` shape to emphasis `See`. Also, I added an eyebrow and designed the pupil of the eye to be closed to the log.

I chose blue by the main color to give trust and stability. To make it fresher, I raised the tone brightly.

![Clog - see all information of the world together. Logo design](/assets/images/category/clog/development-journal/all_design.jpg)


I designed 1~2 page of the application, but when I was developing it, I needed more and more designs. I used `sketchapp` to design all.

{% include in-feed-ads.html %}

## System structure

Clog's system structure is below.

![Clog - see all information of the world together. system structure](/assets/images/category/clog/development-journal/system-architecture.jpg)


The application is developed by `React Native` to support iOS / Android both. Main API server is developed by `Laravel(php)`, and the crawling server is developed by `Django(python)`.

Honestly, it does not need to separate API server and crawling server, but I am a poor developer, so I couldn't keep the server on AWS, and GCP. So I searched a cheap hosting service, and I found `Dothome`(Korea) and `Heroku`, and I thought I can keep the service cheapest.

![Clog - see all information of the world together. Dothome hosting](/assets/images/category/clog/development-journal/dothome_plan.jpg)


If I buy the domain on Dothome, I can use unlimited web hosting for free. Unlimited web hosting gives `1G` for basic traffic, and after it, Dothome limits the speed. I don't know exactly how speed is slower, but I didn't serve images and videos, so I think I won't have any problem to keep the service. If I have any trouble because of the traffic, I can get unlimited traffic by paying just 5 dollors. (This blog post doesn't relate to Dothome.)

If you want to know more details, see the link below(Korean).

- [Dothome - unlimited web hosting](https://www.dothome.co.kr/web/premium/index.php){:rel="nofollow noreferrer noopener" target="_blank"}

The problem is that Dothome provides only `php`, so I should select `Laravel` when I thought the system structure. Also, I can't use SSH, so I can't use `crontab`. So I need an another server for regular works.

Heroku is a cloud service that supports variable languages, and we can use it for free. However, the free plan is not high performance, so I decided to use Dothom for the main API server, and Heroku for the regular works.

Heroku provides `550 free dyno hours` for free. Dyno hours is just hours that you can use the server. If you use the server 24 hours, you can keep the server 22 days, so it is not full month. Fortunately, If you register a credit card, you can get `450 dyno hours` additionaly, so you can use `1000 dyno hours` totally. If the server alive 24 hours, the server is kept for 41 days.

![Clog - see all information of the world together. heroku free plan](/assets/images/category/clog/development-journal/heroku_plan.jpg)


A problem is that the server goes on the sleep mode after 30 minutes inactive. If the server is the sleep mode, waking up takes time. This is one of the reasons that I decide Heroku for only the crawling server not the API server.

If you want to know more details about Heroku free plan, see the link below. (This blog post is not related to Heroku)

- [Heorku - Free plan](https://www.heroku.com/free){:rel="nofollow noreferrer noopener" target="_blank"}

The final system structure is below.

![Clog - see all information of the world together. hosting system structure](/assets/images/category/clog/development-journal/system-architecture-hosting.jpg)


The application is made by React Native. The API server is made by Laravel on Dothome php server and mysql, and the crawling server is made by Django on Heroku.

In retrospect, I don't need Django on Heroku. pure Python is enough for crawling.

{% include in-feed-ads.html %}

## DB design

I should use Mysql, supported by Dothome, for DB, so I used MySQL Workbench to design DB like below.

![Clog - see all information of the world together. DB design](/assets/images/category/clog/development-journal/db_erd.jpg)


## API server development

The API server is developed by Laravel. Among PHP frameworks I've used so far, I think Laravel was the best, so I used Laravel.

The feature is very simple, just getting the data from DB, and sending it via API, so developing do not take time.

I used Dothome server, so I need to deploy via `FTP`, and I should think about PHP version and Mysql version on Dothome. At the first time, I deployed via FTP many times, but the web service is not working. Later, I knew Dothome server's PHP version is lower than my local PC, so I changed the version, and then it works well. How long has it been since I've done FTP deployment...Fortunately, there is `git-ftp` open source, I can deploy easily.

- [Upload files via Git FTP]({{site.url}}/git/git-ftp/){:target="_blank"}

This server has the login feature. I use `JWT(Json Web Token)` for the login authentication.

- [jwt installation&settings]({{site.url}}/laravel/jwt/){:target="_blank"}
- [jwt:signup]({{site.url}}/laravel/jwt-signup){:target="_blank"}
- [jwt:signin]({{site.url}}/laravel/jwt-signin){:target="_blank"}
- [jwt:user information]({{site.url}}/laravel/jwt-user-info){:target="_blank"}
- [jwt:refresh token]({{site.url}}/laravel/jwt-refresh-token){:target="_blank"}
- [jwt:logout]({{site.url}}/laravel/jwt-logout){:target="_blank"}

## Crawling server development

Web crawling has possible to occur legal problems, so I chose `RSS(Rich Site Summary)` crawling for this service.

RSS feed purpose also is for the individual to subscribe, so it makes legal problems, too. However my service is not big as Google, and just shows only the title, image, and the part of the description, and clicks the post, I didn't use the redirect, just show the site directly. So, I thought I don't have big problems. Also, I crawl the personal blog, or startup news instead of the major news not to make a trouble.

I use personal blog list, and GitHub `awesome-devblog` repository(Korean).

- [https://github.com/sarojaba/awesome-devblog](https://github.com/sarojaba/awesome-devblog){:rel="nofollow noreferrer noopener" target="_blank"}

I also use many resource to crawl.

## Application development

I use React Native to develop the app for iOS / Android both. The application is very simple just to get the data via API, and show it on the screen.

I used Typescript and Styled Components with React Native.

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [RN(React Native)에서 root import하기]({{site.url}}/react-native/root-import/){:target="_blank"}

I generated the app icon and splash image by react-native-make library.

- [App icon & Splash image in React Native]({{site.url}}/react-native/react-native-make/){:target="_blank"}
- [App Splash screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}

I use react-navigation v5 for the navigation.

- [react-navigation V5]({{site.url}}/react-native/react-navigation-v5/){:target="_blank"}

And, for analyzing and showing the advertisement, I use react-native-firebase v6.

- [react-native-firebase V6 installation]({{site.url}}/react-native/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/react-native/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/react-native/react-native-firebase-v6-admob/){:target="_blank"}

This application has Native advanced advertisement instead of Banner. However, react-native-firebase doesn't support Native advanced. To display Native advancedm, I use react-native-admob-native-ads.

- [Admob Native Advanced on React Native]({{site.url}}/react-native/react-native-admob-native-ads/){:target="_blank"}

Lastly, this application has the video tab, and plays the Youtube vidoes on the video tab. For this feature, I use react-native-youtube library.

- [Play Youtube on React Native]({{site.url}}/react-native/react-native-youtube/){:target="_blank"}

I tried to use react-native-video, but it takes time to generate Youtube download link, and has limitation(The download link can be generated one time for 6 hours in one IP). So, I decided to use react-native-youtube library. You can see the details on the link above.

{% include in-feed-ads.html %}

## Issue on development

I thought developing this service doesn't have big issues, but I got some issues like below.

### Dothome hosting

As I mentioned above, my first Laravel server is not working on the Dothome hosting. So, I changed old PHP on the local, and develop Laravel server again.

Also, I needed to use FTP for deploying, and I needed to configure `.htaccess` to use Laravel on Dothome server.

### Play video

To play automatically the video, I tried to use react-native-video and react-native-ytdl, but I had an issue to generate the download link on the same IP, and it is difficult to make a video controller on Android.

So, I stopped to use react-native-video, and decided to use react-native-youtube. react-native-youtube doesn't have any trouble on iOS, but on Android, I couldn't show multiple videos on the same screen. Now I developed to play first of the video list, and play it automatically.

### Reject

iOS reject is best difficult. The application's MVP is below.

1. Blog List: Get the blog list via API, and show them.
1. Blog detail: if the user clicks the item of the list, show the detail of the blog post.

I developed the features above, and I applied the application review. My application is rejected because this application just displays the information gathered on the web. For this reject, I developed the features below.

1. Recommend(like) feature
1. Share
1. Recent/Pickup ordering
1. Bookmark
1. Following the author
1. Youtube video

I tried to develop and send the review one by one to check what feature makes the review passed. After developing playing Youtube video in the application, I could pass the first rejection.

Next, the rejection reason is that the application has the article uploaded by users, but there is no hiding the article feature. So I added the features below.

1. hide the article.
1. hide the author's all article.

After it, I applied for the review, and the application was passed. After iOS review, I applied for Android review, and there is no problem deploy Android application.

{% include in-feed-ads.html %}

## Development period

I guess all features development of the service takes 2 months. I develop with the lean style, so I can't tell you how long time takes to develop exactly. The below is brief of the development period.

- Plan and search: 1 week
- Design: 1 week
- Application development: 1 month
- Crawling server: 1 month
- API server: 1 month

The period above doesn't have any meaning. I just developed when I have free time in the morning, noon, night, and weekend, so it is not exactly working time.

I started on May and finished on the end of June.

## Retrospective

- This toy project is my first project that uses the server.
- As I am a poor developer, I think deeply about how to keep the service cheapest.
- If I don't make it, I don't know the difficulties. (various rejection reasons)
- Development is fun!

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - see all information of the world together, ios download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - see all information of the world together, Android download"/>
    </a>
</div>
