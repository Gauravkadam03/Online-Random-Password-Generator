from django.shortcuts import render,redirect
import random
from django.contrib import messages
# Create your views here.

def p_v(chr,p_len):
    random.shuffle(chr)
    passw = ''
    while len(passw) < p_len:
        a = random.choice(chr)
        if a not in passw:
            passw += a
    return passw

def Home(request):
    if request.method=='POST':
        p_len=request.POST.get('length')
        
        cp=request.POST.get('capital')
        sm=request.POST.get('small')
        sy=request.POST.get('symbol')
        nm=request.POST.get('number')
        
        if p_len != '':
            p_len=int(p_len)
            if p_len >= 4 and p_len <= 15:
                
                if cp == 'on' and (sm == None and sy == None and nm == None) :
                    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif sm == 'on' and (cp == None and sy == None and nm == None)  : 
                    chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif sy == 'on' and (cp == None and sm == None and nm == None) :
                    chr = ['@', '*', '$', '%', '&','#','?','+','^']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif nm == 'on' and (cp == None and sm == None and sy == None) :
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (sm == 'on'and cp == 'on') and (sy == None and nm == None):
                    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif (sm == 'on'and cp == 'on' and sy == 'on') and ( nm == None):
                    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@', '*', '$', '%', '&']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (sy == 'on'and cp == 'on') and (sm == None and nm == None):
                    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '*', '$', '%', '&']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (nm == 'on'and cp == 'on') and (sy == None and sm == None):
                    chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif (sy == 'on'and sm == 'on') and (cp == None and nm == None):
                    chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@', '*', '$', '%', '&']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (sm == 'on'and nm == 'on') and (cp == None and sy == None):
                    chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (sy == 'on'and nm == 'on') and (cp == None and sm == None):
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','@', '*', '$', '%', '&']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
                
                elif (sm == 'on'and nm == 'on' and sy == 'on') and ( cp == None):
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@', '*', '$', '%', '&']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif (sm == 'on'and nm == 'on' and cp == 'on') and ( sy == None):
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                elif (sy == 'on'and nm == 'on' and cp == 'on') and ( sm == None):
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','@', '*', '$', '%', '&','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})

                else :
                    chr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','@', '*', '$', '%', '&','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                    c_pass = p_v(chr,p_len)
                    return render(request,'Generate/Home.html',{'password':c_pass})
        else:
            messages.error(request,'please enter password length above 4')

    return render(request, 'Generate/home.html')
