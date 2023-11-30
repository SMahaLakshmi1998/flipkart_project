from flask import Flask,render_template,jsonify,request
import requests,json

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        product_name=request.form.get("product_name")
        quantity=request.form.get("quantity")
        price=request.form.get("price")
        Images=request.form.get("Images")
        
        dict1={}
        dict1.update({"product_name":product_name})
        dict1.update({"quantity":quantity})
        dict1.update({"price":price})
        dict1.update({"Images":Images})
        url="http://127.0.0.1:5000/first"
        response=requests.post(url,json=dict1)
        return{'data':'response'}
    return render_template("pur.html")


if __name__=="__main__":
    app.run(debug=True,port=5001)

#     {
# "product_name":"hometemple",
# "quantity":5,
# "price":"2500",
# "Image":"/static/images/hometemple.webp"}