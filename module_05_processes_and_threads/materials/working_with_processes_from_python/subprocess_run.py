import subprocess


def run_program():
    res = subprocess.run(['python3', 'test_program.py'], input=b'some input\notherinput')
    print(res)

if __name__ == '__main__':
    run_program()
