from flask import Flask, redirect, session,render_template,request
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
app.secret_key='mynameamkumarA'

# facebook data ----
FB_APP_SECRET=os.getenv('FB_APP_SECRET')
FB_APP_ID=os.getenv('FB_APP_ID')
redirectUri = "https://fb-login-python.onrender.com/facebook/callback"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/facebook/login')
def facebook_login():
        print("5444") 
        redirectUri = "https://fb-login-python.onrender.com/facebook/callback"
        url = redirect(f"https://www.facebook.com/v22.0/dialog/oauth?client_id={FB_APP_ID}&redirect_uri={redirectUri}&scope=email")
        print("url", url)
        return url

@app.route('/facebook/callback')
def facebook_callback():
      print("544444444444444444444444444444444444444444444444")
      code= request.args.get('code')
      print("aaa",code)
      if code:
           user_response = requests.get(
                  f"https://www.facebook.com/v22.0/oauth/access_token?client_id={FB_APP_ID}&redirect_uri={redirectUri}&client_scret={FB_APP_SECRET}&code={code}"
            )
           print("456465",user_response)
           data = user_response.json()

           if 'access_token' in data:
                 session['access_token']=data['access_token']

                 user_response= requests.get(
                       f"https://graph.facebook.com/v22.0/me?fields=id,name,email&access_token={data['access_token']}"
                 )
                 print("user response",user_response)
                 return redirect('/')
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)  