from datetime import datetime as dt

def logger_modul(digit1, digit2, oper, result):
    time = dt.now().strftime('%d.%m.%Y, %H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time}, {digit1} {oper} {digit2} = {result}\n')
    
