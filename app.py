from flask import*
import pymysql

# app name
app = Flask (__name__)

@app.route("/")
def homepage():
    # establish a connection to DB 
    connection = pymysql.connect(host='localhost', user='root', password='',database='Nafuu')

    # query to get all phones
    sql ="SELECT * FROM products WHERE product_category= 'phone'"

    # execute the above query 
    # Cursor - is used to execute the above SQL
    cursor = connection.cursor()

    # execute query
    cursor.execute(sql)

    # fetch all the rows
    phone= cursor.fetchall()

    # query to get beauty product
    sql1 = "SELECT * FROM products WHERE product_category = 'beauty' "
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    beauty = cursor1.fetchall()

    # get electronics
    sql2 = "SELECT * FROM products WHERE product_category = 'electronics' "
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    electronic = cursor2.fetchall()

 # query to get beauty product
    sql1 = "SELECT * FROM products WHERE product_category = 'beauty' "
    cursor1 = connection.cursor()
    cursor1.execute(sql1)
    beauty = cursor1.fetchall()

    # get electronics
    sql2 = "SELECT * FROM products WHERE product_category = 'electronics' "
    cursor2 = connection.cursor()
    cursor2.execute(sql2)
    electronic = cursor2.fetchall()
    # return the html template
    return render_template("index.html", phone=phone, beauty=beauty, electronic=electronic)
   
#    route for a single item 
@app.route("/single/<product_id>")
def singleitem(product_id):
    # connection to DB 
    connection = pymysql.connect(host='localhost', user='root', password='',database='Nafuu')

    # create sql query 
    sql="SELECT * FROM products WHERE product_id = %s;"
    # create a cursor 
    cursor= connection.cursor()

    # execute 
    cursor.execute(sql, product_id)

    # get the single product 
    product = cursor.fetchone()

    return render_template("single.html", product = product)

# upload products
@app.route("/upload", methods =['POST', 'GET'])
def Upload():
    if request.method == 'POST':
        # user can add products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # connect to db 
        connection = pymysql.connect(host='localhost', user='root', password='', database='Nafuu')

        # create a cursor 
        cursor = connection.cursor()

        sql = "insert into products (product_name, product_desc, product_cost, product_category, product_image_name) values (%s, %s, %s, %s, %s)"

        data = (product_name, product_desc, product_cost, product_category, product_image_name.filename)

        # execute 
        cursor.execute(sql, data)

        # save changes 
        connection.commit()

        return render_template('uploadfashion.html', message = "product added succesfully")   
    else:
        return render_template('uploadfashion.html', error = "please add a product")  
    
# fashion route 
# helps you to see all the fashions 
@app.route("/fashion")
def Fashion():
    connection = pymysql.connect(host='localhost', user='root', password='',database='Nafuu')

    # query to get all fashion
    sql = "SELECT * FROM products WHERE product_category = 'dresses' "
    sql1 = "SELECT * FROM products WHERE product_category = 'handbags' "
    sql2 = "SELECT * FROM products WHERE product_category = 'caps' "
    sql3 = "SELECT * FROM products WHERE product_category = 'socks' "
    sql4 = "SELECT * FROM products WHERE product_category = 'belts' "
   
    # execute the above query 
    # Cursor - is used to execute the above SQL
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    
    # execute query
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    cursor4.execute(sql4)

    # execute 
    
    # fetch all the rows
    dresses= cursor.fetchall()
    hanbags= cursor1.fetchall()
    caps= cursor2.fetchall()
    socks= cursor3.fetchall()
    belts= cursor4.fetchall()
    

   

    return render_template("fashion.html")

# a route to upload fashion 

@app.route("/uploadfashion", methods =['POST', 'GET'])
def UploadFashion():
    if request.method == 'POST':
        # user can add products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # connect to db 
        connection = pymysql.connect(host='localhost', user='root', password='', database='Nafuu')

        # create a cursor 
        cursor = connection.cursor()

        sql = "insert into products (product_name, product_desc, product_cost, product_category, product_image_name) values (%s, %s, %s, %s, %s)"

        data = (product_name, product_desc, product_cost, product_category, product_image_name.filename)

        # execute 
        cursor.execute(sql, data)

        # save changes 
        connection.commit()

        return render_template('upload.html', message = "fashion added succesfully")   
    else:
        return render_template('upload.html', error = "please add a fashion")  

@app.route("/services")
def services():
    return "This is services page"

@app.route("/login")
def login():
    return "This is login page"

@app.route("/logout")
def logout():
    return "This is logout page"


# app main entry
if __name__ == '__main__':
    app.run(debug=True, port=4000)
