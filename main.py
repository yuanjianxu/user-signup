from flask import Flask,render_template,request,redirect,session,url_for
app=Flask(__name__)
app.debug='True'

@app.route('/',methods=['POST','GET'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        username=request.form.get('username')
        password=request.form.get('pwd')
        vpassword=request.form.get('vpwd')
        email=request.form.get('email')
        if username=='' or len(username)<=3 or len(username)>=20 or ' ' in username  :
            return render_template('signup.html',e=email,n=username,username_error="username is not valid, the length has to between 3 and 20")
        elif password=='' or len(password)<=3 or len(password)>=20 or ' ' in password:
            return render_template('signup.html',n=username,e=email,password_error="password is not valid, the length has to between 3 and 20")
        elif vpassword=='' or len(vpassword)<=3 or len(vpassword)>=20 or ' ' in vpassword:
            return render_template('signup.html',n=username,e=email,vpassword_error="Verify password is not valid, the length has to between 3 and 20")
        elif password!=vpassword:
            return render_template('signup.html',n=username,e=email,vpassword_error="The user's password and password-confirmation do not match.")
        elif email!='' :
            if len(username)<=3 or len(username)>=20 or ' ' in email or ('@' and '.') not in email:
                return render_template('signup.html',n=username,e=email,email_error="The user's email is not valid")
        elif username!='lana' or password!='lana' or vpassword!='lana':
            return render_template('signup.html',n=username,e=email,username_error="username and password not match")
        else:
            return render_template('index.html',name=username)   

if __name__=='__main__':
    app.run()