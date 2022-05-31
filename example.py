import tkinter as tk

root = tk.Tk()  # tkinter root창 생성

root.title("계산기") #창 이름
root.geometry("500x500+200+200") # 창 크기, 가로 x 세로 + 창 출력 위치 좌표

label1 = tk.Label(root, text = "과일 1개 선택")
label1.pack()

'''
라디오버튼은 여러개 항목중에서 1개만 선택하게 하는 것
ex) 답안지 선택
'''
fruit_var =tk.IntVar() #라디오 버튼 해당하는 그룹 항목 설정, value를 int형으로 저장
button_fruit1 = tk.Radiobutton(root, text="사과", value=1, variable=fruit_var)
button_fruit2 = tk.Radiobutton(root, text="바나나", value=2, variable=fruit_var)
button_fruit3 = tk.Radiobutton(root, text="딸기", value=3, variable=fruit_var)
button_fruit4 = tk.Radiobutton(root, text="귤", value=4, variable=fruit_var)

button_fruit1.pack()
button_fruit2.pack()
button_fruit3.pack()
button_fruit4.pack()

tk.Label(root, text="음료 선택").pack()

drink_var = tk.StringVar()
button_drink1 = tk.Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
button_drink1.select() # 기본값 선택
button_drink2 = tk.Radiobutton(root, text="환타", value="환타", variable=drink_var)

button_drink1.pack()
button_drink2.pack()

def button_command():
   print(fruit_var.get())  # 과일 중 선택된 라디오 항목의 value 출력
   print(drink_var.get())

button = tk.Button(root, text="과일 선택", command=button_command)
button.pack()


root.mainloop()