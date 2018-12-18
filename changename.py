import os

os.chdir(r'C:\Users\student\CHANGE\SSAFY지원자')

for a in os.listdir(".") :
    a_r = a.replace("SAMSUNG_","SSAFY")
    os.renames(a,a_r)
#.은 현재폴더