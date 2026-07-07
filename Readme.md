# 🔎 Ba7ath Project — Outils pour l'Investigation Numérique et le Datajournalisme

[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://opensource.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Focus: OSINT](https://img.shields.io/badge/Focus-OSINT%20%7C%20Datajournalisme-blue.svg)]()

**Ba7ath Project** ("Recherche" en arabe) est un écosystème d'outils open source et de ressources pédagogiques dédié à l'investigation numérique (OSINT) et au datajournalisme, conçu pour les journalistes, les chercheurs et les analystes.

---

## 🎯 Notre Mission

Le journalisme d'investigation moderne repose sur la donnée. Ba7ath Project a été créé pour démocratiser et vulgariser l'utilisation de l'OSINT, en particulier pour les journalistes arabes. 

L'objectif est de fournir des outils gratuits, transparents et respectueux de la vie privée, tout en promouvant une hygiène numérique stricte. 

**Nos piliers méthodologiques :**
- ⚖️ **Éthique et Légalité :** Respect absolu du cadre légal, utilisation exclusive de sources publiques (scraping éthique).
- 🧩 **Transparence :** Documentation systématique des sources et de la chaîne de vérification (Mosaic Theory).
- 🔒 **Privacy-First :** Priorité aux environnements locaux (Local LLMs, SQLite) pour protéger les données sensibles et les sources.
- 📚 **Pédagogie :** Des outils documentés étape par étape pour faciliter l'apprentissage.

---

## 🚀 Écosystème d'Outils

Les dépôts sont classés par cas d'usage pour faciliter le travail des cellules d'investigation.

### 📊 Gouvernance des Données & Datajournalisme
| Projet | Description | Stack |
|--------|-------------|-------|
| **[Ba7ath Data Catalog](https://github.com/Ba7athproject/ba7ath_data_catalog)** | Catalogue de datasets pour documenter la traçabilité, l'audit qualité et le lineage des données d'enquête. | Python, Streamlit |
| **[Pest_Tn_Checker](https://github.com/Ba7athproject/Pest_Tn_Checker)** | Pipeline de réconciliation de données (ex: pesticides tunisiens vs bases réglementaires de l'UE). | Python, Pandas |
| **[GCT Watcher](https://github.com/Ba7athproject/GCT_Watcher)** | Plateforme d'analyse liant données financières et impact environnemental. | Python, DataViz |

### 🕵️‍♂️ OSINT & Extraction d'Information
| Projet | Description | Stack |
|--------|-------------|-------|
| **[Ba7ath OSINT Tracker](https://github.com/Ba7athproject/ba7ath_osint_tracker)** | Extraction manuelle d'entités (NER) pour structurer les investigations numériques complexes. | React, DistilBERT |
| **[Intel Scrap](https://github.com/Ba7athproject/intel_scrap)** | Moteur de scraping éthique, veille médiatique et scoring automatisé d'articles. | Python |
| **[Ba7ath_GIS](https://github.com/Ba7athproject/Ba7ath_GIS)** | Outils de cartographie et d'analyse géospatiale pour documenter les enquêtes sur le terrain. | Python, GIS |

### 🤖 IA pour les Rédactions & Traitement Médias
| Projet | Description | Stack |
|--------|-------------|-------|
| **[IA Redact Dashboard](https://github.com/Ba7athproject/IA_Redact_Dashboard)** | Assistant IA d'évaluation de la qualité journalistique et de l'aide au fact-checking. | LLM locaux |
| **[Audio_Derush](https://github.com/Ba7athproject/Audio_Derush)** | Outil de dérushage audio multilingue optimisé pour les dialectes arabes. | Python, Whisper |
| **[B_Trad](https://github.com/Ba7athproject/B_Trad)** | Traducteur de documents PDF assisté par IA locale, sans fuite de données vers le cloud. | Python, LLM |

---

## 🛠️ Stack Technologique

Pour garantir la pérennité, la gratuité et la sécurité des outils, nous privilégions des technologies robustes et déployables localement :
- **Analyse & Pipelines :** Python (Pandas, FastAPI, ...)
- **Interfaces (UI) :** Streamlit (pour les outils data), React / Tailwind CSS
- **Intelligence Artificielle :** Modèles ouverts (Qwen, Gemma, ...), Transformers.js, RAG / GraphRAG locaux
- **Persistance :** SQLite, Neo4J, PostgreSQL, formats ouverts (CSV, JSON)

---

## 📖 Ressources & Formations

Ba7ath n'est pas qu'un dépôt de code, c'est aussi un hub de formation. Nous proposons régulièrement des guides techniques détaillés et des tutoriels étape par étape pour aider la communauté à maîtriser les workflows d'investigation numérique. 
*(Une documentation en français et en arabe accompagne nos projets principaux).*

---

## 🤝 Contribuer

Que vous soyez datajournaliste, développeur ou enquêteur, vos contributions sont les bienvenues ! 
- Vérifiez le fichier `CONTRIBUTING.md` ou `Readme.md` de chaque dépôt.
- Signalez un bug ou suggérez une fonctionnalité via les **Issues**.
- Proposez des traductions ou des améliorations de la documentation.

---

## 📧 Contact & Réseaux

- 🌐 **GitHub :** [@Ba7athproject](https://github.com/Ba7athproject)
- 💬 **Support :** Ouvrez une "Issue" sur le dépôt concerné pour toute question technique ou méthodologique.

> *"L'investigation rigoureuse commence par des outils fiables et des méthodologies transparentes."*