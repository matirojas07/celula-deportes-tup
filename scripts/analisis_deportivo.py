
# CDTUP-3: Script de análisis de resultados deportivos
# Escenario D - Organización Empresarial - UTN TUP 2026

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/resultados_torneo.csv")

equipos = pd.unique(df[["equipo_local", "equipo_visitante"]].values.ravel())
tabla = {equipo: {"PJ":0,"G":0,"E":0,"P":0,"GF":0,"GC":0,"Pts":0} for equipo in equipos}

for _, row in df.iterrows():
    local = row["equipo_local"]
    visita = row["equipo_visitante"]
    gl = row["goles_local"]
    gv = row["goles_visitante"]
    tabla[local]["PJ"] += 1
    tabla[visita]["PJ"] += 1
    tabla[local]["GF"] += gl
    tabla[local]["GC"] += gv
    tabla[visita]["GF"] += gv
    tabla[visita]["GC"] += gl
    if gl > gv:
        tabla[local]["G"] += 1
        tabla[local]["Pts"] += 3
        tabla[visita]["P"] += 1
    elif gl < gv:
        tabla[visita]["G"] += 1
        tabla[visita]["Pts"] += 3
        tabla[local]["P"] += 1
    else:
        tabla[local]["E"] += 1
        tabla[local]["Pts"] += 1
        tabla[visita]["E"] += 1
        tabla[visita]["Pts"] += 1

tabla_df = pd.DataFrame(tabla).T.sort_values("Pts", ascending=False)
print(tabla_df)

total_goles = df["goles_local"].sum() + df["goles_visitante"].sum()
print(f"Promedio goles por partido: {total_goles/len(df):.2f}")

fig, axes = plt.subplots(1, 2, figsize=(14,5))
axes[0].bar(tabla_df.index, tabla_df["Pts"])
axes[0].set_title("Puntos por Equipo")
axes[1].bar(tabla_df.index, tabla_df["GF"], width=0.4, label="GF")
axes[1].set_title("Goles a Favor vs En Contra")
plt.savefig("resultados/grafico_rendimiento.png")
plt.show()
