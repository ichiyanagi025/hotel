#!/usr/bin/python3

import cgi
from cgitb import html
import MySQLdb
from http import cookies
import os

cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
    session_id = cookie["session_id"].value
except KeyError:
    session_id = ""
try:
    mail = cookie["user_id"].value
except KeyError:
    mail = ""

login_success = 0
name = ""

connection = MySQLdb.connect(
    host='localhost',
    user='user1',
    passwd='passwordA1!',
    db='hotel',
    charset='utf8'
)


if(len(mail)!=0 and len(session_id)!=0):
    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='hotel',
        charset='utf8'
        )

    cursor = connection.cursor()

    sql = "select * from `User` where mail = '" + mail + "';"
    cursor.execute(sql)
    rows = cursor.fetchall()

    connection.commit()
    cursor.close()

    for row in rows:
        name = row[0]
    
    print("Set-Cookie: session_id=" + session_id)
    print("Set-Cookie: user_id=" + mail)

    login_success = 1

else:
    name = "ゲスト"

print("Content-Type: text/html")

htmlText = '''

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>GAVA HOTEL</title>
    <style type="text/css">
        body{
            background-color:bisque;
        }
        html {
            scroll-behavior: smooth;
            @media (prefers-reduced-motion: reduce) {
                scroll-behavior: auto;
            }
        }
        .back {
        position: fixed;
        bottom: 10px;
        right: 10px;
        border:1px solid #888888;
        width: 30pt;
        padding:13pt;
        font-size: 15pt;<div> <span onmouseover="deletepage()">名前</span> <script type="text/javascript"> function deletepage() { document.getElementsByTagName("body").item(0).textContent = null; document.write(`<img src="https://www.teu.ac.jp/info/lab/teacher/cs/images/1633.jpg">`) } </script> </div>
        background-color: #e34646;
        filter:alpha(opacity=85);
        border-radius: 60px;
        opacity:0.85;
        cursor: pointer;
        text-decoration: none;
        text-shadow: 0 -1px 1px #FFF, -1px 0 1px #FFF, 1px 0 1px #aaa;
        } 
        a{
            display:block;
            text-decoration: none;
            color : white;
            margin-right: 35px;
        }
        a:hover{
            color: rgb(214,237,248)
        }
        nav {
            text-align: center;
        }

        nav ul {
            margin: 0;
            padding: 0;
        }

        nav li {
            list-style: none;
            display: inline-block;
            width: 20%;
            min-width: 90px;
            height: 70px;
            margin-left: auto;
            margin-right: auto;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        nav li:not(:last-child) {
            border-right: 2px solid #ddd;
        }

        nav a {
            text-decoration: none;
            color: rgba(255, 255, 255, 0.849);
        }

        nav a.current {
            color: #00B0F0;
            border-bottom: 2px solid #00B0F0;
        }

        nav a:hover {
            color: #F7CB4D;
            border-bottom: 2px solid #F7CB4D;
        }
        header{
            height: 170px;
            width: 100%;
            z-index: 9999;
            float:left;
            background-color:white;
            border: solid;
            border-color:brown;
            border-top: transparent; /* 下辺が透明になる */
            border-right: transparent;
            border-left: transparent;
            position: fixed;
            top: 0;
            left: 0;

        }
        .header2{
            background-color: #e34646;
            width:100%;
        }

            .header1-l{
                position: rerative;
            }
                .logo{
                    height:100px;
                    width:100px;
                    float: left;
                    padding: 0px 0px 
                }
                .header-title{
                    position: relative;
                    font-size: 30px;
                    bottom: 30px;
                    float: left;
                }
            .header1-r{
                float: right;
            }
        
                ul{
                    list-style: none;
                }

                .header-24{
                    position: relative;
                    right: 40px;
                    float: left;
                }

                .header-tel{
                    float: right;
                }
                .name_h{
                color:red;
                }
                .header-button{
                    color:white;
                    position: relative;
                    top: 10px;
                    left:-10px;
                    float: right;
                    margin-left:60px;
                    border:1px solid #888888;
                    padding:5pt;
                    background-color: #e34646;
                    outline: white;
                    filter:alpha(opacity=85); /*透明度*/
                    opacity:0.85;
                    box-shadow:0 5px 0 #ca1c30; /*影の色*/
                    border-radius:60px;
                    cursor:pointer;
                    text-decoration: none;
                }
            .header2{
                position: absolute;
                top: 100px;
                font-size: 20px;
            }
            .menu{
                text-align: center;
            }
            .header2 .gnav .menu {
                display: flex; /* 中の要素を横並びにする */
                
            }

            header .gnav .menu li {
                list-style: none; /* リストの[・]を消す */
            }

            header .gnav .menu li + li {
                margin-left: 40px; /* メニューそれぞれに間隔をあけるため */
            }
            .header-button:hover{
                color: black;
            }
            .header-button:active{
                box-shadow: none;
                transform: translateY(5px);
            }
            .slide{
                height: 300px;
                width: 300px;
            }
        main{
            padding-top: 180px;
        }
.reserve{
    width:50%;
    height:600px;
    margin-bottom: 20px;
}
.FlexTextarea {
overflow:scroll;
position: relative;
font-size: 1rem;
line-height: 1.8;
}

.FlexTextarea__dummy {
  overflow: hidden;
  visibility: hidden;
  box-sizing: border-box;
  padding: 5px 15px;
  min-height: 120px;
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow-wrap: break-word;
  border: 1px solid;
}

.FlexTextarea__textarea {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  overflow: hidden;
  box-sizing: border-box;
  padding: 5px 15px;
  width: 100%;
  height: 500px;
  background-color: transparent;
  border: 1px solid #b6c3c6;
  border-radius: 4px;
  color: inherit;
  font: inherit;
  letter-spacing: inherit;
  resize: none;
}

.FlexTextarea__textarea:focus {
  box-shadow: 0 0 0 4px rgba(35, 167, 195, 0.3);
  outline: 0;
}
            .concept-back-img{
                width: 100%;
                height: 500px;
                -ms-filter: blur(6px);
                filter: blur(6px);
                vertical-align: bottom;

            }
            .concept-message{
                position: relative;
                top: -400px;
                text-align: center;
                color:white
            }
            .key{
                position: relative;
                text-align: center;
                padding:0;
                margin:0;
            }
                .key-list{
                    text-align: center;
                    position: relative;
                    font-size: 40px;
                    font-weight: 2000;
                    color:rgb(3, 3, 3);
                    text-shadow: 1px 1px #FFF;
                    top:-250px;

                }
                .key-back-img{
                    width: 400px;
                    -ms-filter: blur(20px);
                    filter: blur(20px);

                }
            

            img{
                height: 180%;
                object-fit: cover;
            }
            .bx-wrapper{
                border:none!important;
                box-shadow: none!important;
            }
            .slider_box{
                width: 100%;
            }
        .cont-pic-l{
            width:60%;
            float:left;
        }
        .cont-pic-r{
            width:60%;
            float:right;
        }
        .box-l{
            position:relative;
            left:400px;
            top:30px;
            float:left;
            width        : 450px;
            height       : 300px;
            background   :#ffffff;
            border: solid 5px;
        }
        .box-r{
            position:relative;
            right:400px;
            top:30px;
            float:right;
            margin       : auto;
            width        : 450px;
            height       : 300px;
            background   :#ffffff;
            border: solid 5px;
        }
        .box-r span .title {     
            position     : absolute;
            display      : inline-block;
            top          : 50%;
            left         : 50%;
            padding      : 3px;
            color        : #333;
            transform    : translate(-50%,-50%);
            font-size    : 12pt;
            border-radius: 5px;
        }
        .box-l span .title {      
            position     : absolute;
            display      : inline-block;
            top          : 50%;
            left         : 50%;
            padding      : 3px;
            color        : #333;
            transform    : translate(-50%,-50%);
            font-size    : 12pt;
            border-radius: 5px;
        }
        .com{
            font-size:20px;
        }
        .map-img{
                position: relative;
                float:left;
        }

        .access{
            position: relative;
            float:left;
        }
        footer{     
            height: 100px;
            width: 100%;
            float:left;
            background-color:brown;
            margin-top: 10px;
            text-align:center;
        }
       .logoevo{
        font-size: 10px;
        margin:0;
        }
         .logoevo a{
         font-size:10px;
         display: inline;
         margin:0;
         text-decoration:underline;
         }   
       .f_logo{
         height:75px;
         width:75px;
         }
       .logoend{
       display: inline-block;
       text-align: center;
       }
    </style>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>
    
    <script type="text/javascript">
            $(document).ready(function(){
                $('.slide').bxSlider({
                    auto: true,
                    pause: 1500,
                    adaptiveHeight: 'true',
                    mode: 'fade'
                });
            });
    </script>
'''
if(login_success == 1):
    htmlText += '''
    <script type="text/javascript">
        function flexTextarea(el) {
            const dummy = el.querySelector('.FlexTextarea__dummy')
            el.querySelector('.FlexTextarea__textarea').addEventListener('input', e => {
                dummy.textContent = e.target.value + '\u200b'
            })
}

document.querySelectorAll('.FlexTextarea').forEach(flexTextarea)
    </script>
'''
htmlText += '''
  </head>

  <body>
    <div id = "header"></div>
    <header>
        <div class="header1">
            <div class="header1-l">
                <img  src="gava_logo.png" class="logo"></div>
                <div class="header-title"><h1>GAVA HOTEL</h1></div>
            </div>
            <div class="header1-r">
                <ul>
                    <li class="header-24">24時間受け付けております</li>
                    <li class="header-tel">☎042-637-2111</li>
                    
                </ul>

                <ul class="header-buttons">
'''
if(login_success == 1):
    htmlText += '''
    <button onclick="location.href='./reserve.cgi'" type="button" class="header-button">予約</button>
    <button onclick="location.href='./form.cgi'" type="button" class="header-button">予約確認・消去</button>
    '''

