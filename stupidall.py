import string, random, time, os


class sprint:
    def __init__(self, text):
        symbols = string.printable
        output = ''
        for i in text:
            while True:
                rch = random.choice(symbols)
                output += rch
                print(output, end='\r', flush=True)
                time.sleep(0.05)
                if rch == i:
                    break
                else:
                    output = output[:-1]
                    os.system('cls')
                     
        print(output)