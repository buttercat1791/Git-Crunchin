import re
from re import Match
from re import Pattern
from typing import AnyStr


class Redactor:
    ad_list: list[tuple[str, str]] = [
        ('aquinas_wealth_start', 'aquinas_wealth_end'),
        ('pilgrimage_start', 'pilgrimage_end'),
    ]

    ad_regexes: dict[str, Pattern] = {
        'aquinas_wealth_start': re.compile(r'(?i)this\s+episode\s+is\s+sponsored\s+by\s+\bAquinas\s+Wealth\s+Advisors\b'),
        'aquinas_wealth_end': re.compile(r'(?i)Aquinas\s+Wealth\s+Advisors\s+a\s+registered\s+investment\s+advisor\s+with\s+the\s+Securities\s+and\s+Exchange\s+Commission[.]?\s+'),
        'pilgrimage_start': re.compile(r'(?i)hey\s+guys[.,;]?\s+Patrick\s+here\s+with\s+a\s+pretty\s+exciting\s+announcement\s+'),
        'pilgrimage_end': re.compile(r'(?i)now[.,;]?\s+back\s+to\s+the\s+episode\s+[,;]?guys[.,;]?\s+yeah[.]?\s+'),
    }

    def remove_ads(self, transcript: str) -> str:
        """Removes known ads from a given podcast episode transcript.

        Args:
            transcript (str): The text to be processed.

        Returns:
            str: The input text with the ads removed.
        """
        processed_text = transcript

        for ad in self.ad_list:
            start_match: Match = self.ad_regexes[ad[0]].search(processed_text)
            end_match: Match = self.ad_regexes[ad[1]].search(processed_text)

            if start_match and end_match:
                processed_text = processed_text[:start_match.start()] + processed_text[end_match.end():]
        
        return processed_text
