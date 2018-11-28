import sys
if sys.platform.startswith('win'):
    import ctypes
    STD_INPUT_HANDLE = -10  
    STD_OUTPUT_HANDLE= -11  
    STD_ERROR_HANDLE = -12  
    
    FOREGROUND_DARKBLUE = 0x01
    FOREGROUND_DARKGREEN = 0x02
    FOREGROUND_DARKSKYBLUE = 0x03
    FOREGROUND_DARKRED = 0x04 
    FOREGROUND_DARKPINK = 0x05 
    FOREGROUND_DARKYELLOW = 0x06
    FOREGROUND_DARKWHITE = 0x07 
    FOREGROUND_DARKGRAY = 0x08 
    FOREGROUND_BLUE = 0x09 
    FOREGROUND_GREEN = 0x0a
    FOREGROUND_SKYBLUE = 0x0b
    FOREGROUND_RED = 0x0c
    FOREGROUND_PINK = 0x0d
    FOREGROUND_YELLOW = 0x0e
    FOREGROUND_WHITE = 0x0f
    std_out_handle=ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    
    def set_cmd_text_color(color, handle=std_out_handle):
        Bool=ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return Bool
    
    def resetColor():
        set_cmd_text_color(FOREGROUND_DARKWHITE)
    
    def ccprint(mess,color):
        if color=='darkblue':
            set_cmd_text_color(FOREGROUND_DARKBLUE)
    
        # elif color=='DARKGREEN':
        #     set_cmd_text_color(FOREGROUND_DARKGREEN)
    
        # elif color=='DARKSKYBLUE':
        #     set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
            
        # elif color=='DARKRED':
        #     set_cmd_text_color(FOREGROUND_DARKRED)
    
        # elif color=='DARKPINK':
        #     set_cmd_text_color(FOREGROUND_DARKPINK)
            
        # elif color=='DARKYELLOW':
        #     set_cmd_text_color(FOREGROUND_DARKYELLOW)
    
        # elif color=='DARKWHITE':
        #     set_cmd_text_color(FOREGROUND_DARKWHITE)
    
        # elif color=='DARKGRAY':
        #     set_cmd_text_color(FOREGROUND_DARKGRAY)
    
        elif color=='blue':
            set_cmd_text_color(FOREGROUND_BLUE)
    
        elif color=='green':
            set_cmd_text_color(FOREGROUND_GREEN)
    
        elif color=='cyan':
            set_cmd_text_color(FOREGROUND_SKYBLUE)
    
        elif color=='red':
            set_cmd_text_color(FOREGROUND_RED)
    
        elif color=='magenta':
            set_cmd_text_color(FOREGROUND_PINK)
    
        elif color=='yellow':
            set_cmd_text_color(FOREGROUND_YELLOW)
    
        elif color=='white':
            set_cmd_text_color(FOREGROUND_WHITE)
            
        print(mess)
        resetColor()
    def llprint(mess,color):
        if color=='darkblue':
            set_cmd_text_color(FOREGROUND_DARKBLUE)
    
        # elif color=='DARKGREEN':
        #     set_cmd_text_color(FOREGROUND_DARKGREEN)
    
        # elif color=='DARKSKYBLUE':
        #     set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
            
        # elif color=='DARKRED':
        #     set_cmd_text_color(FOREGROUND_DARKRED)
    
        # elif color=='DARKPINK':
        #     set_cmd_text_color(FOREGROUND_DARKPINK)
            
        # elif color=='DARKYELLOW':
        #     set_cmd_text_color(FOREGROUND_DARKYELLOW)
    
        # elif color=='DARKWHITE':
        #     set_cmd_text_color(FOREGROUND_DARKWHITE)
    
        # elif color=='DARKGRAY':
        #     set_cmd_text_color(FOREGROUND_DARKGRAY)
    
        elif color=='blue':
            set_cmd_text_color(FOREGROUND_BLUE)
    
        elif color=='green':
            set_cmd_text_color(FOREGROUND_GREEN)
    
        elif color=='cyan':
            set_cmd_text_color(FOREGROUND_SKYBLUE)
    
        elif color=='red':
            set_cmd_text_color(FOREGROUND_RED)
    
        elif color=='magenta':
            set_cmd_text_color(FOREGROUND_PINK)
    
        elif color=='yellow':
            set_cmd_text_color(FOREGROUND_YELLOW)
    
        elif color=='white':
            set_cmd_text_color(FOREGROUND_WHITE)
            
        print(mess, end=' ')
        resetColor()
else:
    from termcolor import colored
    def ccprint(msg,color):
        text=colored(text=msg,color=color)
        print(text)
    def llprint(msg,color):
        text=colored(text=msg,color=color)
        print(text, end=' ')

def cprint(msg,color):
    ccprint(msg,color)
def lprint(msg,color):
    llprint(msg,color)

    
    
if __name__=='__main__':
    while 1:
        mess=input('msg:')
        color=input('color:')
        cprint(mess,color)