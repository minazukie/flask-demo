#coding:utf-8
import pymysql
#SQL方法
def all_blog():
    s =u"SELECT * FROM blog ORDER BY b_id"
    return s
def searchById(searchid):
    s="SELECT * FROM blog WHERE b_id= "+str(searchid)+" ORDER BY b_id"
    return s
def paginate(page):
    p=(page-1)*5
    s="SELECT * FROM blog ORDER BY b_id DESC limit "+str(p)+",5 "
    return s
def editblog(id,text):
    s="UPDATE blog SET text = '"+text+"' WHERE b_id="+str(id)
    return s
def tagcount(tag):
    s="SELECT COUNT(*) AS tagcount FROM blog WHERE b_tag='"+tag+"'"
    return s
def newblog(title,tag,pre,text):
    s="INSERT INTO blog(b_title,b_tag,b_pre,b_text) VALUES ('"+title+"','"+tag+"','"+pre+"','"+text+"')"
    return s
def newcomm(name,email,text,b_id):
    s="INSERT INTO comment(c_name,c_text,c_email,b_id) VALUES ('"+name+"','"+email+"','"+text+"','"+b_id+"')"
    return s
def verifylogin(username,password):
    s="SELECT u_id  FROM user WHERE u_user='"+username+"' AND u_pwd='"+password+"'"
    return s
def getcomm(b_id):
    s="SELECT comment.b_id,c_id,c_text,c_name,c_date  FROM comment JOIN blog ON comment.b_id = blog.b_id WHERE comment.b_id="+b_id+" ORDER BY c_date DESC"
    return s
def countcategory():
    s="SELECT b_tag,count(*) AS count FROM blog GROUP BY b_tag ORDER BY b_id  "
    return s
def getcategory(tag):
    s="SELECT *  FROM blog  WHERE b_tag='"+tag+"'"
    return s
#数据库连接函数
def sql_dict(sql):
    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='sandwinds',charset='utf8')
    cur = connection.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    r=cur.fetchall()
    cur.close()
    connection.close()
    return r
def sql(sql):
    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='sandwinds',charset='utf8')
    cur = connection.cursor()
    cur.execute(sql)
    connection.commit()
    cur.close()
    connection.close()
    return "done"