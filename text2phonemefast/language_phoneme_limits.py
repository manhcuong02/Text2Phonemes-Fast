"""
Configuration file that defines maximum phoneme token lengths for different languages.

These limits are used when generating phoneme sequences to ensure the model output
doesn't exceed the expected length for each language.
"""

# Maximum number of tokens to generate for each language's phoneme sequence
MAX_PHONEME_LENGTHS = {
    "msa.tsv": 27,
    "amh.tsv": 28,
    "urd.tsv": 152,
    "mri.tsv": 30,
    "glg.tsv": 22,
    "swa.tsv": 28,
    "est.tsv": 47,
    "hbs-latn.tsv": 31,
    "spa.tsv": 28,
    "pol.tsv": 38,
    "spa-latin.tsv": 24,
    "fra.tsv": 43,
    "uig.tsv": 33,
    "aze.tsv": 34,
    "nob.tsv": 52,
    "swe.tsv": 36,
    "por-bz.tsv": 28,
    "arg.tsv": 30,
    "yue.tsv": 227,
    "sqi.tsv": 42,
    "cat.tsv": 27,
    "hbs-cyrl.tsv": 31,
    "grc.tsv": 39,
    "bak.tsv": 44,
    "hun.tsv": 67,
    "lat-clas.tsv": 61,
    "ita.tsv": 37,
    "san.tsv": 38,
    "arm-w.tsv": 41,
    "afr.tsv": 81,
    "ind.tsv": 87,
    "sme.tsv": 31,
    "egy.tsv": 22,
    "rus.tsv": 62,
    "ady.tsv": 29,
    "epo.tsv": 43,
    "srp.tsv": 42,
    "zho-t.tsv": 135,
    "tha.tsv": 295,
    "vie-c.tsv": 184,
    "kur.tsv": 37,
    "ice.tsv": 37,
    "geo.tsv": 75,
    "cze.tsv": 43,
    "ara.tsv": 370,
    "tgl.tsv": 27,
    "nan.tsv": 175,
    "por-po.tsv": 35,
    "bos.tsv": 52,
    "enm.tsv": 24,
    "ltz.tsv": 55,
    "ina.tsv": 26,
    "ukr.tsv": 39,
    "mac.tsv": 44,
    "kaz.tsv": 44,
    "slk.tsv": 73,
    "ang.tsv": 33,
    "khm.tsv": 47,
    "syc.tsv": 24,
    "eus.tsv": 35,
    "spa-me.tsv": 28,
    "tts.tsv": 26,
    "gle.tsv": 36,
    "slv.tsv": 35,
    "ido.tsv": 23,
    "zho-s.tsv": 135,
    "vie-n.tsv": 174,
    "gre.tsv": 20,
    "eng-us.tsv": 119,
    "fin.tsv": 44,
    "pap.tsv": 26,
    "tuk.tsv": 49,
    "jpn.tsv": 174,
    "bel.tsv": 58,
    "uzb.tsv": 36,
    "dan.tsv": 42,
    "ori.tsv": 45,
    "ron.tsv": 30,
    "bul.tsv": 40,
    "bur.tsv": 52,
    "lit.tsv": 87,
    "dut.tsv": 48,
    "fra-qu.tsv": 255,
    "eng-uk.tsv": 129,
    "hin.tsv": 110,
    "isl.tsv": 41,
    "arm-e.tsv": 38,
    "kor.tsv": 175,
    "tur.tsv": 54,
    "fas.tsv": 70,
    "ger.tsv": 56,
    "tam.tsv": 38,
    "wel-sw.tsv": 44,
    "vie-s.tsv": 172,
    "mlt.tsv": 47,
    "wel-nw.tsv": 49,
    "slo.tsv": 27,
    "lat-eccl.tsv": 43,
    "snd.tsv": 60,
    "tat.tsv": 103,
    "alb.tsv": 40,
    "hau.tsv": 45,
    "pus.tsv": 34,
    "tib.tsv": 61,
    "sga.tsv": 47,
    "heb.tsv": 39,
    "hrx.tsv": 27,
    "fao.tsv": 42,
    "dsb.tsv": 29,
}

# Default value to use when a language is not found in the dictionary
DEFAULT_MAX_PHONEME_LENGTH = 50
