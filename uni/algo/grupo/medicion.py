import time
import random
import sys

sys.setrecursionlimit(10000)

# ── algoritmos ────────────────────────────────────────────────────────────────

def selection_sort_iterativo(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0
    a = arr[:]
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            intercambios += 1
    return comparaciones, intercambios, 0   # llamadas recursivas = N/A


def selection_sort_recursivo(arr):
    a = arr[:]
    comparaciones = [0]
    intercambios  = [0]
    llamadas      = [0]

    def _rec(start):
        llamadas[0] += 1
        if start >= len(a) - 1:
            return
        min_idx = start
        for j in range(start + 1, len(a)):
            comparaciones[0] += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != start:
            a[start], a[min_idx] = a[min_idx], a[start]
            intercambios[0] += 1
        _rec(start + 1)

    _rec(0)
    return comparaciones[0], intercambios[0], llamadas[0]


# ── generadores de entrada ────────────────────────────────────────────────────

def gen_array(n, tipo):
    if tipo == "Aleatoria":
        a = list(range(1, n + 1))
        random.shuffle(a)
        return a
    elif tipo == "Ordenada":
        return list(range(1, n + 1))
    elif tipo == "Invertida":
        return list(range(n, 0, -1))
    return list(range(1, n + 1))


# ── casos requeridos por la plantilla ─────────────────────────────────────────

CASOS = [
    (10,  "Aleatoria", "Iterativa"),
    (10,  "Aleatoria", "Recursiva"),
    (100, "Ordenada",  "Iterativa"),
    (100, "Ordenada",  "Recursiva"),
    (500, "Aleatoria", "Iterativa"),
    (500, "Aleatoria", "Recursiva"),
]

REPETICIONES = 5   # promedio de varias corridas para más estabilidad

random.seed(42)

resultados = []

for n, entrada, version in CASOS:
    tiempos = []
    for rep in range(REPETICIONES):
        arr = gen_array(n, entrada)
        t0 = time.perf_counter()
        if version == "Iterativa":
            cmp, swp, rec = selection_sort_iterativo(arr)
        else:
            cmp, swp, rec = selection_sort_recursivo(arr)
        t1 = time.perf_counter()
        tiempos.append(t1 - t0)

    tiempo_ms = (sum(tiempos) / len(tiempos)) * 1000
    resultados.append((n, entrada, version, tiempo_ms, cmp, swp, rec))


# ── salida formateada ─────────────────────────────────────────────────────────

SEP  = "-" * 72
def fila(n, entrada, version, tiempo, cmp, swp, rec):
    rec_str = str(rec) if rec > 0 else "N/A"
    return (
        f"| {str(n):<5} | {entrada:<10} | {version:<10} | "
        f"{tiempo:>8.4f} ms | {cmp:>12} | {swp:>10} | {rec_str:>9} |"
    )

output_lines = [
    "",
    "5. Medición experimental — Selection Sort",
    SEP,
    f"| {'n':<5} | {'Entrada':<10} | {'Versión':<10} | {'Tiempo':>11} | "
    f"{'Comparaciones':>12} | {'Interc./Mov':>10} | {'Llam.rec.':>9} |",
    SEP,
]

for r in resultados:
    output_lines.append(fila(*r))

output_lines += [
    SEP,
    f"  (cada valor es el promedio de {REPETICIONES} ejecuciones)",
    "",
]

output = "\n".join(output_lines)
print(output)

# guardar en archivo
with open("medicion_resultados.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Resultados guardados en medicion_resultados.txt")
