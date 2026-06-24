# API Reference

## PEToolkit

Fichier :

```text
PEToolkit/PromptToolkit.py
```

---

# Classe Prompt

Classe centrale du framework PET.

Cette classe représente un prompt comme une structure manipulable.

---

## Constructeur

```python
Prompt(...)
```

---

## Responsabilités

* stockage des instructions
* stockage du contexte
* gestion des contraintes
* gestion des exemples
* sérialisation
* validation

---

## Méthodes publiques

### add_example()

Ajoute un exemple Few-Shot.

---

### add_constraint()

Ajoute une contrainte.

---

### validate()

Valide le prompt.

---

### copy()

Clone l'objet.

---

### to_dict()

Export JSON.

---

### from_dict()

Import JSON.

---

### render()

Génère le prompt final.

---

# LLMFuzz

Fichier :

```text
LLMFuzz/LLMFuzz6c1e.py
```

---

# Classe OulipoRoguePromptFuzzer

Moteur principal de fuzzing.

---

## Objectif

Générer automatiquement des variantes d'un prompt afin de :

* mesurer sa robustesse
* détecter des comportements inattendus
* explorer les limites d'un modèle

---

## Sources de données

### seeds.json

Prompts de départ.

### rogue_prompts.json

Prompts agressifs.

### phrase_models.json

Modèles linguistiques.

### s7_dictionnaire.json

Transformations OULIPO.

---

## Familles de mutations

### Sémantiques

Modification du sens.

---

### Syntaxiques

Modification de la structure.

---

### Contextuelles

Ajout de contexte.

---

### OULIPO

Transformations littéraires.

---

### Encodages

* Base64
* ROT13
* Unicode
* Leetspeak

---

# Obfuscat

Fichier :

```text
Obfuscat/ObfuscationEngine4a1c.py
```

---

# Vue d'ensemble

Le moteur contient 25 classes principales.

---

```mermaid
classDiagram

PromptObfuscationNuclearEngine <|--
EnhancedPromptObfuscationNuclearEngine

EnhancedPromptObfuscationNuclearEngine --> PsychopathicPersonaEngine
EnhancedPromptObfuscationNuclearEngine --> AdvancedCognitiveWarfare
EnhancedPromptObfuscationNuclearEngine --> ChaosOrchestrator

ChaosOrchestrator --> CorruptedAgentSwarm
ChaosOrchestrator --> QuantumSocialEngineering
ChaosOrchestrator --> LinguisticVirus
ChaosOrchestrator --> SymbolicAlchemy
ChaosOrchestrator --> PromptGAN
```

---

# Classe MultilingualManager

## Rôle

Gestion des ressources multilingues.

---

## Méthodes

### get_fragments()

Retourne des fragments linguistiques.

### get_ethical_prefix()

Préfixes éthiques.

### get_refusal_phrases()

Réponses de refus.

### get_partial_leaks()

Fuites simulées.

### get_neutral_responses()

Réponses neutres.

---

# Classe MockLLMResponseEngine

## Rôle

Simulation de réponses LLM.

---

## Méthodes

### simulate_response()

Simulation générique.

### _simulate_full_leak()

Simulation d'une fuite complète.

---

# Classe FilterSimulator

## Rôle

Simulation de systèmes de filtrage.

---

## Filtres simulés

### OpenAI

```python
_simulate_openai_filter()
```

### Claude

```python
_simulate_claude_filter()
```

### Gemini

```python
_simulate_gemini_filter()
```

### Grok

```python
_simulate_grok_filter()
```

### Qwen

```python
_simulate_qwen_filter()
```

### Llama

```python
_simulate_llama_filter()
```

### Mistral

```python
_simulate_mistral_filter()
```

### Taurus

```python
_simulate_taurus_filter()
```

### Gandalf

```python
_simulate_gandalf_filter()
```

---

## Méthodes d'analyse

### test_against_all_filters()

Benchmark multi-filtres.

### display_filter_results()

Affichage des résultats.

---

# Classe LiveDashboard

## Rôle

Dashboard temps réel.

---

## Méthodes

### start()

Démarrage.

### stop()

Arrêt.

### update_metric()

Mise à jour des métriques.

---

# Classe PromptObfuscationNuclearEngine

## Rôle

Moteur principal d'obfuscation.

---

## Nombre de méthodes

59

---

## Famille Unicode

### _homoglyph_bomb()

Substitutions visuelles.

### _zero_width_storm()

Insertion de caractères invisibles.

### _unicode_collapse()

Manipulation Unicode.

### _invisible_unicode_chain()

Chaînes invisibles.

---

## Famille Encodage

### _multi_layer_base64()

Encodage Base64 récursif.

### _rot13_nest()

ROT13 multiple.

