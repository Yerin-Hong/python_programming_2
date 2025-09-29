# 예제 3
Label(root, text = "이름").pack()     # 레이블 참조 변수는 필요하지 않음.

entry_name = Entry(root)
entry_name.pack()

Label(root, text = "나이").pack()       # 레이블 참조 변수는 필요하지 않음.
entry_age.pack()

entry_age.pack()
button_submit = Button(root, text = "제출", command = submit)
button_submit.pack()

root.mainloop()