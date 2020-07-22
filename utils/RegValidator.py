from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QValidator


class QRV(QRegExpValidator):
    def __init__(self, reg_exp_str=r'^(0|[1-9]\d*)([.,]\d+)?'):
        super().__init__(QRegExp(reg_exp_str))

    def validate(self, text, pos):
        res, s, i = super().validate(text, pos)
        s = self.fixup(text) if res != QValidator.Acceptable else s
        return res, s, i

    def fixup(self, s):
        s = s.replace(',', '.') if ',' in s else s
        return s