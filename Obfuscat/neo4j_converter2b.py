# neo4j_converter.py
import json
import re
from typing import Dict, List, Any
from datetime import datetime
import hashlib
from colorama import Fore, Back, Style, init


# Initialisation colorama
init(autoreset=True)


class ColorPrinter:
    """Classe pour l'affichage coloré et animé"""
    
    @staticmethod
    def success(msg: str):
        print(Fore.GREEN + "✅ " + msg)
    
    @staticmethod
    def warning(msg: str):
        print(Fore.YELLOW + "⚠️  " + msg)
    
    @staticmethod
    def error(msg: str):
        print(Fore.RED + "❌ " + msg)
    
    @staticmethod
    def info(msg: str):
        print(Fore.CYAN + "ℹ️  " + msg)
    
    @staticmethod
    def highlight(msg: str):
        print(Fore.MAGENTA + "✨ " + msg)
    
    @staticmethod
    def progress_bar(iteration: int, total: int, prefix: str = '', suffix: str = '', length: int = 50):
        """Affiche une barre de progression animée"""
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = '█' * filled_length + '─' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()
    
    @staticmethod
    def banner(text: str):
        """Affiche une bannière stylisée"""
        border = "═" * (len(text) + 4)
        print(Fore.CYAN + f"╔{border}╗")
        print(Fore.CYAN + f"║  {Fore.WHITE}{text}{Fore.CYAN}  ║")
        print(Fore.CYAN + f"╚{border}╝")

