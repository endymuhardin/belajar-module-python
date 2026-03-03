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

## Menggunakan di Project Lain

### Dengan `requirements.txt`

Tambahkan baris berikut di `requirements.txt`:

```
terbilang @ git+https://github.com/endymuhardin/terbilang.git
```

Untuk pin ke commit atau tag tertentu:

```
terbilang @ git+https://github.com/endymuhardin/terbilang.git@v0.1.0
terbilang @ git+https://github.com/endymuhardin/terbilang.git@main
terbilang @ git+https://github.com/endymuhardin/terbilang.git@abc1234
```

Lalu install:

```bash
pip install -r requirements.txt
```

### Dengan `pyproject.toml`

Tambahkan di bagian `[project]` → `dependencies`:

```toml
[project]
dependencies = [
    "terbilang @ git+https://github.com/endymuhardin/terbilang.git",
]
```

Untuk pin ke tag tertentu:

```toml
[project]
dependencies = [
    "terbilang @ git+https://github.com/endymuhardin/terbilang.git@v0.1.0",
]
```

Lalu install project:

```bash
pip install .
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
