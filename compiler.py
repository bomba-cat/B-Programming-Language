import sys
import os
import tkinter as tk
import keyboard as key
import random
import math
from tkinter import filedialog as fd

filetype = {
    ('B+ files', '*.b')
}

_to_compile = fd.askopenfilename(filetypes=filetype)
#_to_compile = fr"C:\Users\bledi\Documents\Python\B+\compiler\file_example.b"
_syntax = ['out','var','str','func','if','ifn','endif','take','add','sub','mul','div','rand'] #add = addition, sub = subtraction, mul = multiplication, div = division for math
_syn = ['<<', '>>']
_out_output = ''
_out_var = ''
_skip = False
_vars = {
    'MATH.PI': math.pi,
    'MATH.random': random.randint(0,255),
    'MATH.dice': random.randint(1,6),
}
_func_tmp = []
_func_libary = {}
_func = False
_index = False

def check_func():
    global _func_tmp, _func_libary, _lines, _func, _index, func_name
    _lin = _lines.split()
    _w = _lines.split()[0]
    if _w != 'end':
        _func_tmp.append(_lin)
        _index = False
    else:
        for x in _func_tmp:
            _func_libary[_func_name] = x
            print(_func_libary)
        _func_tmp = []
        _func = False

def check_syntax():
    global _out_output, _out_var, _skip, _func_libary, _func_tmp, _func, _func_name, _lines, _index, _func_name
    _out_output = ''
    _word = _lines.split()[0]

    if _word in _func_libary:
        _index = True
        _IDX = _func_libary[_word]
        print(_IDX)

    if _word in _syntax:

        if _index == False:
            _IDX = _lines.split()

        if _word == 'out':
            _IDX.pop(0)
            for _idx in _IDX:
                if _idx not in _syn:
                    _out_output = _out_output + _idx + ' '
                    if _idx in _vars:
                        _out_var = _vars[_idx]
                if _idx in _syn:
                    if _idx == '<<':
                        print(_out_output)
                    elif _idx == '>>':
                        print(_out_var)
                    else:
                        print(r'Unexpected out Error; Press any Key to Continue the Programm anyways')
                        input('')

        if _word == 'var':
            _IDX.pop(0)
            _name = _IDX[0]
            _IDX.pop(0)
            _value = _IDX[0]
            _vars[_name] = int(_value)
            #print(_vars)

        if _word == 'take':
            _IDX.pop(0)
            _to_take_name = _IDX[0]
            _IDX.pop(0)
            _to_take_text = ''.join(str(_x) + ' ' for _x in _IDX)
            _to_take_var = input(_to_take_text)
            _vars[_to_take_name] = _to_take_var

        if _word == 'str':
            _IDX.pop(0)
            _name = _IDX[0]
            _IDX.pop(0)
            _value = ''.join(str(_x) + ' ' for _x in _IDX)
            _vars[_name] = _value
            #print(_vars)
        
        if _word == 'rand':
            _IDX.pop(0)
            _rand_name = _IDX[0]
            _IDX.pop(0)
            if _IDX[-1] in _syn:
                if _IDX[-1] == '<<':
                    _rand_min = _IDX[0]
                    _IDX.pop(0)
                    _rand_max = _IDX[0]
                    _rand_val = random.randint(int(_rand_min), int(_rand_max))
                    _vars[_rand_name] = _rand_val
                elif _IDX[-1] == '>>':
                    _rand_min = _IDX[0]
                    _IDX.pop(0)
                    _rand_max = _IDX[0]
                    _rand_val = random.randint(int(_vars[_rand_min]), int(_vars[_rand_max]))
                    _vars[_rand_name] = _rand_val

        if _word == 'if':
            _IDX.pop(0)
            _thing = _IDX[0]
            _IDX.pop(0)
            _condition = _IDX[0]
            _IDX.pop(0)
            if _vars[_thing] != _vars[_condition]:
                _skip = True
        
        if _word == 'ifn':
            _IDX.pop(0)
            _thing = _IDX[0]
            _IDX.pop(0)
            _condition = _IDX[0]
            _IDX.pop(0)
            if _vars[_thing] == _vars[_condition]:
                _skip = True

        if _word == 'add':
            _IDX.pop(0)
            _add_name = _IDX[0]
            _IDX.pop(0)
            _con_1 = _IDX[0]
            _IDX.pop(0)
            _con_2 = _IDX[0]
            _IDX.pop(0)
            if _IDX[-1] == '<<':
                _vars[_add_name] = _con_1 + _con_2
            elif _IDX[-1] == '>>':
                _vars[_add_name] = _vars[_con_1] + _vars[_con_2]
        
        if _word == 'sub':
            _IDX.pop(0)
            _add_name = _IDX[0]
            _IDX.pop(0)
            _con_1 = _IDX[0]
            _IDX.pop(0)
            _con_2 = _IDX[0]
            _IDX.pop(0)
            if _IDX[-1] == '<<':
                _vars[_add_name] = int(_con_1) - int(_con_2)
            elif _IDX[-1] == '>>':
                _vars[_add_name] = int(_vars[_con_1]) - int(_vars[_con_2])

        if _word == 'mul':
            _IDX.pop(0)
            _add_name = _IDX[0]
            _IDX.pop(0)
            _con_1 = _IDX[0]
            _IDX.pop(0)
            _con_2 = _IDX[0]
            _IDX.pop(0)
            if _IDX[-1] == '<<':
                _vars[_add_name] = int(_con_1) * int(_con_2)
            elif _IDX[-1] == '>>':
                _vars[_add_name] = int(_vars[_con_1]) * int(_vars[_con_2])

        if _word == 'div':
            _IDX.pop(0)
            _add_name = _IDX[0]
            _IDX.pop(0)
            _con_1 = _IDX[0]
            _IDX.pop(0)
            _con_2 = _IDX[0]
            _IDX.pop(0)
            if _IDX[-1] == '<<':
                _vars[_add_name] = int(_con_1) / int(_con_2)
            elif _IDX[-1] == '>>':
                _vars[_add_name] = int(_vars[_con_1]) / int(_vars[_con_2])

        if _word == 'func':
            _IDX.pop(0)
            _func_name = _IDX[0]
            _IDX.pop(0)
            _func = True

    else:
        if _word not in _func_libary:
            print(r"Error Exception '{No Accessible Syntax}'; Press any Key to Continue the Programm anyways" + _word + input(''))


with open(_to_compile, 'r') as _line:
    for _l in _line:
        #print(_l)
        if _l != '\n':
            if _skip == False:
                if _func == False:
                    _lines = ''
                    _lines = _l.strip('\n')
                    #print(_lines)
                    check_syntax()
                elif _func == True:
                    _lines = ''
                    _lines = _l.strip('\n')
                    check_func()
            elif _skip == True:
                _lines = ''
                _lines = _l.strip('\n')
                if _lines == 'endif':
                    _skip = False


#CHECK-LIST

#out = done
#var = done
#take = done
#str = done
#rand = done
#if and ifn = done
#add = done
#sub = done
#mul = done
#div = done
#func = W.I.P 75%