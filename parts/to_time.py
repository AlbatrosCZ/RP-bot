def time_to_text(time, maximal = 1):
    days = ((time/60)/60)//24
    hours = (time/60)//60 - days*24
    minuts = time//60 - (days*24 + hours)*60
    secunds = time//1 - ((days*24 + hours)*60 + minuts)*60
    ret = ''
    if days != 0 and maximal <= 4:
        if days == 1:
            ret += 'day '
        else:
            ret += '{} days '.format(int(days)) 
    if hours != 0 and maximal <= 3:
        if hours == 1:
            ret += 'hour '
        else:
            ret += '{} hours '.format(int(hours)) 
    if minuts != 0 and maximal <= 2:
        if minuts == 1:
            ret += 'minut '
        else:
            ret += '{} minuts '.format(int(minuts)) 
    if secunds != 0 and maximal == 1:
        if ret != '':
            ret += 'and '
        if secunds == 1:
            ret += 'secund'
        else:
            ret += '{} secunds'.format(int(secunds)) 
    if ret == '':
        if maximal == 2:
            ret = 'méně než minutu'
        elif maximal == 3:
            ret = 'méně než hodinu'
        elif maximal == 4:
            ret = 'méně než den'
    return ret 