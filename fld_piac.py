arlista:str = '''
=====árlista=====
banán  1250 Ft/Kg
alma    530 Ft/Kg
körte   800 Ft/Kg
'''
print(arlista)
kerdes:str = 'Jó reggelt, szeretnél valamit vásárolni? '
ossz_ar:int = 0

while input(kerdes) == 'igen':
    termek:str = input('mit szeretnél? ')
    if termek in {'banán', 'alma', 'körte'}:
        mennyiseg:float = float(input(f'hány Kg {termek}-t szeretnél? '))
        if termek == 'alma': ossz_ar += 530 * mennyiseg
        elif termek == 'banán': ossz_ar += 1250 * mennyiseg
        elif termek == 'körte': ossz_ar += 800 * mennyiseg
    else: print(f'sajnos {termek} nincs :(')
    kerdes = 'szeretnél még valamit vásárolni? '
print(f'rendben, összesen {ossz_ar} Ft-ot kérnék!')


















# árlista
# ismétlés, amíg szeretnék vásárolni
    # szeretnék-e vásárolni?
    # igen -> mit?
    # in árlista -> mennyit?
# kiírja a végösszeget


