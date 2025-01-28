#funkcje anonimowe - lambda. funkcje ktore nie posiadaja nazwy
#uzywamy ją gdzie chcemy wykonac jedna operacje
from ast import Lambda

double = Lambda a: a * 2 # type: ignore
print(double(4))