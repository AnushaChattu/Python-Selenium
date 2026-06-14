#ex-1 creating dictionary
# mydic={101:"x",102:"y",103:"z"}
# print(mydic)        {101: 'x', 102: 'y', 103: 'z'}

#ex-2 access items from dictionary
# mydic={
#     "brand":"maruthisuzuki",
#     "model":"vdl",
#     "year":2026
# }
# print(mydic["brand"])
# print(mydic["model"])
# #using get
# print(mydic.get("year"))

#ex-3 change values in dictionary
# mydic={
#      "brand":"maruthisuzuki",
#      "model":"vdl",
#      "year":2026
#  }
# print(mydic)
# mydic["year"]=2025
# print(mydic)

#ex-4 reading items from dictionary using loop
# mydic={
#     "brand":"maruthisuzuki",
#     "model":"vdl",
#     "year":2026
# }
# for i in mydic:
#     print(i)
# for i in mydic:
#     print(mydic[i])
# for i in mydic.values():
#     print(i)
# for x,y in mydic.items():
#     print(x,y)

#ex-5 check key is exist in dictionary
# mydic={
#     "brand":"maruthisuzuki",
#     "model":"vdl",
#     "year":2026
# }
# if "model1" in mydic:
#     print("exist")
# else:
#     print("not exist")

#ex-6 find no of items in dictionary
# mydic={
#     "brand":"maruthisuzuki",
#     "model":"vdl",
#     "year":2026
# }
# print(len(mydic))

#ex-7 adding items to dictionary
# mydic={
#     "brand":"maruthisuzuki",
#     "model":"vdl",
#     "year":2026
# }
# mydic['color']="red"
# print(mydic)

#ex-8 remove item from dictionary
mydic1={
    "brand":"maruthisuzuki",
    "model":"vdl",
    "year":2026
}
mydic1.pop("brand")
print(mydic1)
# del mydic["brand"]
# print(mydic)
# mydic.clear()
# print(mydic)
#using copy()
mydic2=mydic1.copy()
print(mydic2)
#without using copy()
mydic2=mydic1
print(mydic2)