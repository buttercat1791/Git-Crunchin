import re


class Redactor:
    ad_regexes: dict[str, str] = {
        'aquinas_wealth_start': r'(?i)this\s+episode\s+is\s+sponsored\s+by\s+\bAquinas\s+Wealth\s+Advisors\b',
        'aquinas_wealth_end': r'(?i)Aquinas\s+Wealth\s+Advisors\s+a\s+registered\s+investment\s+advisor\s+with\s+the\s+Securities\s+and\s+Exchange\s+Commission[.]?\s+',
        'pilgrimage_start': r'(?i)hey\s+guys[.,;]?\s+Patrick\s+here\s+with\s+a\s+pretty\s+exciting\s+announcement\s+',
        'pilgirmage_end': r'(?i)now[.,;]?\s+back\s+to\s+the\s+episode\s+[,;]?guys[.,;]?\s+yeah[.]?\s+',
    }
