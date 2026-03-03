"""Fungsi utama konversi angka ke terbilang."""

SATUAN = [
    "", "satu", "dua", "tiga", "empat", "lima",
    "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas",
]

TINGKAT = [
    (1_000_000_000_000, "triliun"),
    (1_000_000_000, "miliar"),
    (1_000_000, "juta"),
    (1_000, "ribu"),
]


def terbilang(n: int) -> str:
    """Konversi bilangan bulat menjadi string terbilang Bahasa Indonesia.

    Args:
        n: Bilangan bulat (positif, negatif, atau nol).

    Returns:
        String terbilang dalam Bahasa Indonesia.

    Raises:
        TypeError: Jika input bukan integer.

    Examples:
        >>> terbilang(0)
        'nol'
        >>> terbilang(11)
        'sebelas'
        >>> terbilang(1000)
        'seribu'
        >>> terbilang(1_500_000)
        'satu juta lima ratus ribu'
    """
    if not isinstance(n, int):
        raise TypeError(f"Input harus bertipe int, diterima {type(n).__name__}")

    if n < 0:
        return "minus " + terbilang(-n)

    if n == 0:
        return "nol"

    return _konversi(n).strip()


def _konversi(n: int) -> str:
    if n == 0:
        return ""

    if n < 12:
        return SATUAN[n]

    if n < 20:
        return SATUAN[n - 10] + " belas"

    if n < 100:
        puluhan = n // 10
        sisa = n % 10
        return SATUAN[puluhan] + " puluh" + (" " + SATUAN[sisa] if sisa else "")

    if n < 1000:
        ratusan = n // 100
        sisa = n % 100
        awalan = "seratus" if ratusan == 1 else SATUAN[ratusan] + " ratus"
        return awalan + (" " + _konversi(sisa) if sisa else "")

    for batas, label in TINGKAT:
        if n >= batas:
            bagian = n // batas
            sisa = n % batas
            if bagian == 1 and label == "ribu":
                awalan = "seribu"
            else:
                awalan = _konversi(bagian) + " " + label
            return awalan + (" " + _konversi(sisa) if sisa else "")

    return ""
