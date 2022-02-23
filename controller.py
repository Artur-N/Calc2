import input
import calculat
import view
import logger

def button():
    value_a = input.input_digit()
    oper = input.input_oper()
    value_b = input.input_digit()
    result = calculat.calculation(value_a, value_b, oper)
    view.print_result(value_a, oper, value_b, result)
    logger.logger_modul(value_a, value_b, oper, result)
