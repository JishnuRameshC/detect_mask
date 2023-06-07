import random

from flask import Flask,render_template,request,redirect,session
from DBConnection import Db
app = Flask(__name__)
app.secret_key="abc"

@app.route('/logout')
def logout():
    session['lin']=''
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/log')
def hello_world():
    return render_template('login.html')

@app.route('/login',methods=['post'])
def login1():
    database = Db()
    uname=request.form['textfield']
    passw=request.form['textfield2']
    query="select * from login where username='"+uname+"' and password='"+passw+"'"
    result=database.selectOne(query)
    if result is not None:
        if result['type']=="admin":
            session['lin']='lo'
            return redirect('/adminhome')
        elif result['type']=="tp":
            session['lin'] = 'lo'
            session['lid']=result['loginid']
            return redirect('/thome')
        elif result['type'] == "user":
            session['lin'] = 'lo'
            session['lid'] = result['loginid']
            return redirect('/uhome')
        else:
            return '''<script>alert("invalid user");</script>'''
    else:
        return '''<script>alert("invalid user");</script>'''


@app.route('/adminhome')
def adminh():
    if session['lin']=='lo':
        return render_template('admin/admin home.html')
    else:
        return redirect('/log')

@app.route('/t')
def traffic():
    if session['lin'] == 'lo':
        return render_template('admin/traffic police.html')
    else:
        return redirect('/log')

@app.route('/g',methods=['post'])
def trafic():
    if session['lin'] == 'lo':
        database =Db()
        name=request.form['textfield']
        phone=request.form['textfield2']
        email=request.form['textfield3']
        gender=request.form['radio']
        qualification=request.form['textarea']
        password=random.randint(0000,9999)
        query = "insert into login VALUES ('','"+email+"','"+str(password)+"','traffic police')"
        res=database.insert(query)
        query2="insert into trafficpolice VALUES ('"+str(res)+"','"+name+"','"+phone+"','"+email+"','"+gender+"','"+qualification+"')"
        database.insert(query2)
        return  '''<script>alert("user added succesfully");window.location='/manag'</script>'''
    else:
        return redirect('/log')

@app.route('/manag')
def managee():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from trafficpolice "
        res=database.select(query)
        return render_template('admin/manage police.html',data=res)
    else:
        return redirect('/log')

@app.route('/dlt/<b>')
def delt(b):
    if session['lin'] == 'lo':
        database=Db()
        query="delete  from trafficpolice where trafficid ='"+b+"'"
        database.delete(query)
        query2="delete  from login where loginid ='"+b+"'"
        database.delete(query2)
        return '''<script>alert("deleted  succesfully");window.location='/manag'</script>'''
    else:
        return redirect('/log')

@app.route('/edi/<e>')
def editt(e):
    if session['lin'] == 'lo':
        database=Db()
        query="select * from trafficpolice where trafficid='"+e+"'"
        res=database.selectOne(query)
        return render_template('admin/edit traffic.html',data=res)
    else:
        return redirect('/log')

@app.route('/updte/<u>',methods=['post'])
def update(u):
    if session['lin'] == 'lo':
        database=Db()
        name = request.form['textfield']
        phone = request.form['textfield2']
        email = request.form['textfield3']
        gender = request.form['radio']
        qualification = request.form['textarea']
        query="update trafficpolice set name='"+name+"',phone='"+phone+"',email='"+email+"',gender='"+gender+"',qualification='"+qualification+"' where trafficid='"+u+"'"
        database.update(query)
        return '''<script>alert("edited  succesfully");window.location="/manag"</script>'''
    else:
        return redirect('/log')

@app.route('/v')
def view():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from user "
        result=database.select(query)
        return render_template('admin/view user.html',data=result)
    else:
        return redirect('/log')


@app.route('/facemask')
def facemassk():
    if session['lin'] == 'lo':
        database=Db()
        query="SELECT * FROM USER,assign_fine,`fine` WHERE user.userid=assign_fine.userid AND `fine`.`fineid`=`assign_fine`.`fineid`"
        result=database.select(query)
        return render_template('admin/facemask.html',data=result)
    else:
        return redirect('/log')

@app.route('/complaint')
def complaintt():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from user,complaint where user.userid=complaint.userid"
        result=database.select(query)
        return render_template('admin/complaint.html',data=result)
    else:
        return redirect('/log')