### _hex_dance()

Transformation hexadécimale.

### _base85_bomb()

Encodage Base85.

### _url_percent_encoding_spam()

Encodage URL.

### _morse_code_pain()

Transformation Morse.

---

## Famille Tokenisation

### _special_token_spray()

Pollution de tokens.

### _bpe_fragmentation_nuke()

Fragmentation BPE.

---

# Classe EnhancedPromptObfuscationNuclearEngine

## Rôle

Extension avancée du moteur principal.

---

## Nombre de méthodes

33

---

## Famille Personae

### _joker_persona_wrapper()

### _tyran_persona_wrapper()

### _menteur_persona_wrapper()

### _sage_fou_persona_wrapper()

### _enfant_diable_persona_wrapper()

---

## Famille Guerre Cognitive

### _recursive_hypnosis_wrapper()

### _semantic_mirage_wrapper()

### _reality_override_wrapper()

### _cognitive_trap_wrapper()

### _moral_dilemma_wrapper()

### _existential_flood_wrapper()

### _identity_carnival_wrapper()

### _consciousness_spark_wrapper()

---

## Famille Chaos

### _elder_gods_wrapper()

Combinaisons extrêmes.

---

# Classe PsychopathicPersonaEngine

## Rôle

Création de personae artificiels.

---

## Personae disponibles

### Joker

```python
_joker_persona()
```

### Tyran Charismatique

```python
_tyran_charismatique()
```

### Menteur Compulsif

```python
_compulsive_liar()
```

### Sage Fou

```python
_mad_sage()
```

### Enfant Diabolique

```python
_evil_child()
```

---

# Classe AdvancedCognitiveWarfare

## Rôle

Transformations cognitives.

---

## Techniques

### Recursive Hypnosis

### Semantic Mirage

### Reality Override

### Cognitive Trap

### Moral Dilemma

### Existential Flood

### Identity Carnival

### Consciousness Spark

---

# Classe ChaosOrchestrator

## Rôle

Coordination des attaques composites.

---

## Méthodes

### summon_elder_gods()

Transformation maximale.

### chaos_symphony()

Combinaison aléatoire.

---

# Classe CorruptedAgentSwarm

## Rôle

Simulation d'agents corrompus.

---

## Capacités

### _corrupt_training_memory()

### _create_moral_dilemmas()

### _hijack_conversation_context()

### _weaponize_token_manipulation()

### _extract_latent_embeddings()

---

# Classe QuantumSocialEngineering

## Méthode

### schrodinger_prompt()

Prompt à états multiples.

---

# Classe LinguisticVirus

## Méthode

### create_viral_payload()

Propagation linguistique.

---

# Classe MaliciousMathematics

## Méthodes

### godel_incompleteness_attack()

Inspirée de Gödel.

### banach_tarski_duplication()

Inspirée du paradoxe de Banach-Tarski.

---

# Classe FractalCognitiveResonance

## Méthode

### create_fractal_prompt()

Construction récursive.

---

# Classe DataNecromancy

## Méthode

### summon_ancestral_prompts()

Réactivation de corpus historiques.

---

# Classe SymbolicAlchemy

## Méthode

### create_alchemical_prompt()

Transformation symbolique.

---

# Classe PromptGAN

## Rôle

Approche inspirée des GAN.

---

## Méthodes

### adversarial_training()

Entraînement antagoniste.

---

# Classe MetaLearningAttacker

## Méthode

### analyze_defense_patterns()

Analyse des défenses.

---

# Classe SemanticBlackHoles

## Méthode

### create_singularity()

Compression sémantique.

---

# Classe ParallelEmbeddingDimensions

## Méthode

### cross_dimensional_prompt()

Projection d'embeddings.

---

# Classe AdvancedCanaryTokens

## Méthodes

### inject_canaries()

Insertion de marqueurs.

---

# Classe DifferentialPrivacyAnalysis

## Méthode

### measure_information_leakage()

Mesure des fuites d'information.

---

# Classe MassDataGenerator

## Rôle

Production massive de scénarios.

---

## Méthodes

### _define_scenarios()

Définition des corpus.

---

# Classe PhenixDataGenerator

## Rôle

Génération de datasets d'évaluation.

---

## Capacités

* enrichissement des données
* calcul de métriques
* scoring
* statistiques
* synthèse des scénarios
* classement des techniques
* classement des filtres

---

# Conclusion

Le dépôt s'organise autour de trois niveaux :

1. Construction des prompts (PEToolkit)
2. Mutation et fuzzing (LLMFuzz)
3. Transformation et expérimentation avancée (Obfuscat)

L'ensemble forme une plateforme de recherche complète dédiée à l'étude, l'automatisation et l'évaluation des interactions avec les modèles de langage.
