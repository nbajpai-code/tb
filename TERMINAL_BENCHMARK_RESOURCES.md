# Terminal Benchmark Resources for LLM/Agent Evaluation

A curated list of benchmarks, frameworks, datasets, and tools for evaluating Large Language Models (LLMs) and AI Agents in terminal and command-line environments.

---

## 📊 Major Benchmarks

### Terminal-Bench
**Focus:** Terminal mastery and command-line operations

- **Description:** Open-source benchmark for evaluating AI agents' ability to perform complex tasks within terminal environments. Created by Stanford University and Laude Institute.
- **Tasks:** ~100 challenging tasks including code compilation, ML model training, server setup, and system debugging
- **Environment:** Docker-containerized environments with verification scripts
- **Website:** [tbench.ai](https://tbench.ai)
- **GitHub:** [Terminal-Bench](https://github.com/terminal-bench/terminal-bench)
- **Key Features:**
  - Real-world, end-to-end terminal operations
  - Systematic step-by-step reasoning
  - Comprehensive task verification
  - Reference solutions included

### SWE-bench (Software Engineering Benchmark)
**Focus:** Real-world software engineering tasks

- **Description:** Evaluates LLMs on resolving real-world GitHub issues from open-source projects
- **Tasks:** Generate patches to fix described problems in actual codebases
- **Variants:**
  - SWE-bench Lite
  - SWE-bench Verified
  - SWE-bench Multimodal
- **Website:** [swebench.com](https://swebench.com)
- **GitHub:** [SWE-bench](https://github.com/princeton-nlp/SWE-bench)
- **Key Features:**
  - Docker-based reproducible evaluations
  - Real GitHub issues
  - Multi-file coordination testing
  - Python codebase navigation

### AgentBench
**Focus:** Multi-environment agent evaluation

- **Description:** Comprehensive benchmarking suite evaluating LLMs as agents across 8 diverse interactive environments
- **Capabilities Tested:**
  - Reasoning and decision-making
  - Tool usage and collaboration
  - Information synthesis
  - Multi-step planning
- **GitHub:** [AgentBench](https://github.com/THUDM/AgentBench)
- **Paper:** [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)
- **Key Features:**
  - Multi-turn, open-ended settings
  - OS interaction tasks
  - Containerized deployment support

### OSWorld
**Focus:** Real computer environment interactions

- **Description:** Scalable benchmark for multimodal agents in actual operating systems (Ubuntu, Windows, macOS)
- **Tasks:** 369 real-world computer tasks with complex multi-application workflows
- **Input:** Realistic mouse and keyboard events
- **Website:** [os-world.github.io](https://os-world.github.io)
- **Paper:** [arXiv:2404.07972](https://arxiv.org/abs/2404.07972)
- **Key Features:**
  - Task setup and execution-based evaluation
  - Interactive learning support
  - GUI grounding assessment
  - Human performance baselines

### GAIA (General AI Assistants)
**Focus:** Real-world assistant capabilities

- **Description:** Benchmark for testing fundamental AI assistant skills with unambiguous factual answers
- **Dataset:** 466 curated questions across 3 difficulty levels
- **Developers:** Meta-FAIR, Meta-GenAI, Hugging Face, AutoGPT
- **Leaderboard:** [Hugging Face GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
- **Dataset:** [Hugging Face Dataset](https://huggingface.co/datasets/gaia-benchmark/GAIA)
- **Paper:** [arXiv:2311.12983](https://arxiv.org/abs/2311.12983)
- **Key Features:**
  - Multi-modality understanding
  - Web browsing and tool use
  - Strategic planning
  - Human baseline: ~92% accuracy

---

## 🌐 Web & Interactive Benchmarks

### WebArena
**Focus:** Autonomous web navigation and task completion

- **Description:** Realistic web environment with functional websites across multiple categories
- **Domains:** E-commerce, social forums, software development, content management
- **Tools:** Maps, calculators, Wikipedia integration
- **Website:** [webarena.dev](https://webarena.dev)
- **Key Features:**
  - Self-hosted environments
  - Complex multi-step web tasks
  - Realistic human-web interaction simulation

### τ-bench (tau-bench)
**Focus:** Dynamic conversational scenarios with policy adherence

- **Description:** Evaluates agents in multi-turn dialogues with domain-specific API tools and policies
- **Domains:** Retail, airline, telecom (τ²-bench extension)
- **Website:** [taubench.com](https://taubench.com)
- **Paper:** [arXiv:2406.12045](https://arxiv.org/abs/2406.12045)
- **Key Features:**
  - Multi-turn interaction simulation
  - Policy compliance testing
  - LLM-based user simulator
  - Objective database state evaluation

### InterCode
**Focus:** Interactive code execution environments

- **Description:** Benchmark for digital agents with interactive coding capabilities
- **Website:** [intercode-benchmark.github.io](https://intercode-benchmark.github.io)
- **Key Features:**
  - Interactive execution feedback
  - Multi-turn code refinement
  - Environment state management

---

## 🛠️ Frameworks & Tools

### cline-bench (Terminal-Bench 2.0)
**Focus:** High-fidelity benchmarks from real development scenarios

- **Description:** Creates benchmarks and RL environments from open-source development
- **Website:** [cline.bot](https://cline.bot)
- **Key Features:**
  - Real-world development scenarios
  - Reinforcement learning support
  - Human-verified tasks

### Super CLI
**Focus:** Agent-native command-line interface

- **Description:** Unified workflow for developing, evaluating, and optimizing AI agents
- **Supported Ecosystems:**
  - DSPy
  - OpenAI SDK
  - CrewAI
  - Google ADK
  - Microsoft Agent Framework
  - DeepAgents
- **Website:** [super-agentic.ai](https://super-agentic.ai)
- **Key Features:**
  - Behavioral specification definitions
  - GEPA optimizer (Genetic-Pareto Algorithm)
  - Multi-framework support

### Google ADK (Agent Development Kit)
**Focus:** Agent development and evaluation tools

- **Description:** Command-line tools for running agent evaluations
- **Command:** `adk eval` for evaluation execution
- **Documentation:** [Google ADK Docs](https://google.github.io/adk/)
- **Key Features:**
  - Tool trajectory matching
  - LLM-judged response quality
  - CI/CD integration

### DeepEval
**Focus:** Open-source LLM evaluation framework

- **Description:** Framework for evaluating LLMs and agents with CI/CD support
- **Website:** [deepeval.com](https://deepeval.com)
- **Key Features:**
  - End-to-end task evaluation
  - Component-level metrics
  - Pipeline integration
  - Multiple evaluation metrics

---

## 📚 Additional Resources

### Research Papers

1. **Terminal-Bench: A Benchmark for AI Agents in Terminal Environments**
   - Authors: The Terminal-Bench Team (Stanford, Laude)
   - Focus: Terminal mastery evaluation

2. **AgentBench: Evaluating LLMs as Agents**
   - [arXiv:2308.03688](https://arxiv.org/abs/2308.03688)
   - Focus: Multi-environment agent capabilities

3. **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments**
   - [arXiv:2404.07972](https://arxiv.org/abs/2404.07972)
   - Focus: Real OS interaction

4. **GAIA: A Benchmark for General AI Assistants**
   - [arXiv:2311.12983](https://arxiv.org/abs/2311.12983)
   - Focus: General assistant capabilities

5. **τ-bench: A Benchmark for Tool-Augmented LLMs**
   - [arXiv:2406.12045](https://arxiv.org/abs/2406.12045)
   - Focus: Policy-aware conversational agents

### AI Coding Agents (CLI)

- **Gemini CLI** - Polished UX, multi-file context
- **Claude Code CLI** - Code diffing, legacy analysis
- **OpenAI Codex CLI** - Accuracy and creativity
- **ForgeCode** - Fast local development
- **Aider** - Git-savvy, customizable

---

## 📊 Evaluation Metrics

### Common Metrics Across Benchmarks

1. **Task Success Rate** - Percentage of successfully completed tasks
2. **Tool Use Trajectory** - Correctness of tool call sequences
3. **Reasoning Quality** - Problem decomposition and planning
4. **Context Management** - Multi-turn interaction handling
5. **Policy Adherence** - Following domain-specific rules
6. **Efficiency** - Response time and resource usage
7. **Robustness** - Performance under adversarial conditions

---

## 🎯 Key Capabilities Evaluated

### Terminal & Command-Line Skills
- Shell command execution
- File system navigation
- System configuration
- Package management
- Process management

### Coding & Development
- Code generation and understanding
- Bug fixing and debugging
- Multi-file coordination
- Version control operations
- Build system interaction

### Reasoning & Planning
- Multi-step task decomposition
- Sequential decision making
- Error recovery
- State management
- Goal-oriented behavior

### Tool & API Usage
- External tool integration
- API calling and parsing
- Function calling accuracy
- Tool selection and chaining

### Multi-modal Interaction
- Text understanding and generation
- GUI interaction (OSWorld)
- Image/document processing
- Web browsing

---

## 🔗 Useful Links

- **Terminal-Bench Leaderboard:** [tbench.ai](https://tbench.ai)
- **SWE-bench Leaderboard:** [swebench.com](https://swebench.com)
- **GAIA Leaderboard:** [Hugging Face](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
- **AgentBench GitHub:** [THUDM/AgentBench](https://github.com/THUDM/AgentBench)
- **OSWorld Project:** [os-world.github.io](https://os-world.github.io)

---

## 📖 Related Benchmarks

### Other Notable Benchmarks
- **ToolLLM** - Advanced API and tool usage training
- **ToolEmu** - Risk behavior identification in tool usage
- **OSWorld-Human** - Efficiency-focused computer-use evaluation

---

## 🤝 Contributing

This is a living document. Contributions are welcome! Please submit pull requests with:
- New benchmarks or frameworks
- Updated links or information
- Additional evaluation metrics
- Research papers and resources

---

## 📝 License

This resource compilation is provided for educational and research purposes.

---

**Last Updated:** November 2025
**Maintained by:** [@nbajpai-code](https://github.com/nbajpai-code)
