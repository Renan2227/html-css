from time import sleep


def cronometro(tempo):
    if tempo > 0:
        min, seg = divmod(tempo, 60)
        frase = f'{min:02d}:{seg:02d}'
        print(frase, end='\r')
        sleep(1)
        cronometro(tempo - 1)
    else:
        print('o tempo acabou!')


cronometro(65)
