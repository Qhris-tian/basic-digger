import os

def main():
    my_value = os.getenv('MY_ENV_VAR', 'Default Value')
    print(f'The value of MY_ENV_VAR is: {my_value}')

if __name__ == "__main__":
    main()
