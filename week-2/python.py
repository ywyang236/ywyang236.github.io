print("=== Task 1 ===")

def find_and_print(messages):
    for key, message in messages.items():
        # 判斷條件一：包含 "student" 和 "college"
        if "student" in message and "college" in message:
            print(key)

        # 判斷條件二：包含 "18 years old"
        if "18 years old" in message:
            print(key)

        # 判斷條件三：包含 "vote"
        if "vote" in message:
            print(key)

        # 判斷條件四：包含 "legal age"
        if "legal age" in message:
            print(key)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})


print("=== Task 2 ===")


def calculate_sum_of_bonus(data):
    sum_of_bonus = 0

    # 根據 performance 計算 bonus_percentage
    for employee in data["employees"]:
        salary = convert_salary_to_twd(employee["salary"])
        performance = employee["performance"]
        bonus_percentage = 0
        # 如果 performance 是 above average，bonus_percentage 是 12%
        if performance == "above average":
            bonus_percentage = 0.12
        # 如果 performance 是 average，bonus_percentage 是 8%
        elif performance == "average":
            bonus_percentage = 0.08
        # 如果 performance 是 below average，bonus_percentage 是 3%
        elif performance == "below average":
            bonus_percentage = 0.03

        bonus_amount = salary * bonus_percentage
        sum_of_bonus += bonus_amount
    print("Total Bonus:", sum_of_bonus)


# 將 salary 統一格式，預設數值是新台幣，如果有出現美金USD，就用1:30換算
def convert_salary_to_twd(salary):
    if isinstance(salary, str):
        if "USD" in salary:
            salary = int(salary.replace("USD", "")) * 30
        elif "," in salary:
            salary = int(salary.replace(",", ""))
    return salary


calculate_sum_of_bonus({"employees": [
    {
        "name": "John",
        "salary": "1000USD",
        "performance": "above average",
        "role": "Engineer"
    },
    {
        "name": "Bob",
        "salary": 60000,
        "performance": "average",
        "role": "CEO"
    },
    {
        "name": "Jenny",
        "salary": "50,000",
        "performance": "below average",
        "role": "Sales"
    }
]
})  # call calculate_sum_of_bonus function


print("=== Task 3 ===")


def func(*data):
    # 用迴圈檢查 func () 裡每個字串的第二個字中間是否重複，印出沒有重複的那一個字串
    for i in range(len(data)):
        str = data[i]
        middleChar = str[1]
        # 比較不同字串的第二個字是否相同
        restStr = ''
        for j in range(len(data)):
            if i != j:
                restStr += data[j]
        # 如果沒有重複，就印出字串
        if middleChar not in restStr:
            print(str)
            break
        # 如果全部的字串的第二個字都有重複，印出沒有
        if i == len(data) - 1:
            print('沒有')


func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有


print("=== Task 4 ===")


def get_number(index):
    odd = 3
    even = 4
    mergedSequence = [0]

    for i in range(10):
        if i % 2 == 0:
            mergedSequence.append(even)
            even += 3
        else:
            mergedSequence.append(odd)
            odd += 3

    print(mergedSequence[index])


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15
