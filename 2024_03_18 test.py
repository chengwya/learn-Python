# student_score = {"小明": 80, "小红": 90, "小王": 88}
# student_score["小李"] = 84
# print(student_score) # {'小明': 80, '小红': 90, '小王': 88, '小李': 84}

# student_score = {"小明": 80, "小红": 90, "小王": 88}
# student_score["小明"] = 84
# print(student_score) # {'小明': 84, '小红': 90, '小王': 88}

# student_score = {"小明": 80, "小红": 90, "小王": 88}
# student_score.clear()
# print(student_score) # {}

# student_score = {"小明": 80, "小红": 90, "小王": 88}
# obtain_value = student_score.keys()
# print(obtain_value) # dict_keys(['小明', '小红', '小王'])
# print(student_score) # {}
# student_score = {"小明": 80, "小红": 90, "小王": 88}
# obtain_value = student_score.keys()
# for key in obtain_value:
#     print(f"Key：{key}")
#     print(f"Value：{student_score[key]}")
# Key：小明
# Value：80
# Key：小红
# Value：90
# Key：小王
# Value：88

staff_information = {"小明": {"部门": "营销部", "工资": 3500, "级别": 1},
                     "小红": {"部门": "运营部", "工资": 4000, "级别": 2},
                     "小李": {"部门": "技术部", "工资": 5000, "级别": 3},
                     "小王": {"部门": "管理部", "工资": 7000, "级别": 1},
                     "小黑": {"部门": "安保部", "工资": 3000, "级别": 1}}
for i in staff_information:
    if(staff_information[i]["级别"] == 1):
        staff_information[i]["级别"] += 1
        staff_information[i]["工资"] += 1500

print(staff_information )
