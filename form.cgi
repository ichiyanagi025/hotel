#!/usr/bin/python3
 
import cgi
import MySQLdb
import MySQLdb
from http import cookies
import os
 
form = cgi.FieldStorage()
mail = form.getfirst('mail')
password = form.getfirst('password')
mail2 = form.getfirst('mail2')
rank = form.getfirst("rank")
 
login_success = 0 #メールとパスワードが存在するか
flag = 0#データベースの中身があるか
 
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
try:
    session_id = cookie["session_id"].value
except KeyError:
    session_id = ""
try:
    mail_c = cookie["user_id"].value
except KeyError:
    mail_c = ""
 
 
if (mail is not None and password and not None ):
    login_success = 1
    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='hotel',
        charset='utf8'
        )
 
    cursor = connection.cursor()
 
    sql = "select * from `Reservation` where mail = '" + mail + "'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
 
if (mail2 is not None):#取り消すが押されたとき
    login_success = 2
    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='hotel',
        charset='utf8'
        )
    cursor = connection.cursor()
 
    sql = "delete from Reservation where mail = '" + mail2 + "' and status = '" + rank +"';"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
 
 
print("Set-Cookie: session_id=" + session_id)
print("Set-Cookie: user_id=" + mail_c)
 
#初期ページ
htmlText = '''
 
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>予約取り消し</title>
<style type="text/css">
    <!--
    body{
        background-image: url("https://images.unsplash.com/photo-1594099462046-1df31fd4a66c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDl8fGhvdGVsc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60");
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-color: #464646;
        height: 100%;
        width: auto;
        }
    img{
        text-align: left;
        width: 125px;
        height: 125px;
    }
    form {
        height: auto;
        width: 375px;
        padding: 10px 10px;
        position: absolute;
        top: auto;
        left: 50%;
        transform: translate(-50%,-50%);
        background-color: white;
        text-align: center;
        border-radius:10px;
        top: 300px;
    }
    p{
        color: black;
    }
    h2 {
        color: black;
    }
    input{
        box-sizing: form;
        width: 85%;;
    }
    button{
        outline: none;
        border: none;
        border-radius:5px;
        color: aliceblue;
        font-weight: 600;
    }
    .next{
        box-sizing: form;
        height: 30px;
        width: 90%;
        background-color: #40c264;
        font-size: 18px;
    }
    .back{
        height: 30px;
        width: 90%;
        background-color: blue;
        font-size: 18px;
    }
 
  </style>
<body>
    <h1><a href="homepage.cgi"><img src="gava_logo.png" alt="ガバホテル"></a></h1>
    <form action="" method="post">
        <h2>予約取り消し</h2>
        <p>
            <label for="">メールアアドレス</label><br>
            <input id="mail" name="mail" type="text" size="40"/>
        </p>
        <p>
            <label for="">パスワード</label><br>
            <input id="password" name="password" type="password" size="40" />
        </p>
        <button class="next" type="submit">次へ</button>
        <p>      </p>
        <button class="back" type="button" onclick="location.href='homepage.cgi'">戻る</button>
'''
 
#メールとパスワード入力後
if(login_success==1):
    htmlText2 = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>予約取り消し</title>
<style type="text/css">
    <!--
    body{
        background-image: url("https://images.unsplash.com/photo-1594099462046-1df31fd4a66c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDl8fGhvdGVsc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60");
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-color: #464646;
        height: 100%;
        width: auto;
        }
    img{
        text-align: left;
        width: 125px;
        height: 125px;
    }
    form {
        height: auto;
        width: 375px;
        padding: 10px 10px;
        position: absolute;
        top: auto;
        left: 50%;
        transform: translate(-50%,-50%);
        background-color: white;
        text-align: center;
        border-radius:10px;
        top: 300px;
    }
    p{
        color: black;
    }
    h2 {
        color: black;
    }
    input{
        box-sizing: form;
        width: 85%;;
    }
    button{
        outline: none;
        border: none;
        border-radius:5px;
        color: aliceblue;
        font-weight: 600;
    }
    .next{
        box-sizing: form;
        height: 30px;
        width: 90%;
        background-color: #40c264;
        font-size: 18px;
    }
    .back{
        height: 30px;
        width: 90%;
        background-color: blue;
        font-size: 18px;
    }
 
  </style>
<body>
    <h1><a href="homepage.cgi"><img src="gava_logo.png" alt="ガバホテル"></a></h1>
    <form action="" method="post">
        <h2>予約取り消し</h2>
    '''
    if(rows is not None):#データベースの中身がある場合
        for row in (reversed(rows)):
            flag = 1;
            htmlText2 += '''
             <p>
                以下の内容を取り消します よろしいですか
             </p>
            <div class="reserve">
                <p>お部屋のランク:%s</p><p>人数:%s</p>チェックイン日:%s</p>チェックアウト日:%s</p>
                <input type ="hidden" name = "mail2" value = %s>
                <input type ="hidden" name = "rank" value = %s>
                <input type ="hidden" name = "nubmer" value = %s>
                <button class="next" type="submit">取り消す</button>
            '''%(row[2], row[1], row[3], row[4],row[0],row[2],row[1])
    if(flag == 0):#データベースの中身がない場合
        htmlText2 +='''
        <h3>見つかりませんでした</h3>
         '''
 
    htmlText2 += '''
        <p>      </p>
        <button class="back" type="button" onclick="location.href='homepage.cgi'">戻る</button>
    '''
 
if(login_success==2):
    htmlText3 = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>予約取り消し</title>
<style type="text/css">
    <!--
    body{
        background-image: url("https://images.unsplash.com/photo-1594099462046-1df31fd4a66c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDl8fGhvdGVsc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60");
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-color: #464646;
        height: 100%;
        width: auto;
        }
    img{
        text-align: left;
        width: 125px;
        height: 125px;
    }
    form {
        height: auto;
        width: 375px;
        padding: 10px 10px;
        position: absolute;
        top: auto;
        left: 50%;
        transform: translate(-50%,-50%);
        background-color: white;
        text-align: center;
        border-radius:10px;
        top: 300px;
    }
    p{
        color: black;
    }
    h2 {
        color: black;
    }
    input{
        box-sizing: form;
        width: 85%;;
    }
    button{
        outline: none;
        border: none;
        border-radius:5px;
        color: aliceblue;
        font-weight: 600;
    }
    .next{
        box-sizing: form;
        height: 30px;
        width: 90%;
        background-color: #40c264;
        font-size: 18px;
    }
    .back{
        height: 30px;
        width: 90%;
        background-color: blue;
        font-size: 18px;
    }
 
  </style>
<body>
    <h1><a href="homepage.cgi"><img src="gava_logo.png" alt="ガバホテル"></a></h1>
    <form action="" method="post">
        <h2>予約取り消し</h2>
        <h3>取り消しました</h3>
        <p>      </p>
    '''
    htmlText3 +='''
        <button class="back" type="button" onclick="location.href='homepage.cgi'">戻る</button>
    '''
 
if(login_success == 0):
    print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
elif(login_success == 1):
    print(htmlText2.encode("utf-8", 'ignore').decode('utf-8'))
elif(login_success == 2):
    print(htmlText3.encode("utf-8", 'ignore').decode('utf-8'))