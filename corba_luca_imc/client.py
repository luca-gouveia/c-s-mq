import sys
from omniORB import CORBA
import IMCApp

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

ior = sys.argv[1]
obj = orb.string_to_object(ior)

eo = obj._narrow(IMCApp.CalcIMC)

if eo is None:
     print "Erro"
     sys.exit(1)

a = float(input("Altura: "))
b = float(input("Peso: "))
result  = eo.imc(a,b)

print "IMC= "+str("%.2f" % result)
