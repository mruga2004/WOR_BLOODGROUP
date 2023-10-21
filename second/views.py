from django.http import HttpResponse;
from django.shortcuts import render;

def home(req):
    posiB=0;
    negB=0;
    posiAB=0;
    negAB=0;
    posiA = 0;
    negA = 0;
    Tposi =0;
    Tneg=0;
    posiO=0;
    negO=0;
    try:    
        inf=req.GET['num1']
        inm=req.GET.get('num2')
        
        dic1 = {
            "A+": ["A+","A+","A+","A-","A+","i+","A+","i-","A-","i+","A-","A+"],
            "B+": ["B+","B+","B+","B-","B+","i+","B+","i-","B-","i+","B-","B+"],
            "O+":["i+","i-","i-","i+","i+","i+"],
            "AB+":["A+","B+","A+","B-","A-","B+"],
            "A-":["A-","A-","A-","i-"],
            "B-":["B-","B-","B-","i-"],
            "O-":["i-","i-","i-","i-"],
            "AB-": ["A-","B-"]
        }
        P11=[]
        for i in dic1[inf]:
            for j in dic1[inm]:
                P11.append(i+j)
        lenn=len(P11)
        av=100/lenn
        for i in P11:
            if "+" in i:
                Tposi += av
                if i.count("A")==2:
                    posiA += av
                elif i.count("A")==1 and i.count("i")==1:
                    posiA += av
                elif i.count("B")==2:
                    posiB += av
                elif i.count("B")==1 and i.count("i")==1:
                    posiB += av
                elif i.count("i")==2:
                    posiO +=av
                elif i.count("A")==1 and i.count("B")==1:
                    posiAB +=av
            else:
                Tneg += av
                if i.count("A")==2:
                    negA += av
                elif i.count("A")==1 and i.count("i")==1:
                    negA += av
                elif i.count("B")==2:
                    negB += av
                elif i.count("B")==1 and i.count("i")==1:
                    negB += av
                elif i.count("i")==2:
                    negO +=av
                elif i.count("A")==1 and i.count("B")==1:
                    negAB +=av
        
        return render(req,"index.html",{'posiA':posiA,'posiB':posiB,'posiO':posiO,'posiAB':posiAB,'negA':negA,'negB':negB,'negO':negO,'negAB':negAB})
    except:
        pass

    return render(req,"index.html")

def info(req):
    data={'take':'','give':''}
    try:
        inn = req.GET.get('posi')
        if(inn=='posiA'):
            data={'take':'From whom you can recieve : A+ O+ O- A-',
                  'give':'To whom you can give : A+ AB+ '}
            return render(req,"info.html",data)
        
        elif(inn=='posiB'):
            data={'take':'From whom you can recieve : B+ O+ O- B-',
                  'give':'To whom you can give : B+ AB+ '}
            return render(req,"info.html",data)
        
        elif(inn=='posiO'):
            data={'take':'From whom you can recieve : O+ O-',
                  'give':'To whom you can give : A+ B+ AB+ O+ '}
            return render(req,"info.html",data)
        
        elif(inn=='posiAB'):
            data={'take':'From whom you can recieve : A+ O+ B+ AB+ O- A- B-',
                  'give':'To whom you can give : AB+ '}
            return render(req,"info.html",data)
        
        elif(inn=='negA'):
            data={'take':'From whom you can recieve : O- A-',
                  'give':'To whom you can give : A+ AB+ A- AB- '}
            return render(req,"info.html",data)
        
        elif(inn=='negB'):
            data={'take':'From whom you can recieve :  O- B-',
                  'give':'To whom you can give : B+ AB+ B- AB- '}
            return render(req,"info.html",data)
        
        elif(inn=='negO'):
            data={'take':'From whom you can recieve :  O- ',
                  'give':'To whom you can give : A+ AB+ B+ A- B- AB- O- O+'}
            return render(req,"info.html",data)
        
        elif(inn=='negAB'):
            data={'take':'From whom you can recieve : O- A- B- AB-',
                  'give':'To whom you can give : AB- AB+  '}
            return render(req,"info.html",data)
        
    except:
        pass
    return render(req,"info.html",data)