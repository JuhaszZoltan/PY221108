magassag:float = float(input('add meg a magasságod (cm): ')) / 100
testtomeg:float = float(input('add meg a testtömeged (Kg): '))

tii:float = testtomeg / magassag ** 2
tso:str = '-'

if tii < 16: tso = 'súlyos soványság'
elif tii < 17: tso = 'mérsékelt soványság'
elif tti < 18.5: tso = 'enyhe soványság'
elif tti < 25: tso = 'normális testsúly'
elif tti < 30: tso = 'túlsúlyos'
elif tti < 35: tso = 'I. fokú elhízás'
elif tti < 40: tso = 'II. fokú elhízás'
else: tso = 'III. fokú (súlyos) elhízás'

print(f'testsúlyosztályod: {tso} (tti = {round(tti, 2)})')