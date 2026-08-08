#!/usr/bin/env python3
"""
validar_relatorio.py — Validação determinística de relatórios da jornada-invisivel-mapper.

Uso:
  Linux / macOS / Hermes:
    python3 scripts/validar_relatorio.py <relatorio.md>
  Windows / Kimi CLI / Claude Code:
    python scripts\validar_relatorio.py <relatorio.md>

Verifica (sem depender de interpretação de LLM):
  1. Datas: nenhuma data de prazo anterior à data da análise
  2. Conversão acumulada: percentual bate com a conta; headline usa etapa EFETIVA, não nominal
  3. Divergência calc vs oficial em etapas obrigatórias (WARN se houver GAP/Veredito, FAIL se não)
  4. Gate de amostra: teste com n < 100 por variação sem marcação DIRECTIONAL = FAIL
  5. Prazos > 14 dias sem justificativa = WARN
  6. Taxonomia: tipo de momento de verdade fora dos 5 oficiais = FAIL

Exit code: 0 = PASS (WARN permitido), 1 = FAIL.
"""

import io
import re
import sys
from datetime import date

# Garante saída UTF-8 mesmo em terminais Windows legados (cp1252).
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
except AttributeError:
    pass

TIPOS_OFICIAIS = {"Magia", "Frustração", "Dúvida", "Confirmação", "Recuperação"}
ETAPAS_OBRIGATORIAS = {"compra", "entrega"}


def num(s):
    return int(s.replace(".", "").replace(",", "").strip())


def parse_tabelas_funil(linhas):
    """Extrai tabelas de funil (header com Chegaram + Abandonaram)."""
    tabelas = []
    i = 0
    while i < len(linhas):
        l = linhas[i]
        if l.strip().startswith("|") and "Chegaram" in l and "Abandonaram" in l:
            linhas_tab = []
            j = i + 2  # pula header + separador
            while j < len(linhas) and linhas[j].strip().startswith("|"):
                celulas = [c.strip() for c in linhas[j].strip().strip("|").split("|")]
                if len(celulas) >= 3 and re.match(r"^\d", celulas[1]):
                    try:
                        linhas_tab.append(
                            {"etapa": celulas[0], "chegaram": num(celulas[1]), "abandonaram": num(celulas[2])}
                        )
                    except ValueError:
                        pass
                j += 1
            if linhas_tab:
                tabelas.append(linhas_tab)
            i = j
        else:
            i += 1
    return tabelas


