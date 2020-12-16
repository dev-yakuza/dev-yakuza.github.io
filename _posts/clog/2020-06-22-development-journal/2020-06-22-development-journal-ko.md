---
layout: 'post'
permalink: '/clog/development-journal/'
paginate_path: '/clog/:num/development-journal/'
lang: 'ko'
categories: 'clog'
comments: true

title: '「Clog」 서비스 개발기(React Native, Laravel, Django)'
description: 'React Native, Laravel, Django를 사용하여 「Clog」라는 서비스를 제작해 보았습니다. 이 서비스를 제작하면서 격은 내용을 정리해보려고 합니다.'
image: '/assets/images/category/clog/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [목차](#목차)
- [개요](#개요)
- [Clog란](#clog란)
- [왜 만들게 되었나](#왜-만들게-되었나)
- [서비스 기획](#서비스-기획)
- [디자인](#디자인)
- [시스템 구성](#시스템-구성)
- [DB 설계](#db-설계)
- [API 서버 개발](#api-서버-개발)
- [크롤링 서버 개발](#크롤링-서버-개발)
- [앱 개발](#앱-개발)
- [개발중 문제](#개발중-문제)
  - [닷홈 호스팅](#닷홈-호스팅)
  - [비디오 재생](#비디오-재생)
  - [리젝](#리젝)
- [개발 기간](#개발-기간)
- [회고](#회고)

</div>

## 개요

벌써 16번째 토이 프로젝트네요. 아래 링크를 통해 지금까지 제가 개발한 토이프로젝트를 확인할 수 있습니다. 궁금하신 분들은 아래 링크를 통해 확인해 보세요.

- [JeongHean's App List]({{site.url}}/app/list/ko/){:target="_blank"}

토이프로젝트를 개발하면서 작성한 개발기도 있습니다.

- [BlaBoo 앱 개발기(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumoncho 앱 개발기(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}
- [일단공부 앱 개발기(RN, React Native)]({{site.url}}/ildangongbu/development-journal/){:target="_blank"}

저는 주로 페이스북 그룹을 통해 개발, 스타트업, 자기 개발 등의 정보를 얻고 있습니다. 하지만, 페이스북이 이런 정보 공유를 위해 탄생한 플랫폼이 아니므로, 불필요한 정보들도 많이 가지고 있습니다.

그래서 꼭 제게 필요한 정보만을 모아볼 수 있는 앱이 있으면 좋겠다고 생각해서 이번 서비스을 기획 및 제작하게 되었습니다.

## Clog란

Clog는 개발, 스타트업, 자기 개발 등 유용한 정보를 얻기 위해 블로그, 검색, 페이스북 등을 통해 얻던 방식을 개선하기 위해, 한 곳에서 모든 정보를 모아보는 서비스입니다.

- Clog 소개 페이지: [Clog - 세상의 모든 정보를 모아보다]( https://dev-yakuza.posstree.com/app/clog/){:target="_blank"}

아래는 앱을 다운로드 받을 수 있는 링크입니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - 세상의 모든 정보를 모아보다, ios 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - 세상의 모든 정보를 모아보다, 안드로이드 다운로드"/>
    </a>
</div>

## 왜 만들게 되었나

개요에서도 잠깐 이야기 했지만, 저는 개발/스타트업/자기 개발 등의 정보를 페이스북 그룹을 통해서 얻고 있습니다. 또한 브런치나 GitHub, tstory 등과 같은 개인 블로그도 검색을 통해서 찾아보곤 합니다.

이렇게 필요한 정보를 얻기 위해서, 페이스북을 확인하거나 좋은 블로그들을 찾아 보는게 어렵고, 이런 방식은 원하는 정보만을 골라 볼 수가 없는 단점이 있었습니다.

그래서 개발/스타트업/자기 개발 등과 같은 정보를 한 곳에서 모아볼 수 있는 서비스를 제작하면 도움이 되지 않을까 싶어서 이번 서비스를 제작하게 되었습니다.

![Clog - 세상의 모든 정보를 모아보다](/assets/images/category/clog/background.jpg)


{% include in-feed-ads.html %}

## 서비스 기획

일단 네이밍은 Clog의 `C`는 `B`log의 다음 버전을 의미하기 하고 있습니다. 또한 `C`가 영어의 `See`와 발음이 유사한 점도 고려하여 `See log`, 즉 기록을 보다라는 의미도 함축하도록 하였습니다.

Clog의 MVP(Minimum Viable Product: 최소 기능 제품)는 아래와 같이 정의했습니다.

1. 정보 수집: 개발/스타트업/자기 개발 등과 관련 된 정보, 특히 블로그를 모은다.
1. 정보 제공 API: 위에서 모은 정보를 API로 공급한다.
1. 블로그 리스트: API를 통해 블로그 포스트 리스트들을 받아오고 이를 보여준다.
1. 블로그 상세: 리스트에서 자세히 보고자 하는 아이템을 선택하면, 해당 블로그에 대한 상세 내용이 보인다.

다른 앱들을 제작할 때보다, MVP가 매우 간단했었습니다. `글들을 모으고, 글들을 보여준다.`에 집중하였습니다.

## 디자인

저는 디자인은 제 영역이 아니라고 생각하고 살아온 개발자입니다. 그래서 디자인이 제일 어렵습니다. 작은 회사에서 프론트엔드 개발할 때, 왠만한 문제는 개발자들이 UI/UX도 하기 때문에, 툴을 다루는 것에 대한 불편함은 없지만, 문제를 해결하는 개발과는 다른 디자인은 센스에 영역이기 때문에 큰 어려움을 느끼고 있습니다.

그래도 토이프로젝트를 진행하면서 고민하고, 실패하면서 점점 좋아지고 있는게 아닌가 싶습니다. 역시 연습이 제일 중요한거 같네요.

![Clog - 세상의 모든 정보를 모아보다. 로고 디자인](/assets/images/category/clog/development-journal/logo.jpg)


로고는 `See log`에서 아이디어를 떠올렸습니다. `보다`라는 의미를 강조하기 위해 `C`를 사람의 `눈` 모양으로 디자인 해 보았습니다. 또한, 큰 로고에는 눈을 뜨고 log를 바라보는 이미지로써, 눈썹 이미지를 추가했으며 눈동자가 log쪽에 좀 더 가깝도록 디자인 해 보았습니다.

메인 색상은 신뢰와 안정감을 줄 수 있는 파랑색 계열로 했으며, 좀 더 신선함을 주기 위해, 밝게 톤을 올렸습니다.

![Clog - 세상의 모든 정보를 모아보다. 로고 디자인](/assets/images/category/clog/development-journal/all_design.jpg)


앱의 전체 디자인은, 처음엔 1~2 페이지만 디자인을 했는데, 개발하다가 점점 필요한 기능들이 많아지면서 위와 같이 디자인이 많아지게 되었습니다. 전체적인 디자인은 `sketchapp`으로 제작했습니다.

{% include in-feed-ads.html %}

## 시스템 구성

Clog는 다음과 같은 시스템으로 구성되어 있습니다.

![Clog - 세상의 모든 정보를 모아보다. 시스템 구성도](/assets/images/category/clog/development-journal/system-architecture.jpg)


앱은 `React Native`로 개발하여, iOS / Android에서 모두 사용하게 만들었습니다. 주 서버가 될 API 서버는 `Laravel(php)`로 구성하였으며, 정보를 모으는 크롤링 서버는 `Django(python)`으로 구성하였습니다.

사실 크롤링 서버와 API 서버를 따로 분리할 필요없이 하나에 서버에서 사용해도 됩니다. 하지만, 제가 가난한 개발자이다 보니, AWS나 GCP를 유지할 여력이 되지 않아, 저렴한 호스팅 서비스에 눈을 돌렸고, 국내 호스팅인 `닷홈`과 `heroku`를 조합하면 저렴하게 서비스를 유지할 수 있을 거 같다는 생각이 들었습니다.

![Clog - 세상의 모든 정보를 모아보다. 닷홈 호스팅](/assets/images/category/clog/development-journal/dothome_plan.jpg)


닷홈은 도메인을 구입하면 무제한 웹 호스팅을 사용할 수 있습니다. 무제한 웹 호스팅은 하루 `1G`까지 기본 트래픽이 제공되고, 그 이후에는 웹 서비스가 속도가 제한된다고 합니다. 현재까지 1G를 초과해본 적이 없어 얼마나 느려지는지 테스트 해보지 못했지만, 사진, 동영상 등을 서비스하고 있지 않기 때문에 큰 문제없이 서비스를 유지할 수 있을거라고 판단하였습니다. 사용자가 많아 문제가 되면, 5000원을 내고 무제한 트래픽을 사용하면 되지 않을까 싶습니다. (이 블로그 포스트는 닷홈과는 무관함을 알려드립니다.)

자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [닷홈 - 무제한 웹호스팅](https://www.dothome.co.kr/web/premium/index.php){:rel="nofollow noreferrer noopener" target="_blank"}

문제는 닷홈이 `php`만을 서비스하고 있습니다. 그래서 시스템을 구성할 때 `Laravel`을 선택하였습니다. 또한, ssh 접근도 불가능하고, `crontab` 등을 사용할 수 없으므로, 정기적으로 작업하는 서버가 별도로 필요하게 되었습니다.

Heroku는 다양한 언어를 지원하는 클라우드 서비스로 `무료`로 사용이 가능합니다. 하지만, 무료이다보니 성능적인 면에서 좀 떨어지는 면이 있어서, 닷홈을 메인 API 서버로 두고, Heroku 서버를 크롤링을 전담하는 서버로 만들었습니다.

Heroku는 무료로 `550 free dyno hours`를 제공합니다. dyno hours라고 표시했는데 결국, 사용 가능한 가용 시간을 의미합니다. 하루 24시간을 가동하면 22일 정도 사용할 수 있습니다. 그럼 30일 한달 동안을 사용하지 못하는 문제가 있습니다. 하지만 불행중 다행으로, 신용 카드를 등록하면 추가로 `450 dyno hours`를 추가로 제공하고 있어, 도합 `1000 dyno hours`를 사용할 수 있습니다. 그럼 24시간을 가동해도 41일이 되므로, 한달 내내 무료로 사용할 수 있게 됩니다.

![Clog - 세상의 모든 정보를 모아보다. heroku free plan](/assets/images/category/clog/development-journal/heroku_plan.jpg)


문제는 이렇게 무료로 사용할 수 있지만, 30분간 아무것도 하지 않으면, 슬립 모드로 들어가고, 다시 깨우면 시간이 걸리게 됩니다. 그래서, API 서버로는 적당하지 않다고 판단하고, 정기적인 작업을 돌려서 서버를 계속 사용하도록 구성하였습니다.

Heroku의 무료 요금제에 관한 자세한 사항은 아래에 링크를 참고하시기 바랍니다. (이 블로그 포스트는 Heroku와 어떤 관련도 없음을 알려드립니다.)

- [Heorku - 무료 플랜](https://www.heroku.com/free){:rel="nofollow noreferrer noopener" target="_blank"}

이렇게 해서 완성된 시스템 구성이 아래와 같습니다.

![Clog - 세상의 모든 정보를 모아보다. 호스팅 시스템 구성도](/assets/images/category/clog/development-journal/system-architecture-hosting.jpg)


React Native로 앱을 개발하고, 닷홈에서 제공하는 php 서버와 mysql을 Laravel API 서버로 구성하고, 마지막으로 Heroku에 Django를 올리고 정기적인 크롤링 작업을 하도록 하였습니다.

다시 되돌아 보면 Heroku에는 django까지 올릴 필요는 없었던거 같습니다. 단순히 크롤링만 하므로 순수 Python으로도 충분했다고 생각이 드네요.

{% include in-feed-ads.html %}

## DB 설계

DB는 닷홈에서 Mysql을 제공하므로, Mysql을 사용해야 했습니다. 그리고 MySQL Workbench를 사용하여 아래와 같이 DB를 설계하였습니다.

![Clog - 세상의 모든 정보를 모아보다. DB 설계도](/assets/images/category/clog/development-journal/db_erd.jpg)


## API 서버 개발

API 서버 개발은 Laravel로 구성하였습니다. 지금까지 써본 PHP 프레임워크중에는 라라벨이 가장 좋았던거 같아서, Laravel을 사용하게 되었습니다.

단순히, DB에 있는 정보를 가져와 전달하는 서버여서 개발하는 시간은 그리 오래 걸리지 않았습니다.

다만, 닷홈에 `FTP`로 배포를 해야하고, 닷홈에서 제공하는 PHP 버전과 Mysql 버전을 고려해야 했습니다. 처음에 개발할 때는, 이걸 고려하지 않아, 아무리 FTP로 올려도 제대로 동작하지 않았습니다. 아, 그리고 얼마만에 해보는 FTP 배포인가...다행이 `git-ftp`라는 오픈 소스가 있어서, 좀 수월하게 배포할 수 있게 되었습니다.

- [Git FTP를 사용하여 배포하기]({{site.url}}/git/git-ftp/){:target="_blank"}

이번 서비스에는 로그인 기능이 있습니다. 로그인 인증 기능에는 `JWT(Json Web Token)`을 사용하고 있습니다.

- [jwt 설치 및 설정]({{site.url}}/laravel/jwt/){:target="_blank"}
- [jwt:회원가입]({{site.url}}/laravel/jwt-signup){:target="_blank"}
- [jwt:로그인]({{site.url}}/laravel/jwt-signin){:target="_blank"}
- [jwt:사용자 정보]({{site.url}}/laravel/jwt-user-info){:target="_blank"}
- [jwt:토큰 갱신]({{site.url}}/laravel/jwt-refresh-token){:target="_blank"}
- [jwt:로그아웃]({{site.url}}/laravel/jwt-logout){:target="_blank"}

## 크롤링 서버 개발

웹에 있는 정보를 그대로 크롤링하는 것은 많은 법적 문제를 일으킬 수 있기 때문에, 이번 서비스에서는 `RSS(Rich Site Summary)`를 사용한 크롤링 서버를 구성하였습니다.

RSS 피드도 개인적으로 구독하는 것을 목적으로 두기 때문에 법적인 문제가 될 수 있습니다. 하지만, 제 서비스가 네이버나 다음처럼 굉장히 많은 트래픽을 잡아 먹는 서비스도 아니고, 단순 제목, 이미지, 본문 일부를 보여주고, 클릭하면, 리다이렉트가 아닌 직접 사이트를 오픈하기 때문에 큰 문제가 없을 거라고 판단하였습니다. 또한 큰 문제가 될만한, 메이저 뉴스보다는 개인들의 블로그나 스타트업의 기사를 가져오도록 구성하였습니다.

블로그 리스트는 개인적으로 수집한 내용 일부와 `awesome-devblog`의 GitHub에서 가져왔습니다.

- [https://github.com/sarojaba/awesome-devblog](https://github.com/sarojaba/awesome-devblog){:rel="nofollow noreferrer noopener" target="_blank"}

이외에도 여러 리소스들을 활용하여, 크롤링을 진행하고 있습니다.

## 앱 개발

앱은 React Native를 통해 iOS, 안드로이드를 개발/배포하였습니다. 앱은 단순히 API를 통해 필요한 데이터를 얻고, 화면에 표시하므로 그렇게 어려운 기술을 사용하고 있지 않습니다.

앱의 기본 구조는 Typescript와 Styled components를 사용하고 있습니다.

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [RN(React Native)에서 root import하기]({{site.url}}/react-native/root-import/){:target="_blank"}

앱 아이콘과 Splash 이미지 적용은 react-native-make라는 라이브러리를 사용하고 있습니다.

- [React Native에서 App 아이콘 & Splash 이미지 만들기]({{site.url}}/react-native/react-native-make/){:target="_blank"}
- [App Splash 스크린]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}

내비게이션에는 react-navigation v5를 사용하고 있습니다.

- RN(React Navtive)에서 react-navigation v5 사용하기: [react-navigation V5]({{site.url}}/react-native/react-navigation-v5/){:target="_blank"}

그리고 앱 분석 및 광고에는 react-native-firebase v6를 사용하고 있습니다.

- [react-native-firebase V6 설치]({{site.url}}/react-native/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/react-native/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/react-native/react-native-firebase-v6-admob/){:target="_blank"}

이번 앱에서는 배너 광고 대신, 네이티브 광고를 사용하고 있습니다. 하지만, react-native-firebase에서는 네이티브 광고를 지원하지 않고 있습니다. 네이티브 광고를 사용하기 위해서 이번 앱에서는 react-native-admob-native-ads를 사용하고 있습니다.

- [react-native에서 네이티브 광고 사용하기]({{site.url}}/react-native/react-native-admob-native-ads/){:target="_blank"}

마지막으로 이번 앱은 비디오 탭을 가지고 있는데, 비디오는 유튜브 동영상을 재생하고 있고, 이를 위해서 react-native-youtube 라는 라이브러리를 사용하고 있습니다.

- [react-native에서 Youtube 재생하기]({{site.url}}/react-native/react-native-youtube/){:target="_blank"}

react-native-video도 시도했지만, youtube의 다운로드 링크를 만들 떄, 걸리는 시간과, 제한(한 IP에서 6시간 동안 한 번만 생성 가능)등에 문제가 있어, react-native-youtube 라이브러리를 사용하게 되었습니다. 자세한 내용은 위에 링크를 참고하시기 바랍니다.

{% include in-feed-ads.html %}

## 개발중 문제

이번 서비스는 단순해서 큰 문제없이 진행되리라고 생각했지만, 아래와 같이 몇가지 문제가 발생하였습니다.

### 닷홈 호스팅

위에서도 잠깐 이야기했지만, 처음 Laravel로 개발한 서버가 닷홈 호스팅에서 돌아가지 않는 문제가 발생하였습니다. 그래서 닷홈에서 구동 가능한 php 버전을 로컬에 설치하고, 그에 맞는 Laravel 버전을 설치한 후 다시 개발하게 되었습니다.

또한, 서버에 배포하기 위해서 FTP를 이용해야 했고, Laravel을 구동시키기 위해서 `.htaccess`을 사용해야 했습니다.

### 비디오 재생

앱에서 자연스럽게 비디오를 재생하기 위해 react-native-video와 react-native-ytdl을 사용하여 구성하였지만, 같은 IP에서 여러번 링크를 생성하는 것에 문제가 있었고, 안드로이드에서 Video 컨트롤러를 구현하는데 어려움을 겪었습니다.

그래서 react-native-video를 사용하는 것을 중지하고, react-native-youtube를 사용하기로 결정하였습니다. react-native-youtube도 iOS에서는 별 문제가 없었으나, Android에서는 여러 플레이어를 동시에 표시할 수 없어서, 화면에 표시된 Youtube에 첫번째 동영상만 플레이어를 생성하고, 재생하도록 구성하였습니다.

### 리젝

역시 가장 넘기 힘든 산은 iOS의 앱 심사네요. 앱 기능의 MVP는 아래와 같습니다.

1. 블로그 리스트: API를 통해 블로그 포스트 리스트들을 받아오고 이를 보여준다.
1. 블로그 상세: 리스트에서 자세히 보고자 하는 아이템을 선택하면, 해당 블로그에 대한 상세 내용이 보인다.

위에 기능을 구현하고, 앱을 등록하였지만, 단순히 웹 정보를 모아서 보여주는 것은 앱으로써 의미가 없으며, 네이티브 기능을 사용하지 않으므로 웹 서비스로 서비스를 제공하라며, 첫 리젝을 당했습니다. 이를 통과하기 위해 아래에 기능들을 추가하였습니다.

1. 추천(좋아요) 기능
1. 공유
1. 최신순/픽업순
1. 북마크
1. 작가 팔로우
1. Youtube 비디오

위에 기능중 하나가 개발이 끝나면, 심사를 신청하는 식으로, 어떤 기능이 추가되면 통과되는지 확인하였습니다. 그 결과 Youtube 비디오를 앱 내에서 볼 수 있도록 하는 기능을 추가하고 나서, 첫 리젝은 통과하였습니다.

그 다음은, 앱이 사용자가 올린 정보를 공유하고 있는데, 보기 싫은 정보를 숨기는 기능이 없다고 리젝을 당했습니다. 그래서 다음과 같은 기능을 추가하였습니다.

1. 해당 게시물 숨기기
1. 해당 작가 게시물 숨기기

그리고 심사를 신청하니, 통과되어 지금은 앱 스토어에 등록된 상태네요. 이렇게 통과된 앱을 구글 플레이에 배포하였고, 안드로이드는 별 문제없이 배포되었습니다.

{% include in-feed-ads.html %}

## 개발 기간

전체 서비스 개발 기간은 2개월 정도인거 같습니다. 린하게 개발을 하다보니, 정확히 어떤게 얼마나 걸렸는지 딱 짤라서 이야기하기가 어렵지만, 좀 구별해보면 아래와 같습니다.

- 기획 및 자료 조사: 1주일
- 디자인: 1주일
- 앱 개발: 1달
- 크롤링 서버: 1달
- API 서버: 1달

위에 기간은 크게 의미가 없습니다. 아침, 점심, 저녁, 주말 등 시간있을 때 틈틈히 만든거이기 때문에, 실제 걸린 시간이랑은 관계가 없습니다. 또 린스타일로 개발을 하고 있기 때문에 정확히 시간 산정이 아니고, 체감상 걸린 시간을 입니다.

개발을 5월부터 시작했고, 6월 말에 릴리스했습니다.

## 회고

- 이번 토이프로젝트는 지금까지 만든 토이프로젝트중에서 처음으로 서버를 사용하는 프로젝트였다.
- 가난한 개발자이다보니, 어떻게 하면 저렴하게 서비스를 할 수 있을지 고민을 많이 했다.
- 역시 만들어보지 않으면, 어려움을 모른다.(이런 이유의 리젝도 있구나)
- 개발은 재밌다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - 세상의 모든 정보를 모아보다, ios 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - 세상의 모든 정보를 모아보다, 안드로이드 다운로드"/>
    </a>
</div>
