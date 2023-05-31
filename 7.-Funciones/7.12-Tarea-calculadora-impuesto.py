"""
Calculadora de impuesto
Crear una funcion para calcular el total de un pago de impuesto aplicado
Formula: pago_total = pagon_sin_impuesto + pagon_sin_impuesto * (impuesto / 100)
"""

def calculaImpuesto(pago_sim_impuesto, impuesto):
    pago_total = pago_sim_impuesto + pago_sim_impuesto * (impuesto / 100)
    return pago_total

# ejecutar funcion

pago_sin_impuesto = float(input('Proporcione el pago sin inpuesto: '))
impuesto = float(input("Propocione el porcentaje del impuesto: "))
pago_con_impuesto = calculaImpuesto(pago_sin_impuesto, impuesto)
print(pago_con_impuesto)