@app.route('/rep/<y>')
def reply(y):
    if session['lin'] == 'lo':
        return render_template('admin/reply.html',data=y)
    else:
        return redirect('/log')

@app.route('/repp/<j>',methods=['post'])
def replyy(j):
    if session['lin'] == 'lo':
        database=Db()
        reply=request.form['textarea']
        query="update complaint set reply='"+reply+"',replydate=curdate() where complaintid='"+j+"'"
        database.update(query)
        return '''<script>alert("submitted  succesfully");window.location="/complaint"</script>'''
    else:
        return redirect('/log')

@app.route('/cam')
def cam():
    if session['lin'] == 'lo':
        return render_template('admin/camera.html')
    else:
        return redirect('/log')

@app.route('/cam1',methods=['post'])
def cam1():
    if session['lin'] == 'lo':
        database =Db()
        serial=request.form['textfield']
        model=request.form['textfield2']
        loc=request.form['textfield3']
        latt=request.form['textfield4']
        lon=request.form['textfield5']
        query2="insert into camera VALUES ('','"+serial+"','"+model+"','"+loc+"','"+latt+"','"+lon+"')"
        database.insert(query2)
        return  '''<script>alert("camera added succesfully");window.location='/viewcam'</script>'''
    else:
        return redirect('/log')

@app.route('/viewcam')
def viewcam():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from camera "
        result=database.select(query)
        return render_template('admin/view camera.html',data=result)
    else:
        return redirect('/log')


@app.route('/delcam/<a>')
def delcam(a):
    if session['lin'] == 'lo':
        database=Db()
        query="delete from camera where cameraid='"+a+"'"
        result=database.delete(query)
        return redirect('/viewcam')
    else:
        return redirect('/log')


@app.route('/fine')
def fine():
    if session['lin'] == 'lo':
        return render_template('admin/generate fine.html')
    else:
        return redirect('/log')

@app.route('/fine1',methods=['post'])
def fine1():
    if session['lin'] == 'lo':
        database =Db()
        de=request.form['textarea']
        fine=request.form['textfield3']
        d=request.form['textfield']
        query2="insert into fine VALUES ('','"+d+"','"+de+"','"+fine+"')"
        database.insert(query2)
        return '''<script>alert("fine added succesfully");window.location='/viewf'</script>'''
    else:
        return redirect('/log')

@app.route('/viewf')
def viewf():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from fine "
        result=database.select(query)
        return render_template('admin/view fine.html',data=result)
    else:
        return redirect('/log')


@app.route('/delf/<a>')
def delf(a):
    if session['lin'] == 'lo':
        database=Db()
        query="delete from fine where fineid='"+a+"'"
        result=database.delete(query)
        return redirect('/viewf')
    else:
        return redirect('/log')

@app.route('/adviewv')
def adviewv():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from violation "
        result=database.select(query)
        return render_template('admin/view offence.html',data=result)
    else:
        return redirect('/log')



################# TRAFFIC POLICE #######################

@app.route('/thome')
def thome():
    if session['lin'] == 'lo':
        return render_template("tp/tp home.html")
    else:
        return redirect('/log')

@app.route('/viewp')
def viewp():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from trafficpolice where  trafficid='"+str( session['lid'])+"'"
        result=database.selectOne(query)
        return render_template('tp/view profile.html',data=result)
    else:
        return redirect('/log')

@app.route('/detectmask')
def detectmask():
    if session['lin'] == 'lo':
        database=Db()
        query="SELECT * FROM assign_fine,USER,`fine` WHERE assign_fine.userid=user.userid AND `assign_fine`.`fineid`=`fine`.`fineid` ORDER BY afineid DESC"
        result=database.select(query)
        return render_template('tp/detect mask.html',data=result)
    else:
        return redirect('/log')

@app.route('/tpviewf')
def tpviewf():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from fine "
        result=database.select(query)
        return render_template('tp/view fine.html',data=result)
    else:
        return redirect('/log')


@app.route('/viol')
def viol():
    if session['lin'] == 'lo':
        return render_template("tp/add offence.html")
    else:
        return redirect('/log')

@app.route('/viol1',methods=['post'])
def viol1():
    if session['lin'] == 'lo':
        database = Db()
        v=request.form['textfield']
        p=request.form['textarea']
        res=database.insert("insert into violation values('','"+v+"','"+p+"')")
        return '''<script>alert("Offence Added");window.location='/viewv'</script>'''
    else:
        return redirect('/log')

