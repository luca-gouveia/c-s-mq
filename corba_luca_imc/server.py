import sys
from omniORB import CORBA, PortableServer
import IMCApp, IMCApp__POA

class imc_i (IMCApp__POA.CalcIMC):
    def imc(self, a,b):
        c = b/(a**2)
        print("ok")
        return c

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

ei = imc_i()
eo = ei._this()

print orb.object_to_string(eo)

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run()