def main():
    if len(sys.argv) < 2:
        print("Uso: python validar_relatorio.py <relatorio.md>")
        sys.exit(2)

    texto = open(sys.argv[1], encoding="utf-8").read()
    linhas = texto.splitlines()
    fails, warns, infos = [], [], []

    # --- Data da análise ---
    m = re.search(r"Data da an[áa]lise:\**\s*(\d{4})-(\d{2})-(\d{2})", texto)
    if not m:
        fails.append("Data da análise não encontrada no cabeçalho (formato: Data da análise: YYYY-MM-DD)")
        data_analise = None
    else:
        data_analise = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))

    # --- Check 1: datas ---
    if data_analise:
        for d in re.finditer(r"(20\d{2})-(\d{2})-(\d{2})", texto):
            dt = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
            if dt < data_analise:
                fails.append(f"DATA NO PASSADO: {d.group(0)} < data da análise {data_analise}")
            elif (dt - data_analise).days > 14:
                warns.append(f"Prazo > 14 dias: {d.group(0)} ({(dt - data_analise).days} dias) — exige justificativa explícita")

    # --- Tabelas de funil ---
    tabelas = parse_tabelas_funil(linhas)
    if not tabelas:
        fails.append("Nenhuma tabela de funil (Chegaram/Abandonaram) encontrada")

    efetivos, nominais = set(), set()
    divergencias = []
    if len(tabelas) >= 1:
        por_etapa = {}
        for tab in tabelas:
            for row in tab:
                por_etapa.setdefault(row["etapa"], []).append(row)
        for etapa, rows in por_etapa.items():
            if etapa.lower() in ETAPAS_OBRIGATORIAS:
                for r in rows:
                    nominais.add(r["chegaram"])
                    efetivos.add(r["chegaram"] - r["abandonaram"])
        # proxy: chegada na etapa seguinte também é efetivo
        for tab in tabelas:
            for k, row in enumerate(tab):
                if row["etapa"].lower() in ETAPAS_OBRIGATORIAS and k + 1 < len(tab):
                    efetivos.add(tab[k + 1]["chegaram"])
        # divergências entre tabelas em etapas obrigatórias
        for etapa, rows in por_etapa.items():
            if etapa.lower() in ETAPAS_OBRIGATORIAS:
                vals = {r["chegaram"] for r in rows}
                if len(vals) > 1:
                    divergencias.append(f"{etapa}: {sorted(vals)}")

    # --- Check 2: conversão acumulada ---
    m = re.search(r"(\d+)\s*descobertas?\s*→\s*(\d+)\s*(?:compras?|convers[õo]es)\s*=\s*\**(\d+[.,]?\d*)%", texto)
    if not m:
        fails.append("Frase de conversão acumulada não encontrada (formato: 'X descobertas → Y compras = Z%')")
    else:
        x, y, z = int(m.group(1)), int(m.group(2)), float(m.group(3).replace(",", "."))
        calc_pct = round(y / x * 100, 1) if x else 0
        if abs(calc_pct - z) > 0.6:
            fails.append(f"ARITMÉTICA: {y}/{x} = {calc_pct}%, mas headline diz {z}%")
        if efetivos or nominais:
            if y in efetivos:
                infos.append(f"Conversão acumulada usa valor efetivo ({y}) OK")
            elif y in nominais:
                fails.append(f"HEADLINE NOMINAL: {y} = chegaram na etapa (nominal). Efetivos disponíveis: {sorted(efetivos)}. Use a etapa EFETIVA e mostre a conta.")
            else:
                fails.append(f"HEADLINE NÃO DERIVA DE NENHUMA TABELA: {y} não aparece como nominal {sorted(nominais)} nem efetivo {sorted(efetivos)}")

    # --- Check 3: divergências calc vs oficial ---
    if divergencias:
        if re.search(r"GAP DE DADOS", texto) and re.search(r"Veredito", texto):
            warns.append(f"Divergência calc vs oficial em etapas obrigatórias ({'; '.join(divergencias)}) — GAP/Veredito presente, confirmar cobertura no checklist (Passo 2)")
        else:
            fails.append(f"DIVERGÊNCIA SEM VEREDITO em etapas obrigatórias: {'; '.join(divergencias)} — exigir GAP DE DADOS com veredito (seção 3.3.4)")

    # --- Check 4: gate de amostra ---
    for l in linhas:
        if "variação" in l and "DIRECTIONAL" not in l:
            for mm in re.finditer(r"(\d+)\s*(?:clientes|propostas|entregas)", l):
                if int(mm.group(1)) < 100:
                    fails.append(f"AMOSTRA SEM DIRECTIONAL: '{mm.group(0)}' em linha de teste sem marcação → {l.strip()[:100]}")
    # --- Check 5: taxonomia ---
    for l in linhas:
        if re.search(r"\bMV_[A-Z]_\d+", l) and l.strip().startswith("|"):
            celulas = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(celulas) >= 3:
                tipo = celulas[2]
                if tipo and tipo not in TIPOS_OFICIAIS and "Tipo" not in tipo:
                    fails.append(f"TAXONOMIA: tipo '{tipo}' fora dos 5 oficiais ({celulas[0]}) — usar fallback da seção 5.4")

    # --- Saída ---
    print("=" * 70)
    print(f"VALIDAÇÃO: {sys.argv[1]}")
    print("=" * 70)
    for f in fails:
        print(f"[FAIL] {f}")
    for w in warns:
        print(f"[WARN] {w}")
    for i in infos:
        print(f"[INFO] {i}")
    print("-" * 70)
    if fails:
        print(f"RESULTADO: FAIL ({len(fails)} bloqueante(s), {len(warns)} aviso(s)) — relatório BLOQUEADO")
        sys.exit(1)
    print(f"RESULTADO: PASS ({len(warns)} aviso(s) — justificar no relatório)")
    sys.exit(0)


if __name__ == "__main__":
    main()
