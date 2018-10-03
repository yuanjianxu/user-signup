from flask import Flask,render_template,request,redirect,session,url_for
app=Flask(__name__)
app.debug='True'

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        username=request.form.get('username')
        password=request.form.get('pwd')
        vpassword=request.form.get('vpwd')
        email=request.form.get('email')
        if username=='' or password=='' or vpassword=='':
            return render_template('signup.html',all_error="username, password, verify password can't empty, please signup again")
        elif len(username)<=3 or len(username)>=20 or ' ' in username or len(password)<=3 or len(password)>=20 or ' ' in password:
            return render_template('signup.html',username_error="The user's username or password is not valid, the length has to between 3 and 20")
        elif password!=vpassword:
            return render_template('signup.html',vpassword_error="The user's password and password-confirmation do not match.")
        elif email!='' :
            if len(username)<=3 or len(username)>=20:
                return render_template('signup.html',email_error="The user's email is not valid")
            elif ('@' and '.') not in email:
                return render_template('signup.html',email_error="The user's email is not valid")
            elif ' ' in email:
                return render_template('signup.html',email_error="The user's email is not valid")
        elif username!='lana' or password!='lana' or vpassword!='lana':
            return render_template('signup.html',all_error="username and password not match")
        else:
            return render_template('index.html')   



if __name__=='__main__':
    app.run()