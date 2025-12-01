#!/usr/bin/env python3
"""
Auto-update README.md for the LLM Benchmarking Tasks repository.
This script generates a README with metadata and table of contents.
"""

import os
import re
from datetime import datetime
from pathlib import Path


def extract_table_of_contents(markdown_file):
    """Extract the table of contents from the markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the TOC section
    toc_match = re.search(r'## Table of Contents\n\n(.*?)\n##', content, re.DOTALL)
    if toc_match:
        return toc_match.group(1).strip()
    return ""


def count_tasks(markdown_file):
    """Count the number of tasks in the benchmarking file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count main sections (tasks)
    main_sections = re.findall(r'^## \d+', content, re.MULTILINE)
    # Count subsections (test cases)
    subsections = re.findall(r'^### \d+\.\d+', content, re.MULTILINE)
    
    return len(main_sections), len(subsections)


def get_file_stats(markdown_file):
    """Get file statistics."""
    path = Path(markdown_file)
    size_bytes = path.stat().st_size
    size_kb = size_bytes / 1024
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = len(f.readlines())
    
    return {
        'size_kb': f"{size_kb:.1f}",
        'lines': lines
    }


def generate_readme():
    """Generate the README.md file."""
    
    benchmarking_file = 'LLM_Benchmarking_Tasks.md'
    
    # Extract information
    toc = extract_table_of_contents(benchmarking_file)
    main_tasks, subtasks = count_tasks(benchmarking_file)
    stats = get_file_stats(benchmarking_file)
    
    # Get current timestamp
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    # Generate README content
    readme_content = f"""# LLM Benchmarking Tasks

> **Terminal-Based Evaluation Framework for Large Language Models**

[![Auto-Update README](https://github.com/nbajpai-code/tb/actions/workflows/update-readme.yml/badge.svg)](https://github.com/nbajpai-code/tb/actions/workflows/update-readme.yml)

## 📊 Overview

This repository contains a comprehensive set of terminal-based benchmarking tasks designed to evaluate Large Language Models (LLMs) across various capabilities:

- **Code Generation & Refinement** - Python function generation, bug fixing, and code explanation
- **Text Generation & Manipulation** - Creative writing, summarization, and paraphrasing
- **Reasoning & Logic** - Mathematical problem solving, logical deduction, and common sense reasoning
- **Information Retrieval & Q&A** - Fact retrieval and contextual question answering
- **Language Understanding** - Sentiment analysis, NER, and translation
- **Long-Context Processing** - Document summarization and complex question answering

## 📈 Repository Statistics

| Metric | Value |
|--------|-------|
| **Main Task Categories** | {main_tasks} |
| **Individual Tasks** | {subtasks} |
| **Document Size** | {stats['size_kb']} KB |
| **Total Lines** | {stats['lines']:,} |
| **Last Updated** | {timestamp} |

## 📋 Table of Contents

{toc}

## 🚀 Getting Started

### View the Full Documentation

The complete benchmarking tasks with detailed instructions, test cases, and evaluation criteria are available in:

**[📄 LLM_Benchmarking_Tasks.md](LLM_Benchmarking_Tasks.md)**

### Using the Benchmarks

Each task in the documentation includes:

1. **Objective** - What capability is being evaluated
2. **Instructions** - Clear task description for the LLM
3. **Test Cases** - Specific inputs and expected outputs
4. **Evaluation Criteria** - How to assess LLM performance
5. **Solution Strategies** - Guidance for human evaluators

### Task Categories

The benchmarks are organized into six main categories, each targeting different aspects of LLM capabilities:

1. **Code Generation & Refinement** - Evaluates programming ability
2. **Text Generation & Manipulation** - Tests creative and technical writing
3. **Reasoning & Logic** - Assesses problem-solving capabilities
4. **Information Retrieval & Q&A** - Measures knowledge access and comprehension
5. **Language Understanding & NLU** - Tests linguistic analysis skills
6. **Long-Context Understanding** - Evaluates handling of extended documents

## 🎯 Use Cases

These benchmarks are designed for:

- **Model Evaluation** - Systematic assessment of LLM capabilities
- **Comparative Analysis** - Benchmarking different models against standardized tasks
- **Research & Development** - Identifying strengths and weaknesses in LLM architectures
- **Quality Assurance** - Validating model performance before deployment
- **Terminal-Based Testing** - Reproducible evaluation in command-line environments

## 📝 Contributing

Contributions are welcome! If you have suggestions for additional benchmarking tasks or improvements to existing ones, please feel free to open an issue or submit a pull request.

## 📄 License

This project is open source and available for use in LLM evaluation and research.

---

*This README is automatically updated by GitHub Actions. Last generated: {timestamp}*
"""
    
    # Write README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README.md updated successfully!")
    print(f"   - Main tasks: {main_tasks}")
    print(f"   - Subtasks: {subtasks}")
    print(f"   - File size: {stats['size_kb']} KB")
    print(f"   - Timestamp: {timestamp}")


if __name__ == '__main__':
    generate_readme()
