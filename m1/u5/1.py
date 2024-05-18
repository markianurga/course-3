class My_success():
    def __init__(self,value):
        self.value_of_success = value
    def check_success(self):
        if rate > 4.0:
            return 'Запуск стартапу пройшов успішно'
        elif self.value_of_success < 4.0 and self.value_of_success >= 3.0:
            return 'Запуск стартапу пройшов непогано'
        return 'Проект потребує доопрацювання'
rate = float(input('Рейтинг програми'))
object = My_success(rate)
print(object.check_success())
