# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import json
import typing

class AIDisputeResolver(gl.Contract):
    # Состояние для отслеживания вердикта
    last_winner: str
    is_resolved: bool

    def __init__(self):
        self.last_winner = "NONE"
        self.is_resolved = False

    @gl.public.write
    def resolve_dispute(self, buyer_evidence: str, seller_evidence: str, contract_terms: str) -> dict:
        """
        Функция судьи. Анализирует доказательства и условия сделки.
        """
        
        def judge_logic() -> dict:
            # СИСТЕМНЫЙ ПРОМПТ
            task = f"""
            You are an autonomous on-chain judge.
            Contract Terms: {contract_terms}
            Buyer Evidence: {buyer_evidence}
            Seller Evidence: {seller_evidence}
            
            Evaluate strictly based on the terms. 
            Output ONLY valid JSON: {{"winner": "BUYER" | "SELLER"}}
            Do not add reasoning, markdown, or extra text.
            """
            
            # Получаем решение
            raw_response = gl.nondet.exec_prompt(task).strip()
            # Очистка от markdown
            clean_response = raw_response.replace("```json", "").replace("```", "").strip()
            
            return json.loads(clean_response)

        # Консенсус (строгий фильтр)
        verdict = gl.eq_principle.strict_eq(judge_logic)
        
        # Обновление состояния
        self.last_winner = verdict["winner"]
        self.is_resolved = True
        
        return verdict

    @gl.public.view
    def get_verdict(self) -> dict:
        return {
            "winner": self.last_winner,
            "resolved": self.is_resolved
        }