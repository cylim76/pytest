import time
import  os

# 字符点阵
dict = {

'a' : [[0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'b' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]],
'c' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'd' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0]],
'e' : [[1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
'f' : [[1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
'g' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0]],
'h' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'i' : [[0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0]],
'j' : [[0, 0, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0],
     [1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0]],
'k' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0]],
'l' : [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
'm' : [[1, 0, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'n' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'o' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'p' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
'q' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0],
     [1, 0, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0]],
'r' : [[1, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0]],
's' : [[0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
't' : [[1, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
'u' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
'v' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0],
     [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0]],
'w': [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0],
     [1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 0]],
'x' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0]],
'y' : [[1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
'z' : [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
' ': [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
'.' : [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]],
'?' : [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
}


screen_width = int(input('input screen width(1-10)  :'))
# speed = int(input('input moving speed (1-100)  :'))
text = input('input words :')

# 列表重新排序成输出格式, 是整个句子的点阵
str_list = [dict.get(alpha) for alpha in text]




def get_in_out_char(str_list,in_out_position):         # in_out_position 指针指向进入屏幕的字符index
     in_out_char = [str_list[in_out_position]]         # 根据指针截取进出屏幕的字符
     return in_out_char

def sliced_char_l_half(in_out_char, width):            #字符切片获取左半部（进入屏幕）
     l_half_char =[[]]
     for height in range(0,7):
          tmp = in_out_char[0][height][:width]  # in_out_char  进来的是包含一个字符的列表， 所以索引第[0]个字符
          l_half_char[0].append(tmp)
     return l_half_char

def sliced_char_r_half(in_out_char, width):            #字符切片获取右半部（走出屏幕）
     r_half_char =[[]]
     for height in range(0,7):
          tmp = in_out_char[0][height][width:]
          r_half_char[0].append(tmp)
     return r_half_char     

def before_in_char(str_list, start, in_out_position):  #屏幕中间的完整字符
     before_char = str_list[start:in_out_position]
     return before_char

def screen_clear():
     if os.name == 'nt':
          os.system('cls')
     elif os.name =='posix':
          os.system('clear')     

def prtstars(str_prt):
     time.sleep(5 /100 )
     screen_clear()     
     print('\n\n')
     

     for height in range(len(str_prt[0])):   # 按行遍历
          for i in range(0,len(str_prt)):              #遍历 str_prt 列表中的item 
               for width in range(0,len(str_prt[i][height])):  #按列遍历
                    if str_prt[i][height][width]  == 1:
                         print("* ", end = "")
                    if str_prt[i][height][width] == 0:
                         print("  ", end = "")
          print()   # 每打印一行换行



def get_screen_list(str_list,screen_width):
     empty_list = [dict.get(' ') for i in range(0,screen_width + 1)]
     # 直接给字符前后加上屏幕宽度的空格，就可以实现渐进渐出效果,hehe..
     str_list = empty_list + str_list + empty_list

     for in_out_position in range(0,len(str_list)): # 指针遍历字符串点阵
          for width in range(1,7): #每个字遍历循环切片6次
               str_prt =[]

               if in_out_position < screen_width and in_out_position == 0: # 第一个字符进入画面
                    tmp = get_in_out_char(str_list,in_out_position)           #进入画面的字符
                    char_end = sliced_char_l_half(tmp, width)             # 进入画面的字符的左半部的列表
                    str_prt =  char_end
                    prtstars(str_prt)

               elif in_out_position < screen_width and in_out_position >= 1: #进入画面的字符 >= 1个,且小于屏幕宽度时, 已进入字符+进入字符左半部
                    char_body = before_in_char(str_list,0, in_out_position) # 已经进入的整字字符
                    tmp = get_in_out_char(str_list,in_out_position)             # 正在进入的字符
                    char_end = sliced_char_l_half(tmp, width)               # 正在进入的字符的左半部
                    str_prt =  char_body + char_end
                    prtstars(str_prt)

               elif in_out_position >= screen_width and in_out_position < len(str_list)-1:                             #进入画面的字符数大于屏幕宽度,需要同时切片屏幕左侧和右侧字符
                    head_tmp = get_in_out_char(str_list,in_out_position-screen_width)    #左侧出画面的字符
                    char_head = sliced_char_r_half(head_tmp, width)                  #左侧出画面字符的 右半部
                    char_body = before_in_char(str_list, in_out_position - screen_width + 1,in_out_position) # 中间字符
                    end_tmp = get_in_out_char(str_list,in_out_position)                 # 右侧进入画面的字符
                    char_end = sliced_char_l_half(end_tmp, width)                   # 右侧进入画面的字符的左半部
                    if width < 6:
                         str_prt= char_head + char_body + char_end
                    elif width == 6:
                         str_prt= char_body + char_end
                    prtstars(str_prt)












while True:
     # 参数： 字符串 ， 屏幕宽度，
     # screen_width = 8 
     get_screen_list(str_list,screen_width)  #

     


