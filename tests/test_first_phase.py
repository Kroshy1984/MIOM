import math
import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from core.FirstPhase import Inductor

import pytest

# from core.FirstPhase import Inductor, Form

# import core.FirstPhase
p2_form = dict()
# p2_form["LBT"] = 35 * math.pow(10, -3)
p2_form["LBT"] = 0.035
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
p2_form["PYM"] = 1.65 * 10 ** 8
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
    assert round(inductor.WR, 3) == 8191.592


def test_PM():
    assert round(inductor.PM) == 39600000


def test_VCR():
    assert round(inductor.VCR, 4) == round(45.23029, 4)


def test_K1():
    assert round(inductor.K1, 7) == 0.9235289


def test_K2():
    assert round(inductor.K2, 7) == 0.3608642


def test_K3():
    assert round(inductor.K3, 7) == 0.8681005


def test_K4():
    assert round(inductor.K4, 7) == 0.9335578


# def test_ZEK():
#     assert inductor.ZEK == 0.003240606

def test_ZEK():
    # assert inductor.ZEK == 2.800422e-03
    assert round(inductor.ZEK, 9) == 3.240606e-03


def test_ZPR():
    assert round(inductor.ZPR, 9) == 3.240606e-03


def test_FW():
    assert round(inductor.FW, 2) == 12496.37


def test_ZCP():
    assert inductor.ZCP == 0.0019


def test_DCA():
    assert inductor.DCA == 0.1552


def test_YEMC():
    assert inductor.YEMC == 1.78e-08


def test_FDC():
    assert round(inductor.FDC, 2) == 20385.68


def test_LDC():
    assert inductor.LDC == 2.4e-07


def test_ZS():
    assert inductor.ZS == 0.00065


def test_ZB():
    assert inductor.ZB == 0.001


def test_ZA():
    assert inductor.ZA == 0.00025


def test_BC():
    # assert inductor.BC == 6.008445e-04
    assert round(inductor.BC, 10) == 8.945756e-04


def test_BP():
    # assert inductor.BP == 0.0012
    assert round(inductor.BP, 9) == 1.786637e-03


def test_SCIC():
    assert inductor.SCIC == 0.01


def test_LCA():
    assert inductor.LCA == 0.03


def test_NCT():
    assert inductor.NCT == 7


def test_SSC():
    assert inductor.SSC == 0.0087


def test_LBT():
    assert inductor.LBT == 0.035


def test_LCG():
    assert round(inductor.LU, 4) == 0.033


# def test_NCWC():
#     assert inductor.NCWC == -1


# def test_NCFC():
#     assert inductor.NCF == -2


def test_NCW():
    assert inductor.NCW == 7


# def test_NCTC():
#     assert round(inductor.NCTC, 6) == 2.640996


def test_ESP():
    assert round(inductor.f.EPS, 7) == 0.0074375  # 0.007437468


def test_SUMP():
    assert round(inductor.SUMP, 8) == 1.589199e-02


def test_WYD():
    assert inductor.f.WYD == 2700428


def test_BCMD():
    assert inductor.f.BCMD == 1.378748e+09


def test_FR():
    assert round(inductor.FR, 2) == round(5637.337, 2)


def test_ALFA():
    assert round(inductor.ALFA, 7) == 0.2126289


def test_LP():
    assert round(inductor.LP, 13) == 2.264635e-07


def test_RP():
    assert round(inductor.RP, 10) == 5.272654e-04


def test_QP():
    assert round(inductor.QP, 5) == 15.21231


def test_KZ():
    assert round(inductor.KZ, 7) == 0.6333333

def test_RC():
    assert round(inductor.RC_ind, 9) == round(4.695141e-04, 9)

def test_M():
    assert inductor.M == 0

def test_QQ():
    assert round(inductor.QQ, 4) == 231.4145

def test_LK():
    assert round(inductor.LK, 5) == 16.46998
def test_MAP():
    assert round(inductor.MAP, 20) == 4.935885e-14
# def test_ZEK():
#     assert inductor.ZEK ==
# assert inductor.LDC == 2.3 * math.pow(10, -7)