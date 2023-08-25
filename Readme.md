
# UNIVPET

<div align="center">
<img width="329" alt="image" src="https://i.ibb.co/Mgm7z9z/2-3.png">
</div>

# 2023th Sinchonthon
> **신촌톤 UNIVPET** <br/>

## 배포 주소

> 3.38.34.206 <br>

## 팀 소개

|      김민영 <br/> **(기획/디자인)**       |          정주원 <br/> **(프론트엔드)**          |       최지원 <br/> **(프론트엔드)**        |
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   <img src="https://i.ibb.co/2y5LwSZ/kmy.jpg" alt="kmy" width="160px">    |                      <img src="https://i.ibb.co/ZLqz0YW/jjw.jpg" alt="jjw" width="160px">    |                   <img src="https://i.ibb.co/tXyRMBM/cjw.jpg" alt="cjw" width="160px">  |//github.com/THLcode)  |
|   [minyounggkim](https://github.com/minyounggkim)   |    [ju1e3718](https://github.com/ju1e3718)  |    [JiwonChoi0805](https://github.com/JiwonChoi0805)  |
| 홍익대 경영학과  | 홍익대 컴퓨터공학 | 이화여대 컴퓨터공학 |

|      김규빈 <br/> **(백엔드)**       |          손지석 <br/> **(백엔드)**          |       신선희 <br/> **(백엔드)**        |       신수빈  <br/> **(백엔드)**       | 
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | 
|   <img src="https://i.ibb.co/BywjTNd/kkb.jpg" alt="kkb" width="160px">    |                      <img src="https://i.ibb.co/GQk1mR6/sjs.jpg" alt="sjs" width="160px" />    |                   <img src="https://i.ibb.co/PNYq2gN/ssh.jpg" alt="ssh" width="160px">   | <img src="https://i.ibb.co/YtL1Lqr/ssb.jpg" alt="ssb" width="160px" /> |
|   [kyubiin](https://github.com/kyubiin)   |    [jiseokson](https://github.com/jiseokson)  |    [fressh1127](https://github.com/fressh1127)  |    [2020147508](https://github.com/2020147508)  |
| 서강대 영문, 컴퓨터공학  | 홍익대 컴퓨터공학 | 서강대 수학, 컴퓨터공학 | 연세대 컴퓨터과학 |

## 프로젝트 소개


**UNIVPET**는 학교생활을 하며 겪는 다양한 불편함을 서로 공유하고 동의하는 **대학생 청원 플랫폼**입니다. 일정 이상의 동의가 모이면 학교로 직접 건의되는 서비스가 제공됩니다.

#### UNIVPET, 대학생을 위한 청원 플랫폼
**UNIVPET**과 함께라면 학생들은 불편함을 간단하면서도 강력하게 전달할 수 있으며 학교, 학생회는 반복되는 업무에서 오는 불편함을 최소화 할 수 있습니다.

#### UNIVPET, 간단한 사용과 편리함

1. 간편하게 구글을 통해 **회원가입 및 로그인**을 해주세요.
2. 나의 불편함을 작성하거나, 공감되는 청원에 **동의**해주세요.
3. 학교에 전달되기를 기다리면 끝 !!

## 시작 가이드
### 필수사항
해당 어플리케이션을 동작하기 위해선 다음 버전 이상이 필요해요.

- [Node.js 14.19.3](https://nodejs.org/ca/blog/release/v14.19.3/)
- [Npm 9.2.0](https://www.npmjs.com/package/npm/v/9.2.0)
- [Python 3.11.4](https://www.python.org/downloads/release/python-3114/)

### Installation
``` bash
$ git clone https://github.com/Sinchonthon-Minyoung-Team/sinchon-back.git
$ cd sinchon-back
```



#### Nginx conf
```
server {
        listen 80;
        server_name 3.39.53.3;
        location / {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/univpet-backend/run/gunicorn.sock;
                proxy_read_timeout 300s;
                proxy_connect_timeout 75s;
        }
        location /static {
                alias /home/ubuntu/univpet-backend/static;
        }
}
```





#### Backend
```
$ cd sinchon-back
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 manage.py migrate
$ sudo systemctl daemon-reload
$ sudo systemctl restart nginx
$ sudo systenctl restart gunicorn
```

#### Frontend
```
$ cd education
$ npm install 
$ npm run dev
```

---

## Stacks 🐈

### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Config
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)        

### Development
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white)

### Communication
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)

---
## 화면 구성 📺
| **메인 페이지**  |  **청원 신청**   |
| :-------------------------------------------: | :------------: |
|  <img width="329" src="https://i.ibb.co/tK1Zp27/image.png"/> |  <img width="329" src="https://i.ibb.co/sCr0Cy1/image.png"/>|  
| **동의 진행 청원**   |  **학교 전송 청원**   |  
| <img width="329" src="https://i.ibb.co/dcJGnSt/image.png"/>   |  <img width="329" src="https://i.ibb.co/nsfr0fx/image.png"/>     |

---
## 주요 기능 📦

### ⭐️ 청원 신청에 대한 기능
- 불편함에 대해 새로운 청원을 신청할 수 있음
- 카테고리를 선택하여 원하는 청원 목적을 선정할 수 있음

### ⭐️ 동의 진행 청원에 대한 기능
- 동의 진행 중인 청원을 열람할 수 있음
- 기간 동안에는 자유롭게 동의하거나 댓글을 통해 의견을 남길 수 있음

### ⭐️ 학교 전송 청원에 대한 기능
- 동의율이 100% 달성한 청원을 열람할 수 있음
- 해당 청원에 대한 내용은 학교에 직접 전송됨

---
## 아키텍쳐

### 디렉토리 구조
```bash
├── README.md
├── package-lock.json
├── package.json
├── server : 백엔드
│   ├── README.md
│   ├── requirements.txt
│   ├── manage.py
│   ├── api1 : api1에 대한 정보
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── etc..
│   ├── api2 : api2에 대한 정보
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── etc..
│   ├── api3 : api3에 대한 정보
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── etc..
│   ├── extensions
│   │   └── users-permissions : 권한 정보
└── front : 프론트엔드
    ├── README.md
    ├── public
    │   ├── favicon.ico
    │   └── logo_about.png
    ├── components
    │   ├── a.js : 필요시 설명~
    │   ├── b.js
    │   ├── c.js
    │   ├── d.js
    │   ├── e.js
    │   ├── f.js
    │   ├── g.js
    │   ├── h.js
    │   └── i.js
    ├── package-lock.json
    ├── package.json
    ├── pages
    │   ├── page1.js
    │   ├── page2.js
    │   ├── page3.js
    │   ├── page4.js
    │   ├── newcourse
    ├── app.js
    ├── index.js
    ├── router.js
    └── styles
        └── GlobalStyle.js

```

<!--
```bash
├── README.md : 리드미 파일
│
├── strapi-backend/ : 백엔드
│   ├── api/ : db model, api 관련 정보 폴더
│   │   └── [table 이름] : database table 별로 분리되는 api 폴더 (table 구조, 해당 table 관련 api 정보 저장)
│   │       ├── Config/routes.json : api 설정 파일 (api request에 따른 handler 지정)
│   │       ├── Controllers/ [table 이름].js : api controller 커스텀 파일
│   │       ├── Models : db model 관련 정보 폴더
│   │       │   ├── [table 이름].js : (사용 X) api 커스텀 파일
│   │       │   └── [table 이름].settings.json : model 정보 파일 (field 정보)
│   │       └─── Services/ course.js : (사용 X) api 커스텀 파일
│   │ 
│   ├── config/ : 서버, 데이터베이스 관련 정보 폴더
│   │   ├── Env/production : 배포 환경(NODE_ENV = production) 일 때 설정 정보 폴더
│   │   │   └── database.js : production 환경에서 database 설정 파일
│   │   ├── Functions : 프로젝트에서 실행되는 함수 관련 정보 폴더
│   │   │   │   ├── responses : (사용 X) 커스텀한 응답 저장 폴더
│   │   │   │   ├── bootstrap.js : 어플리케이션 시작 시 실행되는 코드 파일
│   │   │   │   └── cron.js : (사용 X) cron task 관련 파일
│   │   ├── database.js : 기본 개발 환경(NODE_ENV = development)에서 database 설정 파일
│   │   └── server.js : 서버 설정 정보 파일
│   │  
│   ├── extensions/
│   │   └── users-permissions/config/ : 권한 정보
│   │ 
│   └── public/
│       └── uploads/ : 강의 별 사진
│
└── voluntain-app/ : 프론트엔드
    ├── components/
    │   ├── NavigationBar.js : 네비게이션 바 컴포넌트, _app.js에서 공통으로 전체 페이지에 포함됨.
    │   ├── MainBanner.js : 메인 페이지에 있는 남색 배너 컴포넌트, 커뮤니티 이름과 슬로건을 포함.
    │   ├── RecentLecture.js : 사용자가 시청 정보(쿠키)에 따라, 현재/다음 강의를 나타내는 컴포넌트 [호출: MainCookieCard]
    │   ├── MainCookieCard.js : 상위 RecentLecture 컴포넌트에서 전달받은 props를 나타내는 레이아웃 컴포넌트.
    │   ├── MainCard.js : 현재 등록된 course 정보를 백엔드에서 받아서 카드로 나타내는 컴포넌트 [호출: CourseCard]
    │   └── CourseCard.js : 상위 MainCard 컴포넌트에서 전달받은 props를 나타내는 레이아웃 컴포넌트
    │
    ├── config/
    │   └── next.config.js
    │
    ├── lib/
    │   └── ga/
    │   │   └── index.js
    │   └── context.js
    │
    ├── pages/
    │   ├── courses/
    │   │   └── [id].js : 강의 페이지
    │   ├── _app.js : Next.js에서 전체 컴포넌트 구조를 결정, 공통 컴포넌트(navbar, footer)가 선언되도록 customizing 됨.
    │   ├── _document.js : Next.js에서 전체 html 문서의 구조를 결정, lang 속성과 meta tag가 customizing 됨.
    │   ├── about.js : 단체 소개 페이지
    │   ├── index.js : 메인 페이지
    │   ├── question.js : Q&A 페이지
    │   └── setting.js : 쿠키, 구글 애널리틱스 정보 수집 정책 페이지
    │
    ├── public/
    │   ├── favicon.ico : 네비게이션바 이미지
    │   └── logo_about.png : about 페이지 로고 이미지
    │
    └── styles/
        └── Home.module.css

```
-->
