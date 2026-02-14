# RESEARCH: Local LLMs for Gonzo Style Creative Writing

**Date:** 2026-02-12  
**Target Hardware:** NVIDIA RTX 3060 (12GB and 6GB variants)  
**Objective:** Identify the best local models and strategies for "Gonzo" style prose (Hunter S. Thompson).

---

## 1. Model Comparison (RTX 3060 Optimized)

The RTX 3060 12GB is the "sweet spot" for mid-range local LLMs, allowing for 12B-14B models at high precision. The 6GB variant is restricted to 7B-9B models at lower quantization.

| Model Category | Specific Recommendation | VRAM (Q8/Q4) | Notes |
| :--- | :--- | :--- | :--- |
| **Llama 3.1 (8B)** | **Stheno-v3.2** | 8.5GB / 5.5GB | The current king of 8B creative writing. Very "loose" and creative. Fits perfectly on 6GB cards at Q4_K_M. |
| **Mistral NeMo (12B)** | **Mini-Magnum-12B-v1.1** | 13GB / 8GB | Collaborative effort between NVIDIA & Mistral. Fine-tunes like Mini-Magnum are optimized for prose and roleplay. Best overall for 12GB cards. |
| **Gemma 3 (12B)** | **Gemma-3-12B-It** | 13GB / 8GB | Google's latest. Exceptional logic and world-building, but can feel "sanitized." Needs a strong system prompt to hit Gonzo levels of grit. |
| **Specialized (13B/14B)** | **Mistral-Small-3-2409** | 15GB / 9GB | Extremely stable for long-form narrative. Great at maintaining a specific "voice" over long sessions. |

### Specialized Creative Fine-tunes (The "Prose Kings"):
*   **Stheno (Llama 3.1 8B):** Best for visceral, fast-paced action and dialogue.
*   **Mini-Magnum (Mistral NeMo 12B):** Best for descriptive, "unhinged," and metaphor-heavy prose. This is the top recommendation for Gonzo style.
*   **MythoMax-L2-13B:** While classic, it is increasingly outperformed by Llama 3/Mistral NeMo fine-tunes in 2026. Avoid unless you specifically prefer the Llama 2 "feel."

---

## 2. Handling the "Gonzo" Style

Gonzo journalism is characterized by:
1.  **Subjective First-Person:** The narrator is the protagonist, often unreliable and deeply involved.
2.  **Visceral Metaphor:** "The sky was the color of a bruised kidney," etc.
3.  **Rhythmic Paranoia:** Staccato sentences mixed with drug-fueled, sprawling observations.
4.  **Social Commentary:** High-stakes cynicism and a "Search for the American Dream."

### Best Model for Gonzo: **Mistral NeMo 12B (Mini-Magnum)**
*   **Why:** Mistral models historically handle "edge" and "grit" better than Llama or Gemma. NeMo's 12B architecture provides enough "brain" to handle Thompson's complex vocabulary and multi-layered metaphors without becoming incoherent.
*   **Prompting Tip:** Use a system prompt that explicitly permits "hallucinatory metaphors" and "visceral first-person perspectives."

---

## 3. RAG Strategy for Style Injection

Standard RAG (Retrieval-Augmented Generation) is usually used for *fact* retrieval. For *style* injection, we need **Style-RAG**.

### The Corpus:
*   *Fear and Loathing in Las Vegas* (Primary source for rhythm/drug-culture).
*   *Hell's Angels* (Primary source for grit/observation).
*   *The Great Shark Hunt* (Anthology of style variants).
*   *Fear and Loathing on the Campaign Trail '72* (Political cynicism).

### Implementation Strategy:
1.  **Chunking (Paragraph-Based):** 
    *   Do **not** use fixed-token chunking. Thompson’s style is in the *flow* of a paragraph. 
    *   Use a `MarkdownHeaderTextSplitter` or a simple double-newline splitter to keep paragraphs intact.
2.  **Indexing:**
    *   Use a dense embedding model like `bge-small-en-v1.5` or `nomic-embed-text`.
    *   Store in a local vector DB (ChromaDB or FAISS).
3.  **Retrieval (Style-Focused):**
    *   When the user provides a topic (e.g., "The 2026 Election"), retrieve 3-5 passages from the corpus that share similar *thematic* elements (e.g., "politics," "crowds," "fear").
4.  **The Style Injection Prompt:**
    ```text
    [SYSTEM]
    You are Hunter S. Thompson in 1971. Your prose is visceral, metaphor-heavy, and deeply subjective.
    
    REFERENCE STYLE SAMPLES:
    {{retrieved_passages}}
    
    TASK:
    Write about {{user_topic}} using the rhythm, vocabulary, and cynical perspective found in the samples above.
    ```

---

## 4. Hardware Configuration Recommendation

### For RTX 3060 12GB:
*   **Model:** Mini-Magnum-12B-v1.1 (Q6_K or Q8_0)
*   **Backend:** KoboldCPP or Ollama.
*   **Context:** 8k - 16k tokens (fits comfortably in 12GB).

### For RTX 3060 6GB:
*   **Model:** Stheno-v3.2-L3-8B (Q4_K_M)
*   **Backend:** KoboldCPP (with GQA and KV cache compression enabled).
*   **Context:** 4k - 8k tokens max.

---

*Report compiled by Antigravity AI.*
