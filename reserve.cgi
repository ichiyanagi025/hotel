#!/usr/bin/python3
 
import cgi
import MySQLdb#!/usr/bin/python3
 
import cgi
import MySQLdb
import random, string
from http import cookies
import os
 
 
def get_random_str(n):
    char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(char_data) for i in range(n)])
 
form = cgi.FieldStorage()
 
cookie = cookies.SimpleCookie(os.environ.get('HTTP_COOKIE',''))
 
try:
    session_id = cookie["session_id"].value
except KeyError:
    session_id = ""
try:
    mail = cookie["user_id"].value
except KeyError:
    mail = ""
 
rank = form.getfirst('rank', '')
num = form.getfirst('num', '')
check_in = form.getfirst('check_in')
check_out = form.getfirst('check_out')
card_number = form.getfirst('card_number')
card_number_conf = form.getfirst('card_number_conf')
check = form.getfirst('check')
 
 
reserve_success = 0
 
 
if (rank!="選択してください" and check_in is not None and check_out is not None and num!="選択してください" and card_number is not None and card_number_conf is not None ):
    if(card_number == card_number_conf):
        connection = MySQLdb.connect(
            host='localhost',
            user='user1',
            passwd='passwordA1!',
            db='hotel',
            charset='utf8'
            )
 
        cursor = connection.cursor()
        sql = "insert into `Reservation` (`mail`, `number`, `status`, `in`, `out`) values ('" + mail + "', '" + num + "', '" + rank + "', '" + check_in + "', '" + check_out + "');"
        cursor.execute(sql)
        rows = cursor.fetchall()
 
        connection.commit()
        cursor.close()
 
        reserve_success = 1
 
        cursor = connection.cursor()
        sql = "select * from `User` where mail = '" + mail + "';"
        cursor.execute(sql)
        rows = cursor.fetchall()
 
        connection.commit()
        cursor.close()
 
        for row in rows:
            name = row[0]
 
        try:
            cursor = connection.cursor()
            sql = "insert into `Card` (`mail`, `name`, `cardnumber`)values ('" + mail + "', '" + name + "', '" + card_number + "' );"
            cursor.execute(sql)
            rows = cursor.fetchall()
 
            connection.commit()
            cursor.close()
        except MySQLdb._exceptions.IntegrityError:
            pass
 
 
 
    else:
        reserve_success = -2
else:
    reserve_success = -1
 
 
