#!/usr/bin/python3
 
import cgi
import MySQLdb
import random, string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
def get_random_str(n):
    char_data = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return ''.join([random.choice(char_data) for i in range(n)])
 
form = cgi.FieldStorage()
 
family_name = form.getfirst('family_name')
family_name_kana = form.getfirst('family_name_kana')
first_name = form.getfirst('first_name')
first_name_kana = form.getfirst('first_name_kana')
mail = form.getfirst('mail')
mail_conf = form.getfirst('mail_conf')
tel = form.getfirst('phone_number')
password = form.getfirst('password')
password_conf = form.getfirst('password_conf')
 
if(family_name is not None and first_name is not None):
    name = family_name + first_name
   
if(family_name_kana is not None and first_name_kana is not None):
    furigana = family_name_kana + first_name_kana
 
success_adduser = 0
 
 
if (family_name is not None or family_name_kana is not None or
first_name is not None or first_name_kana is not None or
mail is not None or mail_conf is not None or
password is not None or password_conf is not None or
tel is not None):
    if (family_name is not None and family_name_kana is not None and
first_name is not None and first_name_kana is not None and
mail is not None and mail_conf is not None and
password is not None and password_conf is not None and
tel is not None):
        if(mail == mail_conf and password == password_conf):
            try:
                connection = MySQLdb.connect(
                    host='localhost',
                    user='user1',
                    passwd='passwordA1!',
                    db='hotel',
                    charset='utf8'
                    )

                cursor = connection.cursor()

                sql = "insert into `User` (`name`, `furigana`, `mail`, `tell`, `password`) values ('" + name + "', '" + furigana + "', '" + mail + "', '" + tel + "', '" + password + "' );"
                cursor.execute(sql)
                rows = cursor.fetchall()

                connection.commit()
                cursor.close()

                success_adduser = 1

            except MySQLdb._exceptions.IntegrityError:
                success_adduser = -1
            
            me = "c0a20017b3@edu.teu.ac.jp"  # ?????????
            you = mail # ?????????
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "???????????????????????????????????????"
            msg['From'] = me
            msg['To'] = you
            
            text = "??????????????????????????????????????????\n"+ name +"?????????????????????????????????"
            html = """
            <html>
            <head></head>
            <body>
                <p style='font-size:16.0pt;font-family:???????????????'>???????????????????????????????????????</p>
                <p>%s?????????????????????????????????</p>
            </body>
            </html>
            """%(name)
            
            
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')
            
            msg.attach(part1)
            msg.attach(part2)
            try:
                s = smtplib.SMTP('localhost')
                s.sendmail(me, you, msg.as_string())
                s.quit()
            except:
                pass

        else:
            if(mail != mail_conf):
                success_adduser = -3
            elif(password != password_conf):
                success_adduser = -4
    else:
        success_adduser = -2
 
 
 
 
htmlText = '''
 
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>??????????????????</title>
1
2
<script type="text/javascript" src="https://code.jquery.com/jquery-3.4.1.min.js?ver=3.4.1"></script>
<script type="text/javascript" src="jquery.autoKana.js">
    $(function() {
        $.fn.autoKana('name', 'kana', {katakana:true});
    });	
</script>
<style type="text/css">
    <!--
    body{
        background-image: url("https://images.unsplash.com/photo-1594099462046-1df31fd4a66c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDl8fGhvdGVsc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=600&q=60");
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        background-color: #464646;
        max-width: 100%;
        height: auto;
        }
    img{
        text-align: left;
        width: 125px;
        height: 125px;
    }
    form {
        height:auto;
        width: 375px;
        padding: 40px 10px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        background-color: white;
        text-align: center;
        border-radius:10px;
        position: relative;
        top: 300px;
    }
    p{
        color: black;
    }
    h2 { color: black }
    input#sei{
        box-sizing: form;
        width: 40%;
    }
    #seikana{
        box-sizing: form;
        width: 40%;
    }
    #mei{
        box-sizing: form;
        width: 40%;
    }
    #meikana{
        box-sizing: form;
        width: 40%;
    }
    button{
        box-sizing: form;
        height: 30px;
        width: 90%;
        outline: none;
        border: none;
        border-radius:10px;
        background-color: #40c264;
        color: white;
        font-size: 18px;
        font-weight: 600;
    }
    -->
  </style>
<body>
    <h1><a href="homepage.html"><img src="gava_logo.png" alt="???????????????"></a></h1>
    <form action="" method="post">
        <h2>????????????</h2>
        <p>
            <input id="sei" name="family_name" type="text" size="40" placeholder="???" />
            <input id="seikana" name="family_name_kana" type="text" size="40" placeholder="??????" />
        </p>
        <p>
            <input id="mei" name="first_name" type="text" size="40" placeholder="???" />
            <input id="meikana" name="first_name_kana" type="text" size="40" placeholder="??????" />
        </p>        
        <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
        <script src="jquery.autoKana.js"></script>
        <script>
        $(function() {
            $.fn.autoKana('#sei', '#seikana');
            $.fn.autoKana('#mei', '#meikana');
        });
        </script>
            <label for="">????????????</label><br>
            <input id="phone_number" name="phone_number" type="text" size="40" />
        </p>
        <p>
            <label for="">????????????????????????</label><br>
            <input id="mail" name="mail" type="text" size="40"/>
        </p>
        <p>
            <label for="">??????????????????????????????</label><br>
            <input id="mail_conf" name="mail_conf" type="test" size="40"/>
        </p>
        <p>
            <label for="">???????????????</label><br>
            <input id="password" name="password" type="password" size="40" />
        </p>
        <p>
            <label for="">????????????????????????</label><br>
            <input id="password_conf" name="password_conf" type="password" size="40" />
        </p>
        <button id="login" type="submit">????????????</button>
        <p class="forget"><a href="login.cgi">?????????????????????????????????????????????</a></p>
    '''

if(success_adduser == 1):
    session_id = session_id = get_random_str(64)
 
    cursor = connection.cursor()
 
    sql = "insert into `Session`(`mail`,`session_id`)values ( '" + mail + "', '" + session_id + "');"
    cursor.execute(sql)
 
    connection.commit()
    cursor.close()
 
 
    print("Set-Cookie: session_id=" + session_id)
    print("Set-Cookie: user_id=" + mail)
 
    htmlText += '''
    <p>?????????????????????????????????????? 5???????????????????????????????????????</p>
    </form>
    <script>
        setTimeout(function(){
        window.location.href = './homepage.cgi';
        }, 5*1000);
    </script>
    </body>
    </html>
    '''
 
elif(success_adduser == -1):
    htmlText += '''
    <p>???????????????????????????????????????????????????????????????????????????</p>
    </form>
    </body>
    </html>
    '''
 
elif(success_adduser == -2):
    htmlText += '''
    <p>??????????????????????????????????????????</p>
    </form>
    </body>
    </html>
    '''
 
elif(success_adduser == -3):
    htmlText += '''
    <p>????????????????????????????????????????????????</p>
    </form>
    </body>
    </html>
    '''
 
elif(success_adduser == -4):
    htmlText += '''
    <p>??????????????????????????????????????????</p>
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


