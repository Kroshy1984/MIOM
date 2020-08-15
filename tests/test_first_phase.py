import math
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from core.FirstPhase import Inductor

import pytest

# from core.FirstPhase import Inductor, Form

# import core.FirstPhase
p2_form = dict()
p2_form["LBT"] = 30 * math.pow(10, -3)
p2_form["operation"] = "b1"
p2_form["DOT"] = 151.4 * math.pow(10, -3)
p2_form["ST"] = 1.2 * math.pow(10, -3)
# p2_form["FW"] = self.FW
p2_form["YEMP"] = 7.1 * math.pow(10, -8)
p2_form["FCE"] = 24000
p2_form["LCE"] = 1.7 * math.pow(10, -7)
# p2_form["LCB"] = pow(10, -12)
p2_form["LCB"] = 0
p2_form["CCE"] = 0.000254
p2_form["SC"] = 0.65 * math.pow(10, -3)
p2_form["HSC"] = 8 * math.pow(10, -3)
p2_form["PLM"] = 2640
p2_form["BCM"] = 574000000
p2_form["KDM"] = 2.402
p2_form["MM"] = 0.23
p2_form["KPD"] = 0.03
p2_form["RC"] = 73.95 * math.pow(10, -3)
p2_form["NCT1"] = 11
p2_form["ZS"] = 0.00065
p2_form["ZB"] = 1 * math.pow(10, -3)
p2_form["ZA"] = 0.25 * math.pow(10, -3)
p2_form["YEMC"] = 1.78 * math.pow(10, -8)
p2_form["LTC"] = 0.07 * math.pow(10, -6)

inductor = Inductor()

inductor.set_data_from_dict(p2_form)
inductor.calculate_inductor_parameters()

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_LDC():
    assert inductor.LDC == 2.4 * math.pow(10, -7)

def test_WR():
    assert inductor.WR == 8191.592

def test_PM():
    assert inductor.PM == 3.96 * math.pow(10, 7)

def test_VCR():
    assert inductor.VCR == 0

def test_K1():
    assert inductor.K1 == 0.9235289
def test_K2():
    assert inductor.K2 == 0.3608642
def test_K3():
    assert inductor.K3 == 0.8681005
def test_K4():
    assert inductor.K4 == 0.9335578

def test_ZEK():
    assert inductor.ZEK == 0.003240606
def test_FW():
    assert round(inductor.FW, 2) == 12496.37
def test_ZCP():
    assert inductor.ZCP == 0.0019
def test_DCA():
    assert inductor.DCA == 0.1552
def test_YEMC():
    assert inductor.YEMC == 1.78e-08
    # assert inductor.LDC == 2.3 * math.pow(10, -7)

