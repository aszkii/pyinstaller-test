
import sys
import random

def generate_random_number_as_exit_code() -> int:
    ret = random.randint(0, 255)
    print('Number {} was generated.'.format(ret))
    return ret

if __name__ == '__main__':
    random_number = generate_random_number_as_exit_code()
    sys.exit(random_number)
