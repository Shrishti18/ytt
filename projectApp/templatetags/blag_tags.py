from django import template
from datetime import datetime


register = template.Library()


@register.filter
def make(some_list):
    try:
        return some_list.split()
    except:
        return ''

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def cutt(some_list):
    search_list=[]
    new_list=[]
    for i in range(len(some_list)):
        if some_list[i]=='-->':
            search_list.append(some_list[i-1])
            search_list.append(some_list[i+1])
            search_list.append(some_list[i])
    for e in some_list:
        if e not in(search_list):
            new_list.append(e)
    
    str1 = ""
 
    # traverse in the string
    for ele in new_list:
        str1 += ele
        str1+=" "
 
    # return string
    return str1        


@register.filter
def find_pos(some_list,val):
    try:
        for i in range(len(some_list)):
            if some_list[i]==val:
                return i
                break

    except:
        return 0

@register.filter
def next(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) + 1] # access the next element
    except:
        return '' # return empty string in case of exception

@register.filter
def previous(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) - 1] # access the next element
    except:
        return '' # return empty string in case of exception

@register.filter
def previous_str(some_list, current_index):
    """
    Returns the previous element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        x= some_list[int(current_index) - 1]
        pt = datetime.strptime(x,'%M:%S.%f')
        total_seconds = pt.second + pt.minute*60
        if total_seconds==0:
          return 0
        else:
           return total_seconds-5
         # access the previous element
    except:
        return 0 # return empty string in case of exception

