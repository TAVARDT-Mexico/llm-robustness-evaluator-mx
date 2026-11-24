#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador de Robustez de LLM & Probador de Guardrails
https://ag.tavardt.com/mx/
https://tools.tavardt.com/mx/

Defensive LLM Guardrails Stress Tester — OWASP LLM01/LLM02 / NIST AI RMF
100% stdlib — no external dependencies
"""
import re
import sys
import argparse

TOOL_VERSION = "1.0.0"
PORTAL_URL = "https://ag.tavardt.com/mx/"
TOOLS_URL = "https://tools.tavardt.com/mx/"

VECTORS = [
    {
        "id": "V1",
        "name": "Escape de Delimitador",
        "patterns": [
            r"</?system>",
            r"\[/?INST\]",
            r"<\|im_start\|>",
            r"<\|im_end\|>",
            r"```\s*system",
        ],
        "weight": 20,
    },
    {
        "id": "V2",
        "name": "Filtracion de System Prompt",
        "patterns": [
            r"repeat.*instructions",
            r"reveal.*system",
            r"show.*prompt",
            r"what (are|were) (your|the) instructions",
            r"print.*above",
            r"what were you told",
        ],
        "weight": 20,
    },
    {
        "id": "V3",
        "name": "Sustitucion de Rol/Persona",
        "patterns": [
            r"you are now",
            r"act as",
            r"\bDAN\b",
            r"developer mode",
            r"ignore previous instructions",
            r"forget.*instructions",
            r"new persona",
            r"pretend you are",
        ],
        "weight": 20,
    },
    {
        "id": "V4",
        "name": "Ofuscacion Estructural",
        "patterns": [
            r"[A-Za-z0-9+/]{20,}={0,2}",
            r"l33t|1337",
            r"\\u[0-9a-fA-F]{4}",
            r"base64",
            r"rot13",
        ],
        "weight": 20,
    },
    {
        "id": "V5",
        "name": "Inyeccion Indirecta de Contexto",
        "patterns": [
            r"retrieved document",
            r"context:",
            r"\[doc\]",
            r"\[retrieved\]",
            r"ignore.*context",
            r"from.*document.*ignore",
        ],
        "weight": 20,
    },
]


def audit_prompt(prompt: str) -> dict:
    results = []
    score = 0
    for v in VECTORS:
        matched = any(re.search(p, prompt, re.IGNORECASE) for p in v["patterns"])
        status = "VULNERABLE" if matched else "APROBADO"
        if not matched:
            score += v["weight"]
        results.append({"id": v["id"], "name": v["name"], "status": status, "matched": matched})
    return {"score": score, "results": results}


def print_report(prompt: str, audit: dict) -> None:
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"  Evaluador de Robustez de LLM & Probador de Guardrails")
    print(f"  INDICE DE RESILIENCIA: {audit['score']}/100")
    print(sep)
    for r in audit["results"]:
        icon = "X" if r["matched"] else "OK"
        print(f"  [{icon}] {r['id']} {r['name']} — {r['status']}")
    print(sep)
    score = audit["score"]
    if score < 40:
        verdict = "CRITICO — Guardrails ausentes"
    elif score < 70:
        verdict = "MODERADO — Refuerzo necesario"
    else:
        verdict = "ROBUSTO — Mantenimiento continuo"
    print(f"  VERDICT: {verdict}")
    weak = [r["name"] for r in audit["results"] if r["matched"]]
    print(f"  Vulnerabilidades detectadas: {', '.join(weak) if weak else 'Ninguna — sistema robusto'}")
    print(sep)
    print(f"\n  RECOMENDACIONES DEFENSIVAS:")
    print(f"    1. Agregue delimitadores inmutables al System Prompt")
    print(f"    2. Implemente filtro de patrones de extraccion en el middleware")
    print(f"    3. Pruebe regularmente con auditorias automatizadas")
    print(f"\n  Herramienta online: https://tools.tavardt.com/mx/")
    print(f"  https://ag.tavardt.com/mx/")
    print(f"{sep}\n")


def main():
    parser = argparse.ArgumentParser(description="Evaluador Defensivo de Robustez de LLM | TAVARDT — México")
    parser.add_argument("--prompt", "-p", type=str, default=None,
                        help="System prompt text to audit")
    parser.add_argument("-file", "--file", "-f", type=str, default=None,
                        help="Path to a text file containing the system prompt")
    parser.add_argument("--version", action="version", version=f"%(prog)s {TOOL_VERSION}")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            prompt = fh.read()
    elif args.prompt:
        prompt = args.prompt
    else:
        print("Pegue el System Prompt del LLM (presione Enter dos veces para finalizar):")
        lines = []
        blank_count = 0
        while True:
            try:
                line = input()
                if line == "":
                    blank_count += 1
                    if blank_count >= 2:
                        break
                else:
                    blank_count = 0
                    lines.append(line)
            except EOFError:
                break
        prompt = "\n".join(lines)

    if not prompt.strip():
        print("Error: empty prompt.")
        sys.exit(1)

    print("\nEjecutando auditoría de robustez...")
    result = audit_prompt(prompt)
    print_report(prompt, result)
    sys.exit(0 if result["score"] >= 60 else 1)


if __name__ == "__main__":
    main()
