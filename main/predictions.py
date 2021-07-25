import pickle
def PuPhyMeritCal(yop, matric, fsc, et, deduction):
    puphyedsmodel = pickle.load(open('puPhEd.pkl', 'rb'))
    fsc = (fsc * 0.4)
    matric = (matric * 0.4)
    et = (et * 0.2)
    deduction = (2018 - yop) * 2;
    merit = fsc + matric + et - deduction
    puphyedsmodel = puphyedsmodel.predict([[yop, matric, fsc, et, deduction, merit]])
    return puphyedsmodel


# Prediction For BBA PU
def PuBBaMeritCal(yop, matric, fsc, et, deduction):
    puBbamodel = pickle.load(open('PuBBA.pkl', 'rb'))

    fsc = (fsc * 0.4)
    matric = (matric * 0.4)
    et = (et * 0.2)
    deduction = (2018 - yop) * 2
    merit = fsc + matric + et - deduction
    puBbamodel = puBbamodel.predict([[yop, matric, fsc, et, deduction, merit]])

    return puBbamodel

# Prediction For BBIT PU
def PUBBITMeritCal(yop, matric, fsc, et, deduction):
    #puitModel = pickle.load(open('PUBBIT.pkl', 'rb'))
    puitModel = pickle.load(open('PUBBIT.pkl','rb'))
    fsc = (fsc * 0.8)
    matric = (matric * 0.2)
    et=0
    deduction = (2019 - yop) * 2
    merit = (fsc + matric) - deduction
    puitModel = puitModel.predict([[yop, matric, fsc, et, merit]])
    return puitModel




# Prediction For Cs IBU Univeristy
def IbuCsMeritCal(yop, fsc, et, deduction):
    ibuCsmodel = pickle.load(open('IbuCs.pkl', 'rb'))
    fsc = (fsc * 0.8)
    et = (et * 0.2)
    deduction = (2018 - yop) * 2;
    merit = fsc + et - deduction
    ibuCsmodel = ibuCsmodel.predict([[yop, fsc, et, deduction, merit]])
    return ibuCsmodel


# Prediction For IBU University Commerce
def IbuCommMeritCal(yop, fsc, et, deduction):
    ibuCommModel = pickle.load(open('IbuComm.pkl', 'rb'))
    fsc = (fsc * 0.8)
    et = (et * 0.2)
    deduction = (2018 - yop) * 2;
    merit = fsc + et - deduction
    ibuCommModel = ibuCommModel.predict([[yop, fsc, et, deduction, merit]])
    return ibuCommModel