import input
import calculat
import view

def button():
    value_a = input.input_digit()
    value_b = input.input_digit()
    oper = input.input_oper()
    result = calculat.calculation(value_a, value_b, oper)
    view.print_result(value_a, oper, value_b, result)