htmlText = '''
<!DOCTYPE html>
<html lang="ja">
 
<head>
    <meta charset="utf-8">
    <title>予約ページ</title>
    <style>
        .contact-form {
            border: 4px solid  #e34646;
            padding: 10px;
            font-size: 15px;
            font-family: sans-serif;
            background-color: #FFF;
        }
 
        .contact-form .item {
            display: block;
            overflow: hidden;
            margin-bottom: 10px;
        }
 
        .contact-form .item.no-label {
            padding: 5px 0px 5px 40px;
        }
 
        .contact-form .item .label {
            float: left;
            padding: 5px;
            margin: 0;
        }
 
        .contact-form .item .radio-group {
            padding: 5px 0px 5px 60px;
        }
 
        .contact-form .item input[type=text],
        .contact-form .item input[type=email],
        .contact-form .item textarea {
            display: block;
            margin-left: 60px;
            width: 100px;
            padding: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
            font-size: 13px;
        }
 
        .contact-form .item ::placeholder {
            color: #ccc;
        }
 
        .contact-form .item textarea {
            outline: none;
            border: 1px solid #ccc;
            resize: vertical;
 
        }
 
        body {
            background-image: url(https://asp.hotel-story.ne.jp/media/6791000100017.jpg);
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center;
            height: 100%;
            width: auto;
           
 
        }
 
        .btn-square {
            display: inline-block;
            padding: 0.5em 15em;
            text-decoration: none;
            background: #e34646;
            /*ボタン色*/
            color: #FFF;
            border: #7CFC00;
            border-bottom: solid 4px #8d0505;
            border-radius: 3px;
            cursor: pointer;
            text-align: center;
        }
 
        .btn-square-reset {
            display: inline-block;
            padding: 0.5em 14em;
            text-decoration: none;
            background: #bab6ac;
            /*ボタン色*/
            color: #FFF;
            border: #7CFC00;
            border-bottom: solid 4px #9c9a99;
            border-radius: 3px;
            cursor: pointer;
            text-align: center;
        }
 
        .btn-square:active {
            background: #8d0505;
        }
 
        .btn-square-reset:active {
            background: #9c9a99;
        }
 
        .text_center {
            margin: 0 auto;
            width: 40%;
        }
 
        h1 {
            border-bottom: double 5px #e34646;
        }
        p.error_sentence{
            color: red;
        }
    </style>
</head>
 
<body>
    <div class="text_center">
        <form class="contact-form" formaction="" method="post">
            <h1 style="text-align:center"><font size="7" face="Sylfaen">Reserve</font></h1>
            <p>お客様の情報をご記載下さい。</p>
        <p>
            ランク<select name="rank" id="rank">
            <option value="選択してください">選択してください</option>
            <option value="ロイヤルスイート">ロイヤルスイート</option>
            <option value="スイート">スイート</option>
            <option value="エグゼクティブ">エグゼクティブ</option>
            <option value="スタンダード">スタンダード</option>
            <option value="エコノミー">エコノミー</option>
            </select>
        </p>
        <p>
        <p>
            人数<select name="num" id="num">
                <option value="選択してください">選択してください</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
            </select>
        </p>
        <p>
            <label for="user_name">チェックイン日</label>
 
            <input id="check_in" name="check_in" type="date" min="<?php echo
date('Y-m-d');?>" />
        </p>
        <p>
            <label for="user_name">チェックアウト日</label>
            <input id="check_out" name="check_out" type="date" min="<?php echo
date('Y-m-d');?>" />
        </p>
        <p>
            <label for="">カード番号</label>
            <input id="card_number" name="card_number" type="text" size="16" />
        </p>
        <p>
            <label for="">カード番号再入力</label>
            <input id="card_number_conf" name="card_number_conf" type="test" size="16" />
        </p>
        <p>
            <label for="">月/年</label>
            <input id="card_m" name="card_m" type="test" size="2" />/<input id="card_y" name="card_y" type="test"
                size="2" />
        </p>
        <p>
            <label for="">セキュリティコード</label>
            <input id="security_code" name="security_code" type="test" size="5" />
        </p>
        <p>
            <label for="user_name">カードの情報を保存してよろしいですか</label>
            <input id="check" name="check" type="checkbox" />
        </p>
        <div style="text-align:center"><input type="submit" class="btn-square" value="予約"></div>
        <div style="text-align:center"><input type="reset" class="btn-square-reset" value="リセット"></div>
'''
 
print("Content-Type: text/html")
 
if(reserve_success == 1):
 
    print("Set-Cookie: session_id=" + session_id)
    print("Set-Cookie: user_id=" + mail)
 
    htmlText += '''
    <p>ヽ（　＾ω＾）ﾉｻｸｾｽ！ 5秒後にホームページに戻るよ</p>
    </form>
    <script>
        setTimeout(function(){
        window.location.href = './homepage.cgi';
        }, 5*1000);
    </script>
    </body>
    </html>
    '''
 
elif(reserve_success == -1):
    htmlText += '''
    <p class="error_sentence">※未記入の項目があります</p>
    </form>
    </body>
    </html>
    '''
 
elif(reserve_success == -2):
    htmlText += '''
    <p class="error_sentence">※カード番号が一致していません</p>
    </form>
    </body>
    </html>
    '''
 
 
elif(reserve_success == 0):
    htmlText += '''
    </form>
    </body>
    </html>
    '''
 
print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
 
