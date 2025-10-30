# askcolor.py
# 일반적인 색상(색상은 각 (빨간색, 녹색, 파란색) 성분의 양을 숫자로 지정해 섞인 색을 나타냄. 일반적으로 0~255 사이. 모두 0이면 검정)
import tkinter as tk
from tkinter import colorchooser

color = colorchooser.askcolor(title="색상 선택")
print(color)