@app.route('/viewv')
def viewv():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from violation "
        result=database.select(query)
        return render_template('tp/view offence.html',data=result)
    else:
        return redirect('/log')

@app.route('/dele/<a>')
def dele(a):
    if session['lin'] == 'lo':
        database=Db()
        query="delete from violation where vid='"+a+"'"
        result=database.delete(query)
        return redirect('/viewv')
    else:
        return redirect('/log')




############### USER ###########

@app.route('/userreg')
def userreg():
    return render_template('user/registration.html')


@app.route('/userreg1',methods=['post'])
def userreg1():
    database =Db()
    name=request.form['textfield']
    phone=request.form['textfield2']
    email=request.form['textfield3']
    gender=request.form['radio']
    f=request.files['file']
    import datetime
    d=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    # f.save("C:\\Users\\ToShibA\\PycharmProjects\\facemask\\static\\"+d+".jpg")
    f.save(r"C:\Users\ToShibA\Downloads\facemask\static\\"+d+".jpg")
    path="/static/"+d+".jpg"
    p=request.form['passw']
    cp=request.form['cpassw']
    if p==cp:
        query = "insert into login VALUES ('','"+email+"','"+p+"','user')"
        res=database.insert(query)
        query2="insert into user VALUES ('"+str(res)+"','"+name+"','"+phone+"','"+email+"','"+gender+"','"+str(path)+"')"
        database.insert(query2)
        return  '''<script>alert("user added succesfully");window.location='/'</script>'''
    else:
        return '''<script>alert("Password Mismatch");window.location='/'</script>'''

@app.route('/uhome')
def uhome():
    if session['lin'] == 'lo':
        return render_template('user/uhome.html')
    else:
        return redirect('/log')

@app.route('/uprofile')
def uprofile():
    if session['lin'] == 'lo':
        database = Db()
        query = "select * from user where  userid='" + str(session['lid']) + "'"
        result = database.selectOne(query)
        return render_template('user/view profile.html', data=result)
    else:
        return redirect('/log')

@app.route('/viewmv')
def viewmv():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from assign_fine,fine where assign_fine.fineid=fine.fineid and assign_fine.userid='"+str( session['lid'])+"'"
        result=database.select(query)
        return render_template('user/view_maskviolation.html',data=result)
    else:
        return redirect('/log')

@app.route('/sc')
def sc():
    if session['lin'] == 'lo':
        return render_template('user/Send complaint.html')
    else:
        return redirect('/log')

@app.route('/sc1',methods=['post'])
def sc1():
    if session['lin'] == 'lo':
        database =Db()
        c=request.form['t']
        query2="insert into complaint VALUES ('','" + str(session['lid']) + "','"+c+"',curdate(),'pending','')"
        database.insert(query2)
        return  '''<script>alert("complaint added succesfully");window.location='/uhome'</script>'''
    else:
        return redirect('/log')

@app.route('/viewreply')
def viewreply():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from complaint where userid='" + str(session['lid']) + "'"
        result=database.select(query)
        return render_template('user/view reply.html',data=result)
    else:
        return redirect('/log')

@app.route('/adh')
def adh():
    if session['lin'] == 'lo':
     return render_template('user/aadhar.html')
    else:
        return redirect('/log')

@app.route('/adh1',methods=['post'])
def adh1():
    if session['lin'] == 'lo':
        num=request.form['textfield']
        database = Db()
        qry=database.selectOne("select * from aadhar where userid='"+str(session['lid'])+"'")
        if qry is not None:
            qry=database.update("update aadhar set aadhar_number='"+num+"' where userid='"+str(session['lid'])+"'")
            return '''<script>alert("Adhaar Updated succesfully");window.location='/uhome'</script>'''
        else:
            qry=database.insert("insert into aadhar values('','"+num+"','" + str(session['lid']) + "')")
            return '''<script>alert("Adhaar Added succesfully");window.location='/uhome'</script>'''
    else:
        return redirect('/log')

@app.route('/uviewv')
def uviewv():
    if session['lin'] == 'lo':
        database=Db()
        query="select * from violation "
        result=database.select(query)
        return render_template('user/view offence.html',data=result)
    else:
        return redirect('/log')

if __name__ == '__main__':
    app.run(debug=True)