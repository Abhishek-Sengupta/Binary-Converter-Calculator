from tkinter import *
con_cal = Tk()
con_cal.title("CONVERTER & BINARY CALCULATOR")

# Designing Back-end for CONVERTER
decimal_res=StringVar()
octal_res=StringVar()
hexadecimal_res=StringVar()

def Bin_to_Dec (binNum):
    decNum=0
    i=0
    while int(binNum)> 0:
        decNum += int(binNum %10) * (2**i)
        i+=1
        binNum /= 10
    return decNum

def Bin_to_Octal (binNum):
    octNum=0
    decNum = Bin_to_Dec(binNum)
    i=1
    while decNum != 0:
        octNum += int(decNum % 8)*i
        decNum /= 8
        i*=10
    return octNum

def Bin_to_Hex (binNum):
    hexNum=0
    decNum =Bin_to_Dec(binNum)
    i=1
    while decNum != 0:
        hexNum += int(decNum % 16)*i
        if ((decNum % 16)==10):
            hexNum='A'
            break
        if ((decNum % 16)==11):
            hexNum='B'
            break
        if ((decNum % 16)==12):
            hexNum='C'
            break
        if ((decNum % 16)==13):
            hexNum='D'
            break
        if ((decNum % 16)==14):
            hexNum='E'
            break
        if ((decNum % 16)==15):
            hexNum='F'
            break
        decNum /= 16
        i*=10
    return hexNum

def Convert():
    binNum=int(Entry.get(x1))
    
    decimal=(Bin_to_Dec(binNum))
    decimal_res.set(decimal)
    
    octal=(Bin_to_Octal(binNum))
    octal_res.set(octal)
    
    hexadecimal=(Bin_to_Hex(binNum))
    hexadecimal_res.set(hexadecimal)
    
# Designing Back-end for BINARY CALCULATOR
sum_res=StringVar()
diff_res=StringVar()
prod_res=StringVar()
quot_res=StringVar()
rem_res=StringVar()

def add(a,b):
    c=0
    sum=[]
    for i in range(8):
        x= a%2
        y= b%2
        s=(x^y)^c
        c=((x&y)|(y&c)|(c&x))
        a=int(a/2)
        b=int(b/2)
        sum.append(s)
    sum.reverse()
    summ=''.join(map(str, sum))
    return summ

def Addition():
    binNum1=int(Entry.get(x2),2)
    binNum2=int(Entry.get(x3),2)
    sum=(add(binNum1,binNum2))
    sum_res.set(sum)
    
def subs(a,b):
    bor=0
    diff=[]
    for i in range(8):
        x=a%2
        y=b%2
        d=(x^y)^bor
        bor=(~(x^y) & bor) | ((~x) & y)
        a=int(a/2)
        b=int(b/2)
        diff.append(d)
    diff.reverse()
    difference=''.join(map(str, diff))
    return difference 

def Substraction():
    binNum1=int(Entry.get(x2),2)
    binNum2=int(Entry.get(x3),2)
    diff=(subs(binNum1,binNum2))
    diff_res.set(diff)
    
def multiply (a,b):
    l=[]
    for i in range(8):
        e=b%2
        p = a*e
        l.append(p)  #partial products appended to the list l
        b=int(b/2)
        
    l[1]=l[1]<<1     #2nd partial product
    l[2]=l[2]<<2     #3rd partial product
    l[3]=l[3]<<3     #4th partial product
    #partial products added to produce the final product
    sum1=add(l[0],l[1])
    sum2=add(l[2],l[3])
    sum1b=int(sum1,2)
    sum2b=int(sum2,2)
    sum3=add(sum1b,sum2b)
    return sum3

def Multiplication():
    binNum1=int(Entry.get(x2),2)
    binNum2=int(Entry.get(x3),2)
    prod=(multiply(binNum1,binNum2))
    prod_res.set(prod)

def div(a,b):
    q=0
    while(a >= b):
        q=int(add(q,1),2)
        a=int(subs(a,b),2) #using subtractive method
    return (bin(q),a)      # here, q will be quotient, a will be remainder

def Division():
    binNum1=int(Entry.get(x2),2)
    binNum2=int(Entry.get(x3),2)
    quot,rem = div(binNum1,binNum2)
    quot_res.set(quot)
    rem_res.set(rem)

# Designing Front-End for CONVERTER
label1= Label(con_cal, text="CONVERTER", bg="dark green", fg="light green", font = "TIMES 14 bold italic").grid(row=1,column=2)
label2= Label(con_cal, text="Enter the binary number:").grid(row=2,column=1)
x1=Entry(con_cal, width = 30)
x1.grid(row=2,column=2)
convert = Button(con_cal, text="CONVERT",command=Convert).grid(row=2,column=3)

dec_label3 = Label(con_cal, text="DECIMAL:", fg="red").grid(row=3,column=1)
dec_label_res = Label(con_cal, textvariable=decimal_res).grid(row=3,column=2)
oct_label4 = Label(con_cal, text="OCTAL:", fg="red").grid(row=4,column=1)
oct_label_res = Label(con_cal, textvariable=octal_res).grid(row=4,column=2)
hex_label5 = Label(con_cal, text="HEXADECIMAL:", fg="red").grid(row=5,column=1)
hex_label_res = Label(con_cal, textvariable=hexadecimal_res).grid(row=5,column=2)

# Designing Front-End for BINARY CALCULATOR
label6= Label(con_cal, text="BINARY CALCULATOR", bg="dark green", fg="light green", font = "TIMES 14 bold italic").grid(row=7,column=2)
label7= Label(con_cal, text="Enter Operand 1 (in binary):").grid(row=8,column=1)
x2=Entry(con_cal, width = 30)
x2.grid(row=8,column=2)
label8= Label(con_cal, text="Enter Operand 2 (in binary):").grid(row=9,column=1)
x3=Entry(con_cal, width = 30)
x3.grid(row=9,column=2)

sum_label9 = Label(con_cal, text="SUM:", fg="red").grid(row=10,column=1)
sum_label_res = Label(con_cal, textvariable=sum_res).grid(row=10,column=2)
adder = Button(con_cal, text="+", width= 4, command=Addition).grid(row=10,column=4)

diff_label10 = Label(con_cal, text="DIFFERENCE:", fg="red").grid(row=11,column=1)
diff_label_res = Label(con_cal, textvariable=diff_res).grid(row=11,column=2)
subtractor = Button(con_cal, text="-", width = 4, command=Substraction).grid(row=11,column=4)

prod_label11 = Label(con_cal, text="PRODUCT:", fg="red").grid(row=12,column=1)
prod_label_res = Label(con_cal, textvariable=prod_res).grid(row=12,column=2)
multiplier = Button(con_cal, text="*", width = 4, command=Multiplication).grid(row=12,column=4)

div_label12 = Label(con_cal, text="DIVISION:", fg="red").grid(row=13,column=1)
quot_label13 = Label(con_cal, text="QUOTIENT:", fg="red").grid(row=13,column=2)
quot_label_res = Label(con_cal, textvariable=quot_res).grid(row=13,column=3)
rem_label14 = Label(con_cal, text="REMAINDER:", fg="red").grid(row=14,column=2)
rem_label_res = Label(con_cal, textvariable=rem_res).grid(row=14,column=3)
divider = Button(con_cal, text="/", width = 4, command=Division).grid(row=13,column=4)

con_cal.mainloop()
