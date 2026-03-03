# terbilang

Konversi angka menjadi teks terbilang dalam Bahasa Indonesia.

## Instalasi

```bash
pip install terbilang
```

Atau install langsung dari repository:

```bash
pip install git+https://github.com/endymuhardin/terbilang.git
```

## Penggunaan

```python
from terbilang import terbilang

print(terbilang(0))          # nol
print(terbilang(11))         # sebelas
print(terbilang(1000))       # seribu
print(terbilang(1_500_000))  # satu juta lima ratus ribu
print(terbilang(-42))        # minus empat puluh dua
```

## Development

### Setup environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Jalankan test

```bash
pytest
```

## Lisensi

Apache-2.0
