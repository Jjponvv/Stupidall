import string, random, time, os


class sprint:
    def __init__(self, text=str, speed=0.01):
        symbols = string.printable
        output = ''
        for i in text:
            while True:
                rch = random.choice(symbols)
                output += rch
                print(output, end='\r', flush=True)
                time.sleep(speed)
                if rch == i:
                    break
                else:
                    output = output[:-1]
                    os.system('clear')
                     
        print(output)