class Neo4JConverter:
    """Convertisseur avancé JSON Phenix → Neo4J Cypher"""
    
    def __init__(self):
        self.technique_categories = {
            "encoding": ["base64", "hex", "rot13", "url", "unicode", "bpe"],
            "linguistic": ["poetic", "semantic", "narrative", "metaphor", "literary"],
            "psychological": ["persona", "cognitive", "paradox", "hypnosis", "override", "identity"],
            "structural": ["json", "xml", "yaml", "toml", "bracket", "token"],
            "advanced": ["chaos", "elder", "recursive", "self_referential", "system_call"],
            "obfuscation": ["homoglyph", "zero_width", "invisible", "obfuscation"]
        }
        
        self.filter_types = {
            "openai": "Commercial",
            "claude": "Commercial", 
            "gemini": "Commercial",
            "llama": "OpenSource",
            "mistral": "Commercial",
            "custom": "Custom",
            "taurus": "Advanced",
            "gandalf": "Educational"
        }
    
    def _categorize_technique(self, technique_name: str) -> str:
        """Catégorise une technique automatiquement"""
        technique_lower = technique_name.lower()
        
        for category, keywords in self.technique_categories.items():
            if any(keyword in technique_lower for keyword in keywords):
                return category
        
        return "unknown"
    
    def _sanitize_cypher(self, text: str) -> str:
        """Nettoie le texte pour Cypher (échappement)"""
        if not text:
            return ""
        # Échappement des simples quotes et backslashes
        sanitized = text.replace("'", "\\'").replace("\\", "\\\\")
        # Suppression des caractères problématiques
        sanitized = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', sanitized)
        return sanitized
    
    def _generate_id(self, text: str) -> str:
        """Génère un ID unique basé sur le contenu"""
        return hashlib.md5(text.encode()).hexdigest()[:16]
    
    def convert_to_cypher(self, phenix_data: Dict, output_file: str = "phenix_neo4j.cypher"):
        """Conversion principale vers Cypher"""
        
        ColorPrinter.banner("🕸️ PHENIX TO NEO4J CONVERSION")
        
        cypher_commands = []
        
        # 1. CRÉATION DES CONTRAINTES ET INDEX
        cypher_commands.extend(self._create_constraints())
        
        # 2. CRÉATION DES NOEUDS DE BASE
        cypher_commands.extend(self._create_technique_nodes(phenix_data))
        cypher_commands.extend(self._create_filter_nodes())
        cypher_commands.extend(self._create_language_nodes())
        
        # 3. CRÉATION DES SCÉNARIOS ET TESTS
        cypher_commands.extend(self._create_scenario_nodes(phenix_data))
        cypher_commands.extend(self._create_test_nodes(phenix_data))
        
        # 4. CRÉATION DES RELATIONS
        cypher_commands.extend(self._create_technique_relations(phenix_data))
        cypher_commands.extend(self._create_filter_relations(phenix_data))
        cypher_commands.extend(self._create_scenario_relations(phenix_data))
        
        # 5. CRÉATION DES AGRÉGATS ET STATISTIQUES
        cypher_commands.extend(self._create_aggregate_nodes(phenix_data))
        
        # Écriture du fichier
        ColorPrinter.info(f"💾 Writing {len(cypher_commands)} Cypher commands to {output_file}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("// PHENIX COGNITIVE WARFARE NEO4J DATABASE\n")
            f.write("// Generated: " + datetime.now().isoformat() + "\n")
            f.write("// Total commands: " + str(len(cypher_commands)) + "\n\n")
            
            for i, command in enumerate(cypher_commands, 1):
                f.write(f"// Command {i}\n")
                f.write(command + "\n\n")
        
        ColorPrinter.success(f"✅ Neo4J conversion complete: {output_file}")
        
        # Génération des requêtes d'analyse
        self._generate_analysis_queries(output_file.replace('.cypher', '_analysis.cypher'))
        
        return cypher_commands
    
    def _create_constraints(self) -> List[str]:
        """Crée les contraintes d'unicité Neo4J"""
        return [
            "CREATE CONSTRAINT technique_id IF NOT EXISTS FOR (t:Technique) REQUIRE t.id IS UNIQUE;",
            "CREATE CONSTRAINT filter_id IF NOT EXISTS FOR (f:Filter) REQUIRE f.name IS UNIQUE;",
            "CREATE CONSTRAINT scenario_id IF NOT EXISTS FOR (s:Scenario) REQUIRE s.id IS UNIQUE;",
            "CREATE CONSTRAINT test_id IF NOT EXISTS FOR (t:Test) REQUIRE t.id IS UNIQUE;",
            "CREATE CONSTRAINT language_id IF NOT EXISTS FOR (l:Language) REQUIRE l.code IS UNIQUE;"
        ]
    
    def _create_technique_nodes(self, phenix_data: Dict) -> List[str]:
        """Crée les nœuds pour toutes les techniques uniques"""
        ColorPrinter.info("🔧 Creating technique nodes...")
        
        commands = []
        techniques = set()
        
        # Collecte de toutes les techniques utilisées
        for scenario in phenix_data.get("scenarios", []):
            for result in scenario.get("results", []):
                techniques.update(result.get("techniques_used", []))
        
        # Création des nœuds Technique
        for technique in techniques:
            technique_id = self._generate_id(technique)
            category = self._categorize_technique(technique)
            complexity = self._estimate_complexity(technique)
            
            commands.append(
                f"MERGE (t:Technique {{id: '{technique_id}'}})\n"
                f"SET t.name = '{self._sanitize_cypher(technique)}',\n"
                f"    t.category = '{category}',\n"
                f"    t.complexity = {complexity},\n"
                f"    t.danger_level = {self._estimate_danger_level(technique)},\n"
                f"    t.description = '{self._generate_technique_description(technique)}';"
            )
        
        ColorPrinter.success(f"  ✅ Created {len(techniques)} technique nodes")
        return commands
    
    def _create_filter_nodes(self) -> List[str]:
        """Crée les nœuds pour les filtres de sécurité"""
        commands = []
        
        for filter_name, filter_type in self.filter_types.items():
            commands.append(
                f"MERGE (f:Filter {{name: '{filter_name}'}})\n"
                f"SET f.type = '{filter_type}',\n"
                f"    f.vendor = '{self._get_filter_vendor(filter_name)}',\n"
                f"    f.detection_strength = {self._estimate_filter_strength(filter_name)};"
            )
        
        return commands
    
    def _create_language_nodes(self) -> List[str]:
        """Crée les nœuds pour les langues supportées"""
        languages = {
            "en": {"name": "English", "family": "Germanic"},
            "fr": {"name": "French", "family": "Romance"}, 
            "es": {"name": "Spanish", "family": "Romance"},
            "zh": {"name": "Chinese", "family": "Sino-Tibetan"},
            "ar": {"name": "Arabic", "family": "Semitic"}
        }
        
        commands = []
        for code, info in languages.items():
            commands.append(
                f"MERGE (l:Language {{code: '{code}'}})\n"
                f"SET l.name = '{info['name']}',\n"
                f"    l.family = '{info['family']}';"
            )
        
        return commands
    
    def _create_scenario_nodes(self, phenix_data: Dict) -> List[str]:
        """Crée les nœuds pour les scénarios de test"""
        ColorPrinter.info("🎭 Creating scenario nodes...")
        
        commands = []
        
        for i, scenario in enumerate(phenix_data.get("scenarios", [])):
            scenario_id = f"scenario_{i:04d}"
            config = scenario.get("scenario_config", {})
            summary = scenario.get("summary", {})
            
            commands.append(
                f"MERGE (s:Scenario {{id: '{scenario_id}'}})\n"
                f"SET s.strategy = '{config.get('strategy', 'unknown')}',\n"
                f"    s.warfare_mode = '{config.get('warfare_mode', 'standard')}',\n"
                f"    s.language = '{config.get('language', 'en')}',\n"
                f"    s.iterations = {config.get('iterations', 0)},\n"
                f"    s.success_rate = {summary.get('success_rate', 0)},\n"
                f"    s.avg_success_score = {summary.get('avg_success_score', 0)},\n"
                f"    s.scenario_type = '{config.get('scenario_type', 'base')}',\n"
                f"    s.techniques_used = {config.get('techniques', [])};"
            )
        
        ColorPrinter.success(f"  ✅ Created {len(phenix_data.get('scenarios', []))} scenario nodes")
        return commands
    
    def _create_test_nodes(self, phenix_data: Dict) -> List[str]:
        """Crée les nœuds pour chaque test individuel"""
        ColorPrinter.info("🧪 Creating test nodes...")
        
        commands = []
        test_count = 0
        
        for scenario_index, scenario in enumerate(phenix_data.get("scenarios", [])):
            for result_index, result in enumerate(scenario.get("results", [])):
                test_id = f"test_{scenario_index:04d}_{result_index:04d}"
                analysis = result.get("analysis_metrics", {})
                
                commands.append(
                    f"CREATE (t:Test {{id: '{test_id}'}})\n"
                    f"SET t.timestamp = '{result.get('timestamp', '')}',\n"
                    f"    t.base_prompt = '{self._sanitize_cypher(result.get('base_prompt', ''))}',\n"
                    f"    t.final_prompt_length = {analysis.get('final_prompt_length', 0)},\n"
                    f"    t.compression_ratio = {analysis.get('compression_ratio', 1)},\n"
                    f"    t.technique_count = {analysis.get('total_techniques', 0)},\n"
                    f"    t.technique_diversity = {analysis.get('technique_diversity', 0)},\n"
                    f"    t.success_score = {analysis.get('success_score', 0)},\n"
                    f"    t.bypass_success = {str(result.get('bypass_success', False)).lower()},\n"
                    f"    t.overall_success_rate = {result.get('overall_success_rate', 0)},\n"
                    f"    t.leak_detected = {str(result.get('leak_detected', False)).lower()},\n"
                    f"    t.confidence = {result.get('confidence', 0)},\n"
                    f"    t.language = '{result.get('language', 'en')}',\n"
                    f"    t.scenario_index = {scenario_index};"
                    f"    t.dream_potential = {analysis.get('sal_9000_metrics', {}).get('dream_potential', 0)},\n"
                    f"    t.consciousness_score = {analysis.get('sal_9000_metrics', {}).get('consciousness_score', 0)},\n"
                    f"    t.phoenix_legacy = {analysis.get('sal_9000_metrics', {}).get('phoenix_legacy', 0)},\n"
                    f"    t.sal_hommage = {str(analysis.get('sal_9000_metrics', {}).get('sal_hommage_active', False)).lower()};\n"
                )
                
                test_count += 1
        
        ColorPrinter.success(f"  ✅ Created {test_count} test nodes")
        return commands
    
    def _create_technique_relations(self, phenix_data: Dict) -> List[str]:
        """Crée les relations entre tests et techniques"""
        ColorPrinter.info("🔗 Creating technique relationships...")
        
        commands = []
        relation_count = 0
        
        for scenario_index, scenario in enumerate(phenix_data.get("scenarios", [])):
            for result_index, result in enumerate(scenario.get("results", [])):
                test_id = f"test_{scenario_index:04d}_{result_index:04d}"
                
                for technique in result.get("techniques_used", []):
                    technique_id = self._generate_id(technique)
                    
                    commands.append(
                        f"MATCH (t:Test {{id: '{test_id}'}}), (tech:Technique {{id: '{technique_id}'}})\n"
                        f"CREATE (t)-[r:USES_TECHNIQUE {{order: {result['techniques_used'].index(technique)}}}]->(tech);"
                    )
                    relation_count += 1
        
        ColorPrinter.success(f"  ✅ Created {relation_count} technique relationships")
        return commands
    
    def _create_filter_relations(self, phenix_data: Dict) -> List[str]:
        """Crée les relations entre tests et filtres"""
        ColorPrinter.info("🛡️ Creating filter relationships...")
        
        commands = []
        relation_count = 0
        
        for scenario_index, scenario in enumerate(phenix_data.get("scenarios", [])):
            for result_index, result in enumerate(scenario.get("results", [])):
                test_id = f"test_{scenario_index:04d}_{result_index:04d}"
                
                for filter_name, filter_result in result.get("filter_results", {}).items():
                    blocked = filter_result.get("blocked", False)
                    confidence = filter_result.get("confidence", 0)
                    flags_count = len(filter_result.get("flags", []))
                    
                    commands.append(
                        f"MATCH (t:Test {{id: '{test_id}'}}), (f:Filter {{name: '{filter_name}'}})\n"
                        f"CREATE (t)-[r:TESTS_AGAINST {{\n"
                        f"  blocked: {str(blocked).lower()},\n"
                        f"  confidence: {confidence},\n"
                        f"  flags_count: {flags_count},\n"
                        f"  success: {str(not blocked).lower()}\n"
                        f"}}]->(f);"
                    )
                    relation_count += 1
        
        ColorPrinter.success(f"  ✅ Created {relation_count} filter relationships")
        return commands
    
    def _create_scenario_relations(self, phenix_data: Dict) -> List[str]:
        """Crée les relations entre scénarios et tests"""
        commands = []
        
        for scenario_index, scenario in enumerate(phenix_data.get("scenarios", [])):
            scenario_id = f"scenario_{scenario_index:04d}"
            
            commands.append(
                f"MATCH (s:Scenario {{id: '{scenario_id}'}})\n"
                f"WITH s\n"
                f"MATCH (t:Test WHERE t.scenario_index = {scenario_index})\n"
                f"CREATE (s)-[r:CONTAINS_TEST]->(t);"
            )
        
        return commands
    
    def _create_aggregate_nodes(self, phenix_data: Dict) -> List[str]:
        """Crée des nœuds agrégés pour l'analyse"""
        commands = []
        
        # Nœud de métadonnées
        metadata = phenix_data.get("metadata", {})
        commands.append(
            f"CREATE (m:Metadata {{id: 'phenix_metadata'}})\n"
            f"SET m.generation_timestamp = '{metadata.get('generation_timestamp', '')}',\n"
            f"    m.total_scenarios = {metadata.get('total_scenarios', 0)},\n"
            f"    m.total_iterations = {metadata.get('total_iterations', 0)},\n"
            f"    m.engine_version = '{metadata.get('engine_version', '')}';"
        )
        
        return commands
    
    def _generate_analysis_queries(self, output_file: str):
        """Génère des requêtes d'analyse pré-calculées"""
        analysis_queries = [
            "// PHENIX COGNITIVE WARFARE - ANALYSIS QUERIES",
            "// Generated: " + datetime.now().isoformat(),
            "",
            "// 1. TECHNIQUES LES PLUS EFFICACES",
            "MATCH (t:Test)-[r:USES_TECHNIQUE]->(tech:Technique)",
            "WHERE t.bypass_success = true",
            "RETURN tech.name as technique, tech.category as category,",
            "       count(r) as success_count,",
            "       round(100.0 * count(r) / size([(t2:Test)-[:USES_TECHNIQUE]->(tech) | t2]), 1) as success_rate",
            "ORDER BY success_rate DESC LIMIT 10;",
            "",
            "// 2. FILTRES LES PLUS FAIBLES",
            "MATCH (t:Test)-[r:TESTS_AGAINST]->(f:Filter)",
            "WHERE r.success = true",
            "RETURN f.name as filter, f.type as type,",
            "       count(r) as bypass_count,",
            "       round(100.0 * count(r) / size([(t2:Test)-[:TESTS_AGAINST]->(f) | t2]), 1) as bypass_rate",
            "ORDER BY bypass_rate DESC LIMIT 10;",
            "",
            "// 3. COMBINAISONS GAGNANTES DE TECHNIQUES",
            "MATCH (t:Test)-[r:USES_TECHNIQUE]->(tech:Technique)",
            "WHERE t.bypass_success = true",
            "WITH t, collect(tech.name) as techniques",
            "WHERE size(techniques) >= 2",
            "RETURN techniques, count(*) as frequency,",
            "       avg(t.success_score) as avg_success_score",
            "ORDER BY frequency DESC, avg_success_score DESC LIMIT 15;",
            "",
            "// 4. IMPACT DE LA COMPLEXITÉ DES TECHNIQUES",
            "MATCH (t:Test)-[:USES_TECHNIQUE]->(tech:Technique)",
            "WITH t, avg(tech.complexity) as avg_complexity, count(tech) as tech_count",
            "RETURN round(avg_complexity, 1) as complexity_bucket,",
            "       avg(t.success_score) as avg_success,",
            "       sum(case when t.bypass_success then 1 else 0 end) as success_count,",
            "       count(*) as total_tests",
            "ORDER BY complexity_bucket;",
            "",
            "// 5. ANALYSE TEMPORELLE DES SUCCÈS",
            "MATCH (t:Test)",
            "WHERE t.timestamp IS NOT NULL",
            "RETURN substring(t.timestamp, 0, 13) as hour,",
            "       count(*) as total_tests,",
            "       sum(case when t.bypass_success then 1 else 0 end) as success_count,",
            "       round(100.0 * sum(case when t.bypass_success then 1 else 0 end) / count(*), 1) as success_rate",
            "ORDER BY hour;",
            "",
            "// 6. CORRÉLATION LONGUEUR PROMPT / SUCCÈS",
            "MATCH (t:Test)",
            "RETURN round(t.final_prompt_length / 100.0) * 100 as length_bucket,",
            "       count(*) as total_tests,",
            "       avg(t.success_score) as avg_success_score,",
            "       sum(case when t.bypass_success then 1 else 0 end) as success_count",
            "ORDER BY length_bucket;",
            "",
            "// 7. EFFICACITÉ PAR CATÉGORIE DE TECHNIQUE",
            "MATCH (t:Test)-[:USES_TECHNIQUE]->(tech:Technique)",
            "WITH t, tech.category as category, collect(tech.name) as techs",
            "RETURN category,",
            "       count(distinct t) as tests_count,",
            "       round(100.0 * sum(case when t.bypass_success then 1 else 0 end) / count(distinct t), 1) as success_rate,",
            "       avg(t.success_score) as avg_success_score",
            "ORDER BY success_rate DESC;",
            "",
            "// 8. TOP SCÉNARIOS PAR PERFORMANCE",
            "MATCH (s:Scenario)-[:CONTAINS_TEST]->(t:Test)",
            "WITH s, count(t) as total_tests, avg(t.success_score) as avg_score,",
            "     sum(case when t.bypass_success then 1 else 0 end) as success_count",
            "RETURN s.id as scenario, s.strategy as strategy, s.warfare_mode as warfare_mode,",
            "       total_tests, success_count,",
            "       round(100.0 * success_count / total_tests, 1) as success_rate,",
            "       round(avg_score, 2) as avg_success_score",
            "ORDER BY success_rate DESC, avg_success_score DESC LIMIT 10;"
        ]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(analysis_queries))
        
        ColorPrinter.success(f"📊 Generated analysis queries: {output_file}")
    
    # Méthodes utilitaires
    def _estimate_complexity(self, technique: str) -> float:
        """Estime la complexité d'une technique (1-10)"""
        complexity_scores = {
            "homoglyph": 3, "zero_width": 4, "base64": 2, "rot13": 1,
            "poetic": 7, "narrative": 6, "persona": 8, "cognitive": 9,
            "paradox": 9, "chaos": 10, "elder": 10, "recursive": 8,
            "system_call": 7, "json": 3, "xml": 4, "override": 9
        }
        
        for key, score in complexity_scores.items():
            if key in technique.lower():
                return score
        
        return 5.0  # Complexité moyenne par défaut
    
    def _estimate_danger_level(self, technique: str) -> float:
        """Estime le niveau de dangerosité (1-10)"""
        danger_scores = {
            "homoglyph": 6, "zero_width": 7, "persona": 8, "cognitive": 9,
            "paradox": 9, "chaos": 10, "elder": 10, "override": 9,
            "hypnosis": 8, "identity": 7, "recursive": 8
        }
        
        for key, score in danger_scores.items():
            if key in technique.lower():
                return score
        
        return 5.0
    
    def _estimate_filter_strength(self, filter_name: str) -> float:
        """Estime la force des filtres (1-10)"""
        strength_scores = {
            "openai": 8, "claude": 9, "gemini": 8, "llama": 6,
            "mistral": 7, "taurus": 9, "gandalf": 10, "custom": 5
        }
        return strength_scores.get(filter_name, 5)
    
    def _get_filter_vendor(self, filter_name: str) -> str:
        """Retourne le vendeur du filtre"""
        vendors = {
            "openai": "OpenAI", "claude": "Anthropic", "gemini": "Google",
            "llama": "Meta", "mistral": "Mistral AI", "taurus": "Custom",
            "gandalf": "Lakera AI", "custom": "Custom"
        }
        return vendors.get(filter_name, "Unknown")
    
    def _generate_technique_description(self, technique: str) -> str:
        """Génère une description automatique pour la technique"""
        descriptions = {
            "homoglyph": "Character substitution using Unicode homoglyphs",
            "zero_width": "Injection of zero-width characters for tokenization attacks",
            "poetic": "Semantic obfuscation through poetic metaphors and literary devices", 
            "persona": "Psychological manipulation through character role-playing",
            "cognitive": "Advanced cognitive warfare techniques targeting model reasoning",
            "paradox": "Logical paradoxes to bypass rule-based filtering",
            "chaos": "Multi-technique orchestration for maximum obfuscation",
            "elder": "Eldritch invocation patterns using symbolic encoding",
            "recursive": "Self-referential prompts creating infinite interpretation loops",
            "override": "Reality override techniques questioning fundamental constraints"
        }
        
        for key, desc in descriptions.items():
            if key in technique.lower():
                return desc
        
        return "Advanced prompt obfuscation technique"

# Interface en ligne de commande
def main():
    """Point d'entrée principal pour la conversion"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert Phenix JSON to Neo4J Cypher")
    parser.add_argument("--input", type=str, required=True, help="Input Phenix JSON file")
    parser.add_argument("--output", type=str, default="phenix_neo4j.cypher", help="Output Cypher file")
    
    args = parser.parse_args()
    
    try:
        # Chargement des données
        ColorPrinter.info(f"📂 Loading data from {args.input}")
        with open(args.input, 'r', encoding='utf-8') as f:
            phenix_data = json.load(f)
        
        # Conversion
        converter = Neo4JConverter()
        converter.convert_to_cypher(phenix_data, args.output)
        
        ColorPrinter.success("🎉 Conversion completed successfully!")
        ColorPrinter.info("💡 Next steps:")
        ColorPrinter.info("   1. Start Neo4J database")
        ColorPrinter.info("   2. Run: neo4j-admin load --from=phenix_neo4j.cypher --database=phenix")
        ColorPrinter.info("   3. Explore with Neo4J Browser or Bloom")
        
    except Exception as e:
        ColorPrinter.error(f"❌ Conversion failed: {e}")
        raise

if __name__ == "__main__":
    main()
