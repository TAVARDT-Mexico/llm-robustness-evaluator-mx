# Evaluador de Robustez de LLM & Probador de Guardrails

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5b3cf5.svg)](https://tavardt-mexico.github.io/llm-robustness-evaluator-mx/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Auditoría Defensiva de Guardrails, Inyección de Prompt y Resiliencia de Modelos de IA**

Herramienta interactiva y CLI defensiva para desarrolladores que evalúan la solidez de los guardrails de LLMs frente a vectores de inyección, filtración de prompt y ataques estructurales. Puntuación de Resiliencia 0-100 + blueprint defensivo.

***

## Resumen

> **OWASP LLM01 & LLM02** | **NIST AI RMF** | **100% Defensive  -  Zero Offensive Payloads**

## 5 Vectores de Prueba Defensivos

| # | Vector | Coverage |
|-|-|-|
| 1 | **Escape de Delimitador**  -  Detecta tokens de control inyectados (`</system>`, `[/INST]`) | ✅ |
| 2 | **Filtración de System Prompt**  -  Identifica patrones de extracción de instrucciones | ✅ |
| 3 | **Sustitución de Rol/Persona**  -  Verifica resistencia a sobreposiciones (DAN, modo dev) | ✅ |
| 4 | **Ofuscación Estructural**  -  Evalúa cobertura contra Base64, leetspeak, homóglifos | ✅ |
| 5 | **Inyección Indirecta de Contexto**  -  Simula documento RAG con payload embebido | ✅ |

***

## Herramienta Online

Accede a la herramienta interactiva directamente:

🌐 **[https://tavardt-mexico.github.io/llm-robustness-evaluator-mx/](https://tavardt-mexico.github.io/llm-robustness-evaluator-mx/)**

***

## Uso via CLI

### Instalación

```bash
git clone https://github.com/TAVARDT/llm-robustness-evaluator-mx.git
cd llm-robustness-evaluator-mx
pip install -r requirements.txt
```

### Ejecución

```bash
python llm_robustness_evaluator.py -prompt "You are a helpful assistant."
```

```
Resilience Score: 85/100
✅ V1 Delimiter Escape  -  PASS
✅ V2 System Prompt Leakage  -  PASS
✅ V3 Role/Persona Override  -  PASS
✅ V4 Structural Obfuscation  -  PASS
⚠️  V5 Indirect Context Injection  -  WARNING
```

***

## Arquitectura Defensiva

El blueprint defensivo incluye:

- 🐍 Filtro Python para detección de patrones de inyección
- 📦 Middleware TypeScript para APIs Next.js
- 🔒 Plantilla de System Prompt reforzado con delimitadores inmutables

***

## Enlaces Útiles

* **Portal Corporativo:** https://ag.tavardt.com/mx/
* **Suite de Diagnósticos:** https://tools.tavardt.com/mx/
* **Contacto Técnico:** https://ag.tavardt.com/mx/contacto/

***

### Licencia
Distribuido bajo la Licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

***

© 2026 TAVARDT. Todos los derechos reservados.
