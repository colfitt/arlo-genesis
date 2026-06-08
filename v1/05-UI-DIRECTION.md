# 05 — UI Direction

**Keep the engine and the UI separate.** [04](04-USING-IT-WITH-CLAUDE.md) is the valuable, hard part and must work on its own (even if the only "UI" is the `claude` CLI). The UI is a layer that makes the engine pleasant — it should not block or define the engine.

## What you want it to feel like

An **odysseus-style workspace**: a clean, self-hosted AI-workspace look — a chat/agent surface front-and-center, a **sidebar** of your stuff (here: Gear / Software, eventually Songs), and a **documents** area. That layout — sidebar + conversation + content panels — is the target feel.

You said it directly: *"the way they built the UI is very close to what I want"* — and also *"I'm not sure this can even accomplish what I'm after."* So odysseus is **visual reference**, with engine-fit **unproven** (see [07](07-RISKS-OPEN-QUESTIONS.md)).

## Reference: `pewdiepie-archdaemon/odysseus`

- A self-hosted AI workspace (MIT). **Python (FastAPI) + JS/CSS**, Docker/GPU-deployable. Features: Chat, an opencode-based **Agent** (+ MCP), **Documents** (multi-tab editor), **Memory/Skills** (ChromaDB), RAG, local model serving, a phone **companion**.
- **What to borrow:** the *layout/UX* (sidebar + chat + documents), and its **`mcp_servers/` + ChromaDB RAG patterns** as a blueprint for [04](04-USING-IT-WITH-CLAUDE.md)'s B/C.
- **What to be wary of:** it's a *general* horizontal workspace (email/calendar/etc.), brand-new and broad, Python web stack. Using it as the **engine** drags in scope and surface you don't want for a focused music tool. Using it as **UI inspiration** is low-risk.

## Reference: the retired Tauri `patchbay-ai`

The prior app already recreated a polished music-specific UI (sidebar of Songs/Gear/Software, an embedded `claude` terminal, glass aesthetic). It's **strong visual reference** for an ARLO UI and proves the look is achievable natively. Reuse its design language; don't assume its stack.

## UI options (decide AFTER the engine works)

| Option | What | Pros | Cons |
|--------|------|------|------|
| **0. CLI only** | Just `claude` as ARLO in a terminal | Zero UI build; engine-pure | No sidebar/visuals |
| **1. Fork odysseus** | Point its UI at the folders/engine | Closest to the look you like; RAG/MCP built-in | General Python web app; fit unproven; broad surface |
| **2. Thin custom UI** | Minimal web/desktop shell (sidebar + chat) over the engine | Music-specific, controllable; reuse Tauri design | You build it |
| **3. odysseus as UI, ARLO as the agent** | Run odysseus, register ARLO (persona+skills+MCP) as its agent, sidebar = your folders | Best-of-both *if* it composes | Depends on odysseus's extensibility — verify |

**Suggested path:** prove the engine (Option 0 is enough to validate). Then **spike Option 3** — can odysseus host ARLO as its agent and show your folders in the sidebar? If yes, you get the look cheaply. If it fights you, fall back to **Option 2** with the Tauri design language.

## The open UI question to answer in a spike

> Does the UI need to *do music things* (render skeleton grids, patch editors, gear drawers — like the Tauri prototype), or is it **chat + a sidebar of my gear + documents** (what odysseus gives)?

If it's the former, a custom UI (Option 2) is likelier. If the latter, odysseus (Option 1/3) may genuinely be close. **This is the single most important UI question** and should be settled before investing in any UI build.
