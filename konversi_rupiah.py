import locale

def KonversiRupiah(angka, prefix=False, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if prefix:
        return format(rupiah)
    return rupiah
