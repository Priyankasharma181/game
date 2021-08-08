import requests
import json

x = requests.get("http://saral.navgurukul.org/api/courses")

Data = x.json()

with open("data.json","w") as f:
    json.dump(Data,f,indent=4)
serial_number=1
name_list=[]


for index in Data["availableCourses"]:
    print(serial_number,"-",index["name"],index["id"])
    name_list.append(index["name"])
    serial_number+=1

topic=int(input("Enter the topic number:"))


a=input("Enter whether you want to go next or previous(n/p):")
serial_number=topic
print(name_list[serial_number-1])


if a=="p":
    serial_number=1
    for index in Data["availableCourses"]:
        print(serial_number,"-",index["name"],index["id"])
        serial_number+=1
    topic=int(input("Enter the topic number:"))


y=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercises")

data=y.json()

with open("parent.json","w") as f:
    json.dump(data,f,indent=4)
serial_no=1
serial_no1=1
topic_list=[]

for index1 in data["data"]:
    if len(index1["childExercises"])==0:
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        print("           ",serial_no1,".",index1["slug"])
        serial_no+=1
    else:
        serial_no2=1
        print("   ",serial_no,".",index1["name"])
        topic_list.append(index1["name"])
        for questions in index1["childExercises"]:
            print("         ",serial_no2,".",questions["name"])
            serial_no2+=1
        serial_no+=1

parent=int(input("enter the number"))

a=input("Enter whether you want to go next or previous(n/p):")

serial_no=1
serial_no1=1
if a=="p":
    for index1 in data["data"]:
        if len(index1["childExercises"])==0:
            print("   ",serial_no,".",index1["name"])
            print("           ",serial_no1,".",index1["slug"])
            serial_no+=1
        else:
            serial_no2=1
            print("   ",serial_no,".",index1["name"])
            for questions in index1["childExercises"]:
                print("         ",serial_no2,".",questions["name"])
                serial_no2+=1
            serial_no+=1

slug=int(input("Enter the topic number:"))
question_list=[]
slug_list=[]
print("     ",slug,".",topic_list[slug-1])

for index1 in data["data"][slug-1]["childExercises"]:
    s_num=1
    for index1 in data["data"][slug-1]["childExercises"]:
        print("           ",s_num,".",index1["name"])
        question_list.append(index1["name"])
        s_num+=1

    que=int(input("Enter question number:")) 
    w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-1]["slug"]))
    DATA=w.json()
    with open("question.json","w") as f:
        json.dump(DATA,f,indent=4)
        print(DATA["content"])
        break

for i in range(len(question_list)):
    a=input("Enter whether you want to go next or previous(n/p):")
    if a=="n":
        if que==len(question_list): 
            print("Next page.")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que+1
    if a=="p":
        if que==len(question_list):
            print("No more questions")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-2]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que-1

else:
    s_no=1
    print("           ",s_no,".",data["data"][slug-1]["slug"])
    slug_list.append(data["data"][slug-1]["slug"])

    que=int(input("Enter question number:"))
    v=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
    d=v.json()
    with open("questions.json","w") as f:
        json.dump(d,f,indent=4)
        print(d["content"])
    for i in range(len(slug_list)):
        a=input("Enter whether you want to go next or previous:(n/p)")
        if a=="n":
            print("Next page.")
        elif a=="p":
            print("No more questions.")