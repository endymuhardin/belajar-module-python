"""Unit tests untuk modul terbilang."""

import pytest

from terbilang import terbilang


class TestTerbilangSatuan:
    def test_nol(self):
        assert terbilang(0) == "nol"

    def test_satu(self):
        assert terbilang(1) == "satu"

    def test_sebelas(self):
        assert terbilang(11) == "sebelas"


class TestTerbilangBelasan:
    def test_dua_belas(self):
        assert terbilang(12) == "dua belas"

    def test_sembilan_belas(self):
        assert terbilang(19) == "sembilan belas"


class TestTerbilangPuluhan:
    def test_dua_puluh(self):
        assert terbilang(20) == "dua puluh"

    def test_dua_puluh_lima(self):
        assert terbilang(25) == "dua puluh lima"

    def test_sembilan_puluh_sembilan(self):
        assert terbilang(99) == "sembilan puluh sembilan"


class TestTerbilangRatusan:
    def test_seratus(self):
        assert terbilang(100) == "seratus"

    def test_dua_ratus_lima_puluh(self):
        assert terbilang(250) == "dua ratus lima puluh"

    def test_sembilan_ratus_sembilan_puluh_sembilan(self):
        assert terbilang(999) == "sembilan ratus sembilan puluh sembilan"


class TestTerbilangRibuan:
    def test_seribu(self):
        assert terbilang(1000) == "seribu"

    def test_dua_ribu_lima_ratus(self):
        assert terbilang(2500) == "dua ribu lima ratus"

    def test_sepuluh_ribu(self):
        assert terbilang(10_000) == "sepuluh ribu"


class TestTerbilangBesar:
    def test_satu_juta(self):
        assert terbilang(1_000_000) == "satu juta"

    def test_satu_juta_lima_ratus_ribu(self):
        assert terbilang(1_500_000) == "satu juta lima ratus ribu"

    def test_satu_miliar(self):
        assert terbilang(1_000_000_000) == "satu miliar"

    def test_satu_triliun(self):
        assert terbilang(1_000_000_000_000) == "satu triliun"


class TestTerbilangNegatif:
    def test_minus_satu(self):
        assert terbilang(-1) == "minus satu"

    def test_minus_seribu(self):
        assert terbilang(-1000) == "minus seribu"


class TestTerbilangError:
    def test_input_float_raises_type_error(self):
        with pytest.raises(TypeError):
            terbilang(3.14)

    def test_input_string_raises_type_error(self):
        with pytest.raises(TypeError):
            terbilang("123")
