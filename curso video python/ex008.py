medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'A distância de {medida}m corresponde a {km}km, {hm}hm, {dam}dam, {dm}dm, {cm}cm e {mm}mm.')