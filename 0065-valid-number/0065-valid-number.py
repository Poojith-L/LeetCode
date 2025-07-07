class Solution:
    def isNumber(self, s: str) -> bool:
        if s in {"inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity", "nan"}:
            return False
        try:
            int(s)
            return True
        except ValueError:
            try:
                float(s)
                return True
            except ValueError:
                return False
