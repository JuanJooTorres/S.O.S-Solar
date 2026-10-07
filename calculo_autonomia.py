#!/usr/bin/env python3
"""
S.O.S Solar - Calculo de autonomia y recarga.

Los valores por defecto son HIPOTETICOS (ilustrativos).
Reemplazalos con los datos reales del prototipo.

Uso:
    python calculo_autonomia.py
    python calculo_autonomia.py --panel 150 --hsp 3.8 --ah 100 --vbat 12 --carga 60
"""

import argparse


def calcular(p_pv, hsp, pr, c_ah, v_bat, dod, eta_inv, eta_bat, p_carga):
    e_pv_dia = p_pv * hsp * pr                      # Wh/dia generados
    e_bat_util = c_ah * v_bat * dod                 # Wh utilizables en bateria
    e_ac = e_bat_util * eta_inv * eta_bat           # Wh entregables en AC
    t_aut = e_ac / p_carga if p_carga > 0 else float("inf")  # horas
    dias_recarga = e_bat_util / (e_pv_dia * eta_bat) if e_pv_dia > 0 else float("inf")
    return e_pv_dia, e_bat_util, e_ac, t_aut, dias_recarga


def main():
    ap = argparse.ArgumentParser(description="Calculo de autonomia S.O.S Solar")
    ap.add_argument("--panel", type=float, default=100.0, help="Potencia del panel (Wp)")
    ap.add_argument("--hsp", type=float, default=4.0, help="Horas solares pico (h/dia)")
    ap.add_argument("--pr", type=float, default=0.70, help="Performance ratio")
    ap.add_argument("--ah", type=float, default=50.0, help="Capacidad del banco (Ah)")
    ap.add_argument("--vbat", type=float, default=12.0, help="Tension del banco (V)")
    ap.add_argument("--dod", type=float, default=0.50, help="DoD maximo (0-1)")
    ap.add_argument("--eta-inv", type=float, default=0.85, help="Eficiencia del inversor")
    ap.add_argument("--eta-bat", type=float, default=0.85, help="Eficiencia de la bateria")
    ap.add_argument("--carga", type=float, default=40.0, help="Carga promedio (W)")
    a = ap.parse_args()

    e_pv, e_bat, e_ac, t, d = calcular(
        a.panel, a.hsp, a.pr, a.ah, a.vbat, a.dod, a.eta_inv, a.eta_bat, a.carga
    )

    print("=== S.O.S Solar - Resultados ===")
    print(f"Energia generada por dia : {e_pv:8.1f} Wh/dia")
    print(f"Energia util en bateria  : {e_bat:8.1f} Wh")
    print(f"Energia entregable en AC : {e_ac:8.1f} Wh")
    print(f"Autonomia con {a.carga:.0f} W      : {t:8.2f} h")
    print(f"Recarga completa estimada: {d:8.2f} dias de sol")


if __name__ == "__main__":
    main()