else:
    htmlText += '''
    <button onclick="location.href='./login.cgi'" type="button" class="header-button">ログイン</button>
    <button onclick="location.href='./add_user.cgi'" type="button" class="header-button">新規登録</button>
    </ul>
    '''


htmlText += '''
    </div>
        </div>
        <div class="header2">
                <nav class="gnav">
                    <ul class="menu">
                        <li><a href="">GAVA HOTEL</a></li>
                        <li><a href="">お客様へ</a></li>
                        <li><a href="">採用</a></li>
                        <li><a href="">お知らせ</a></li>
                        <li><a href="">お問い合わせ</a></li>
                    </ul>
                </nav>
        </div>
    </header>
    <main>
    '''
if(login_success == 1):
    htmlText += '''
    <h3>%s様 いらっしゃいませ</h3>
    '''%(name)
    
htmlText += '''
        <div class="slide">
            <img class="slipic" src="https://images.unsplash.com/photo-1591828353335-197466da2a4e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
            <img class="slipic" src="https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
            <img class="slipic" src="https://images.unsplash.com/photo-1614064641938-3bbee52942c7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
            <img class="slipic" src="https://cdn.pixabay.com/photo/2017/01/22/17/13/sushi-2000239_960_720.jpg">
        </div>
        <div class="concept">
            <img class="concept-back-img" src="https://images.unsplash.com/photo-1633265486064-086b219458ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
            <div class="concept-message">
                <h1>国内最強のセキュリティ性を誇ります</h1>
                <p></p>
                <h2>お客様のお部屋，個人情報などを世界最高水準のセキュリティでお守りいたします</h2>
            </div>
        </div>
        <!-- <div class="key">
            <img class="key-back-img" src="gava_logo.png">
            <div class="key-list">
                <h1>他にはない</h1>
                <h1>G  A  V  A</h1>
            </div>
        </div> -->
        <div class="four-cont">
            <div cont-1>
                <img class="cont-pic-l" src="https://images.unsplash.com/photo-1461685265823-f8d5d0b08b9b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80">
                <div class="box-r" id="makeImg">
                    <h1>
                    <span class="title">Security<br></span><br>
                    <span class="com">お客様の情報を常に監視し情報の流通を防ぎます<br>もしお忍びで来られるのであれば.....</span>
                    </h1>
                </div>
            </div>
            <div cont-2>   
                <img class="cont-pic-r" src="https://images.unsplash.com/photo-1512552288940-3a300922a275?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2071&q=80">
                <div class="box-l" id="makeImg">
                    <h1>
                    <span class="title">Relaxation<br></span><br>
                    <span class="com">絶景に身を任せ，一時の安らぎを<br></span>
                    </h1>
                </div>
            </div>
            <div cont-3>
                <img class="cont-pic-l" src="https://images.unsplash.com/photo-1504850759690-1c3beb59be7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80">
                <div class="box-r" id="makeImg">
                    <h1>
                    <span class="title">Onsen<br></span><br>
                    <span class="com">天然の温泉はいかがですか？<br>運が良ければ，野生動物との混浴を楽しめます</span>
                    </h1>
                </div>
            </div>
            <div cont-4>
                <img class="cont-pic-r" src="https://images.unsplash.com/photo-1569912629764-4e94377c56f4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80">
                <div class="box-l" id="makeImg">
                    <h1>
                    <span class="title">GOHAN<br></span><br>
                    <span class="com">和・洋・中それぞれ最高の食事を提供致します<br>一人ひとりに合わせた食事を楽しめます</span>
                    </h1>
                </div>
            </div>
        </div>
        <div class="map">
            <iframe class="map-img" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3243.060533347223!2d139.33832701525722!3d35.62623418020717!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60191da6d0a3a261%3A0x337318568a7aaa3b!2z5p2x5Lqs5bel56eR5aSn5a2m!5e0!3m2!1sja!2sjp!4v1657273119434!5m2!1sja!2sjp" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            <h1 class="access">〒 192-0982 東京都八王子市片倉町1404-1<br>横浜線八王子みなみ野駅から徒歩20分<br>横浜線八王子駅からバスで20分</h1>
        </div>
    </main>
        <div class="back"><a href="#header">  Top</a></div>
    <footer>
    <div class = "logoend">
    <img  src="gava_logo.png" class="f_logo">
    <p class = "logoevo">
    ロゴは<a href="https://www.designevo.com/jp/" title="無料オンラインロゴメーカー">DesignEvo</a>ロゴメーカーさんに作られる</p>
    </div>
    </footer>
</body>
</html>
'''



connection.close()

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))

