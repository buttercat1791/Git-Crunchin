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
        'ad_start': re.compile(r'This\s+episode(\s+of\s+The\s+Crunch)?\s+is\s+sponsored\s+by'),
        'ad_end': re.compile(r'thank\s+you\s+to\s+([^ ]+)\s+for\s+sponsoring\s+this\s+episode(\s+of\s+The\s+Crunch)?'),
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
