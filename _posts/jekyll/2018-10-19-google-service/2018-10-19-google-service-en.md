---
layout: 'post'
permalink: '/jekyll/google-service/'
paginate_path: '/jekyll/:num/google-service/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'google service'
description: 'introduce how to integrate google search console / analytics / adsense to jekyll project'
image: '/assets/images/category/jekyll/google-service.jpg'
---

## outline
if you want to gather the money or the insight from your blog, we think integrating google service to your blog is important. we introduce how to integrate google service to jekyll project.

we will introduce below service.

- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

## Google Analytics
if you want to analyze your site, we recommend to use Google Analytics service. click below link to go to the service site and sigin with google account.

- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}

after login, you can see below screen. click ```sign up``` button to go to next step.

![google analytics signup](/assets/images/category/jekyll/google/analytics/signup.png)

input your site informations to the form and click ```Get Tracking ID``` to get tracking code.

![google analytics register site](/assets/images/category/jekyll/google/analytics/register-site.png)

when tracking code is issued, copy the code under the ```Global Site Tag (gtag.js)``` and paste to the ```_include/head.html```. layout file may vary depending on your theme.

![google analytics tracking code](/assets/images/category/jekyll/google/analytics/tracking-code.png)

warning: above code is test code for the example. don't copy-paste. copy-paste your tracking code.

## Google Search Console
if we register our site to Google Search Console, the site is able to be searched on Google. click below link to go to the Google Search Console site.

- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}

click ```Start now``` to starting Google Search Console when you see below screen.

![google search console start](/assets/images/category/jekyll/google/search-console/start.png)

input your site URL to register to Google Search Console.

![google search console start](/assets/images/category/jekyll/google/search-console/register.png)

if you see below screen, select ```Google Analytics``` and click ```VERIFY``` button for verifying your site.

![google search console verify](/assets/images/category/jekyll/google/search-console/verify.png)

now register your sitemap for google bot can crawl your site.

![google search console sitemap](/assets/images/category/jekyll/google/search-console/sitemap.png)

completed to integrate Google Search Console. now Google bot starts to crawl. we just wait for it.

if Google bot can not crawl the site or take a long time, you can request your site to crawl directly.

![google search console request](/assets/images/category/jekyll/google/search-console/request.png)

input the site URL which you want to crawl on the top of the page. when you see above screen, click ```REQUEST INDEXING``` button to request crawling

completed to integrate Google Search Console. our site can be searched in Google.

## Google Adsense
we thought we can not be rich by the blog but we need to practice to integrate Google Adsense and want to get money a little bit. so let's integrate Google Adsense to jekyll blog.

click below link to go to the Google Adsense service site.

- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

click ```sign up``` for registering Google Adsense service.

![google adsense signup](/assets/images/category/jekyll/google/adsense/signup.png)

after registering, we need to register payment informations. you should write person's informations who get the money from Google Adsense service.

![google adsense payment](/assets/images/category/jekyll/google/adsense/payment.png)

and we just wait for Google Adsense allow it. normally take one day, but we took 2~3 weeks. we think we registered it when the blog site release. so we didn't have many contents(pages). that is reason not to allow it maybe.

so if you are in same situation, try to make contents(pages).

![google adsense get](/assets/images/category/jekyll/google/adsense/get.png)

if many users see our blog or click the advertisement on the blog, Google Adsense gives us the money like above screen. we can withdraw that if that is more than a certain amount(¥8,000). when we withdraw that, we will write the blog about how to withdraw it.

## reference
- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}