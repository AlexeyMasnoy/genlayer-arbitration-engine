# GenLayer AI Dispute Resolver: Autonomous On-Chain Arbitration

### The "Trustless" Gap
Traditional smart contracts are binary: they execute code based on hard logic, but fail the moment **context** becomes subjective. When P2P deals go wrong (e.g., missed deadlines, quality disputes), current DeFi protocols either freeze funds indefinitely or rely on slow, centralized human mediators.

**AI Dispute Resolver** is an autonomous arbitration layer that leverages GenLayer’s nondeterministic consensus to evaluate evidence against contract terms, delivering instant, objective verdicts.



## Key Features
* **Nondeterministic Arbitration:** Leverages AI consensus to interpret non-structured data (evidence) and map it to hard code.
* **SLA Enforcement:** Automatically handles time-sensitive disputes (e.g., P2P delivery deadlines) without human intervention.
* **Trustless Context:** Eliminates the need for centralized escrow managers.
* **Strict Consensus:** Uses `strict_eq` to ensure that a verdict is only rendered when multiple AI models reach a consensus, preventing "hallucinated" outcomes.

## Technical Architecture
The system operates as a state-machine that transitions from `Active` to `Resolved` based on an AI-driven "Judge" logic.

1.  **Input:** Buyer and Seller submit evidence strings.
2.  **Logic:** The contract processes the `contract_terms` and evidence through a weighted AI consensus layer.
3.  **Consensus:** GenVM nodes execute the `judge_logic` task. If the consensus fails (models disagree), the system halts to request further evidence, ensuring security over speed.
4.  **Verdict:** The system outputs a rigid JSON structure `{"winner": "BUYER" | "SELLER"}`, which triggers state updates.

## Demo: P2P SLA Breach
This test demonstrates the system penalizing a seller for exceeding a 60-minute delivery window.

* **Contract Terms:** "Delivery of assets within 60 minutes after payment."
* **Buyer Evidence:** "Paid at 14:00. 90 minutes passed. Asset not received."
* **Seller Evidence:** "Internet issues, can send now."
* **System Verdict:** `{"winner": "BUYER", "resolved": true}`

## On-Chain Verification
| Metric | Value |
| :--- | :--- |
| **Contract Address** | `[0x1d10956d960f848bB7514bE8765961A40226E380]` |
| **Success Tx Hash** | `[0xa314c5fe9762db7c2a88584d4098977045cd66081d61058506163d8aacf0e247]` |
| **Consensus Mode** | `MAJORITY_AGREE` |
| **GenVM Version** | `v0.2.16` |

## Roadmap: V2 (Future Scope)
- **Multi-Modal Evidence:** Integration with IPFS to parse images/PDFs as proof (e.g., screenshots of chats).
- **Escrow Integration:** Direct locking/unlocking of funds within the dispute contract.
- **Reputation Layer:** Recording "Win/Loss" stats on-chain to identify malicious actors.

## License
MIT License. Built for the GenLayer Developer Challenge.
