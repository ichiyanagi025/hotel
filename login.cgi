#!/usr/bin/python3

import cgi
import MySQLdb
import random, string


def get_random_str(n):
	char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
	return ''.join([random.choice(char_data) for i in range(n)])

form = cgi.FieldStorage()

mail = form.getfirst('mail')
password = form.getfirst('password')

login_success = 0


if (mail is not None and password and not None ):
    connection = MySQLdb.connect(
        host='localhost',
        user='user1',
        passwd='passwordA1!',
        db='hotel',
        charset='utf8'
        )

    cursor = connection.cursor()

    sql = "select * from `User`;"
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    for row in rows:
        if(row[2] == mail and row[4] == password):
            login_success = 1
    
    if(login_success == 0):
        login_success = -1



htmlText = '''

<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ユーザー登録</title>
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
    .login{
        box-sizing: form;
        height: 30px;
        width: 90%;
        background-color: #40c264;
        font-size: 18px;
    }
    .create{
        height: 30px;
        width: auto;
        background-color: blue;
        font-size: 14px;
    }
    div.or{
        display: flex;
        align-items: center; 
        justify-content: center; 
    }
    .or:before, .or:after {
        border-top: 1px solid;
        content: "";
        width: 40%;
    }
    a.forget{
        margin:10px;
    }
    -->
  </style>
<body>
    <h1><a href="homepage.html"><img src="gava_logo.png" alt="ガバホテル"></a></h1>
    <form action="" method="post">
        <h2>ログイン</h2>
        <p>
            <label for="">メールアアドレス</label><br>
            <input id="mail" name="mail" type="text" size="40"/>
        </p>
        <p>
            <label for="">パスワード</label><br>
            <input id="password" name="password" type="password" size="40" />
        </p>
        <button class="login" type="submit">ログイン</button>
        <p class="forget"><a href="homepage.html">パスワードを忘れた方はこちら</a></p>
        <div class="or">または</div>
        <button class="create" type="button" onclick="add_user.cgi">新しいアカウントを作成</button>
'''
print("Content-Type: text/html")

if(login_success == 1):
    session_id = session_id = get_random_str(64)

    cursor = connection.cursor()

    sql = "insert into `Session`(`user_id`,`mail`,`session_id`)values (null, '" + mail + "', '" + session_id + "');"
    cursor.execute(sql)

    connection.commit()
    cursor.close()


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

elif(login_success == -1):
    htmlText += '''
    <p>ログインに失敗ました。</p>
    </form>
    </body>
    </html>
    '''


else:
    htmlText += '''
    </form>
    </body>
    </html>
    '''


print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))