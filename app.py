from flask import Flask,render_template,request,url_for,session,redirect
import sqlite3 as sql
app=Flask(__name__)

app.secret_key="pass"



@app.route('/')
def home():
    
    return render_template("sample.html")

@app.route('/play')
def play():
    return render_template("play.html")



@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        mobile=request.form.get("mobile")
        password=request.form.get("password")
        conn=sql.connect("shopping.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("select * from login where name=?",(name,))
        data=cur.fetchone()
        if data:
            if str(data["name"])==name and str(data["mobile"])==mobile and str(data["password"])==password:
                session["username"]=name
                # return "Login as"+session["username"]
                return redirect(url_for('home'))
    return render_template("login.html")
    


@app.route('/logout')
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))


@app.route('/signin',methods=["POST","GET"])
def signin():
    if request.method=="POST":
        first_name=request.form.get("first_name")
        last_name=request.form.get("last_name")
        password=request.form.get("password")
        conn=sql.connect("shopping.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("insert into sign_in (first_name,last_name,password) values(?,?,?)",
                    (first_name,last_name,password))
        conn.commit()
        return redirect(url_for("home"))
    return render_template("sign.html")




@app.route('/first',methods=["POST","GET"])
def first():
    if request.method=="POST":
        post=request.json
        conn=sql.connect("shopping.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("insert into seller_details (product_name,quantity,price,Images) values(?,?,?,?)",
                    (post.get("product_name"),post.get("quantity"),post.get("price"),post.get("Images")))
        conn.commit()
        return ""
    conn=sql.connect("shopping.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from seller_details")
    data=cur.fetchall()
    return render_template("capital.html",datas=data)


# @app.route('/first')
# def first():
#     conn=sql.connect("shopping.db")
#     conn.row_factory=sql.Row
#     cur=conn.cursor()
#     cur.execute("select * from shop")
#     data=cur.fetchall()
#     return render_template("capital.html",datas=data)


if __name__=="__main__":
    app.run(debug=True,port=5000)