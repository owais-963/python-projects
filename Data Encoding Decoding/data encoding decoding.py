from os import error
############################# DATA ENCODING AND DECODING ####################################


######################## BINARY TO DECIMAL #############################

def bin_to_deci(binary):
  pow=len(binary)-1
  deci=0
  for digit in binary:
    digit=int(digit)
    deci+=(digit * 2 ** pow)
    pow-=1
  return deci



######################### DECIMAL TO BINARY ##############################


def deci_to_bin(n):

  try:
    bin=""

    while True:
      bin=(str(n%2))+bin
      n=n//2

      if n==0:
        break

    return bin

  except Exception as e:

    print(e)


############################ NUMERIC MODE ###################################


################### ENCODE ##############################


def numeric_mode_encode(file_name):
  with open(file=file_name,mode="r") as f:
    
    text=f.read()

    num=''
    for i in text:
      if ord(i)<30:
        num=num+('0'+str(ord(i)))
      else:
        num=num+(str(ord(i)))


  num_in_pair=[]

  start=0
  end=3
  for j in range(len(num)//3):
    num_in_pair.append((num[start:end]))
    start+=3
    end+=3

  num_in_pair.append((num[-(len(num)%3):len(num)])) 

  open(file_name[0:-4]+".bin","w").close()


  with open(file=file_name[0:-4]+".bin",mode='a+') as bf:

    bf.write('001')

    for i in num_in_pair:

      if len(i)==3:

        b_f=deci_to_bin(int(i))
        b_f=[x for x in b_f]

        if len(b_f)>10:
          n=len(b_f)-10
          del b_f[0:n]

        elif len(b_f)<10:
          for i in range(10-len(b_f)):
            b_f.insert(0,'0')

        for x in b_f: 
          bf.write(x)



      elif len(i)==2:

          b_f=deci_to_bin(int(i))
          
          b_f=[x for x in b_f]

          if len(b_f)>7:
            del b_f[0:len(b_f)-7]

          elif len(b_f)<7:
            for i in range(7-len(b_f)):
              b_f.insert(0,'0')

          for x in b_f:
            bf.write(x)


      elif len(i)==1:

          b_f=deci_to_bin(int(i))

          b_f=[x for x in b_f]

          if len(b_f)>4:
            del b_f[0:len(b_f)-4]

          elif len(b_f)<4:
            for i in range(4-len(b_f)):
              b_f.insert(0,'0')

          for x in b_f:
            bf.write(x)

    bf.close()

  bin_file = file_name[0:-4]+".bin"
  
  return bin_file






###################  DECODE ##############################

def numeric_mode_decode(file_name):

  with open(file=file_name,mode='r') as bf:

    data=bf.read()

    bf.close()


  if data[0:3]=='001':

    data=[x for x in data]
    del data[0:3]
    data="".join(data)

    num_in_pair=[]

    start=0
    end=10

    for j in range(len(data)//10):

      str_deci=str(bin_to_deci(str(data[start:end])))

      if len(str_deci)<3:

        for i in range(3-len(str_deci)):

          str_deci= '0' + str_deci



      num_in_pair.append(str_deci)

      start=end
      end+=10

    if len(data)%10==6:

      str_deci=str(bin_to_deci(str(data[-(len(data)%10):len(data)])))

      for i in range(2-len(str_deci)):

        str_deci= '0' + str_deci


    else:
      num_in_pair.append(str(bin_to_deci(str(data[-(len(data)%10):len(data)]))))

    num_str="".join(num_in_pair)

    text=""

    start=0

    if int(num_str[0])==0:
      start=1
      end=3
    elif int(num_str[0])==2 or int(num_str[0])==1:
      end=3
    else:
      end=2

    while end<=len(num_str):

      text=text+chr(int(num_str[start:end]))

      if end==len(num_str):
        break

      start=end

      if int(num_str[start])==0:
        start+=1
        end+=3

      elif int(num_str[start])==2 or int(num_str[start])==1:

        end+=3

      elif int(num_str[start])>2:

        end+=2

    with open(file_name[0:-4]+".txt",'w') as tf:

      tf.write(text)

      tf.close()

    text_file = file_name[0:-4]+".txt"

    return text_file

  elif data[0:3]=="010":
    return alphanumeric_mode_decode(file_name)

  elif data[0:3]=="011":
    return byte_mode_decode(file_name)

  else:

    return 'This file does not belong to any of the three kind of mehod'




##############################################################################

###################### ALPHA NUMERIC MODE ###################################

############### ENCODING ##################

def alphanumeric_mode_encode(file_name):
  with open(file=file_name[0:-4]+".bin", mode="w") as bf:

    bf.write("010")

    bf.close()

  with open(file=file_name, mode='r') as tf:

    txt=tf.read()

    tf.close()

  list_txt=[]

  start=0
  end=2

  for i in range(len(txt)//2):

    list_txt.append(txt[start:end])

    start=end
    end+=2

    bin_list=[]

  with open(file=file_name[0:-4]+".bin", mode="a+") as bf:

    for pair in list_txt:

      x=ord(pair[0])
      y=ord(pair[1])

      n = 45*x + y


      bin_digit = deci_to_bin(n)

      bin_x=deci_to_bin(x)

      if len(bin_x)<10:
        for i in range(10-len(bin_x)):
          bin_x='0'+bin_x

      if len(bin_digit)<15:
        for i in range(15-len(bin_digit)):
          bin_digit='0'+bin_digit

      b_f=bin_digit+bin_x

      bf.write(b_f)

    if len(txt)%2>0:

      b_f=(deci_to_bin(ord(txt[-1])))


      if len(b_f)<10:
        for _ in range(10-len(b_f)):
          b_f='0'+b_f 

      bf.write(b_f)

    bf.close()

    bin_file=file_name[0:-4]+".bin"

    return bin_file



################# DECODING #########################


def alphanumeric_mode_decode(file_name):
  with open(file=file_name, mode="r") as f:
    data=f.read()
    f.close()


  if data[0:3]=="010":

    data=[x for x in data]

    del data[0:3]

    data="".join(data)

    start=0
    end=25

    with open(file=file_name[0:-4]+".txt", mode="w") as f:

      for _ in range(len(data)//25):

        data_chunk = data[start:end]

        n = int(bin_to_deci(data_chunk[0:15]))

        x = int(bin_to_deci(data_chunk[15:len(data_chunk)]))
      

        y = n-(45*x)


        f.write(chr(x))
        f.write(chr(y))

        start=end
        end+=25

      if len(data)%25>0:

        f.write(chr(int(bin_to_deci(data[-10:len(data)]))))

      f.close()

    txt_file=file_name[0:-4]+".txt"

    return txt_file

  elif data[0:3]=='001':

    return numeric_mode_decode()

  elif data[0:3]=="011":

    return byte_mode_decode()

  else:

    return 'This file does not belong to any of the three kind of mehod'



#############################################################################

####################### BYTE MODE ###########################################

def byte_mode_encode(file_name):

  with open(file=file_name, mode="r") as f:
    text = f.read()
    f.close()

  with open(file=file_name[0:-4]+".bin", mode='w') as bf:

    bf.write("011")

    for char in text:

      bin_digit=deci_to_bin(ord(char))

      for _ in range(10-len(bin_digit)):

        bin_digit = '0'+bin_digit

      bf.write(bin_digit)

    bf.close()

  bin_file = file_name[0:-4]+".bin"
  
  return bin_file

################ DECODE ##################

def byte_mode_decode(file_name):
  with open(file=file_name, mode="r") as f:

    data=f.read()

    f.close()

  if data[0:3]=='011':

    data = [x for x in data]

    del data[0:3]

    data = "".join(data)

    start=0
    end=10

    with open(file=file_name[0:-4]+".txt", mode="w+") as f:

      for i in range(len(data)//10):

        bin_digit = data[start:end]

        deci_digit = bin_to_deci(bin_digit)

        text = chr(int(deci_digit))

        f.write(text)

        start=end
        end+=10

    text_file = file_name[0:-4]+".txt"

    return text_file
  
  elif data[0:3]=="010":

    return alphanumeric_mode_decode(file_name)

  elif data[0:3]=="001":

    return numeric_mode_decode(file_name)

  else:

    return 'This file does not belong to any of the three kind of mehod'



######################################################################




encoding = 1

numeric = 1

alphanumeric = 2

byte = 3

decoding = 2

Flag = True

while Flag:

  try:

    purpose = int(input("Enter 1 for encoding 2 for decoding 0 for quit: "))

    if purpose == encoding:

      file_name = input("Enter the file name: ")

      if file_name[-4:len(file_name)] == ".txt":

        mode = int(input("Enter 1 for numeric mode 2 for alphanumeric 3 for byte and 0 for quit"))

        if mode == numeric:

          file_name=numeric_mode_encode(file_name)
          print(file_name)

        elif mode == alphanumeric:

          file_name=alphanumeric_mode_encode(file_name)
          print(file_name)

        elif mode == byte:

          file_name=byte_mode_encode(file_name)
          print(file_name)

        elif mode == 0:

          Flag = False

      else:

        print("Only '.txt' files can be encoded")

    elif purpose == decoding:

      file_name=input("Enter the file name: ")

      if file_name[-4:len(file_name)]==".bin":

        file_name = numeric_mode_decode(file_name)

        if file_name[-4:len(file_name)]==".txt":

          print(file_name)

          print()

          with open(file=file_name, mode="r") as f:

            print(f.read())

            f.close()


        else:

          print(file_name)

      else:

        print("Only '.bin' files can be decoded")



    elif purpose == 0:

      Flag = False

    else:

      print("Please enter the valid option")


  except Exception as e:

    print(f".... {e} .... error")


