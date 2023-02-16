class Validator:
    
    def get_int_number(string):
        result = 0
        try:
            result = int(string)
        except ValueError:
            print('Could convert to int, try via float:')
            result = int(float(string))
        return result
        
if __name__ == "__main__":
    print(Validator.get_int_number('10.'))
    try:
        user_input = 'aaa'
        Validator.get_int_number(user_input)
    except ValueError:
        print(f'{user_input} is not a number, please enter proper data')
    except Exception as e:
        print(f'Unknow error ask developers {e}')
