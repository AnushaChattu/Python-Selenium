#Example-1
# file=open("C:/demofiles/myfile.txt","w")
# print("file opened")
# file.write("this is my first statement\n")
# file.write("this is my second statement\n")
# file.write("this is my third statement\n")
# file.write("this is my fourth statement\n")
# file.write("this is my fifth statement\n")
# file.close()
# print("file closed")

# #Example-2
# file=open("C:/demofiles/myfile.txt")
# print(file.read())
# #print(file.readline())
# file.close()
#
# #Example-3
file=open("C:/demofiles/myfile.txt","a")
file.write("this is my sixth line/n")
file.write("this is my seventh line/n")
file.close()
print("file closed")