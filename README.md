# 🚀 Azure AI Hackathon – AI Agents Workshop

Welcome to the **Azure AI Hackathon AI Agents Workshop**! This repository contains resources and code samples to help you learn how to build AI agents using various frameworks and techniques.

## 🎯 **Workshop Structure**

This workshop is divided into two main parts:

### Part 1: Hugging Face Agent Workshop

The first part of this workshop consists of completing the **Hugging Face Agent Workshop**, which provides best-in-class fundamentals to get started with AI agents. This external workshop will give you a solid foundation in agent concepts and implementation.

**💡 Bonus:** You can earn a certificate if you have a Hugging Face account when completing the workshop!

### Part 2: Semantic Kernel Samples

After completing the Hugging Face workshop, you'll explore the samples in this repository that demonstrate how to build AI agents using the **Semantic Kernel** framework.

## 📚 **Sample Notebooks**

The `samples` folder contains the following notebooks:

### 1. Basic Agent (01_semantic_kernel_basic_agent.ipynb)

This notebook demonstrates how to build a simple AI agent using **Semantic Kernel**. You'll learn:

- How to implement a basic AI agent with Semantic Kernel
- How to integrate with GitHub Copilot Models for free LLM access during development
- How to transition to Azure OpenAI Service for enterprise-grade scalability
- Best practices for designing modular AI solutions that can easily switch between LLM providers

### 2. Research Agent (02_semantic_kernel_research_agent.ipynb)

This notebook shows how to create a more advanced research-oriented agent that can:

- Process and analyze documents
- Extract key information from research papers
- Generate summaries and insights from complex content
- Perform more sophisticated reasoning tasks

## 🐳 **Development Environment**

This repository is built with **uv** and includes a **devcontainer** configuration that provides a pre-configured development environment with all the necessary dependencies installed. We recommend using one of these environments for the best experience.

### Using GitHub Codespaces

The easiest way to get started is to create a **GitHub Codespace** with the devcontainer:

1. Click on the "Code" button in the GitHub repository
2. Select the "Codespaces" tab
3. Click "Create codespace on main"

This will create a cloud-based development environment with everything you need already set up, allowing you to start working on the workshop immediately without worrying about local configuration. The devcontainer is already pre-configured and ready to go.

### Local Development

If you prefer to work locally, you'll need to:

1. Install **uv** - a fast Python package installer and resolver (https://github.com/astral-sh/uv)
2. Clone this repository to your local machine
3. Run `uv sync` in the repository root to install all dependencies

```bash
# Install uv (if you don't have it already)
# For macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows (using PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Clone the repository
git clone <repository-url>
cd <repository-directory>

# Install dependencies
uv sync
```

## 🛠️ **Getting Started**

To get the most out of this workshop:

1. Start with the Hugging Face Agent Workshop to learn the fundamentals
2. Explore the Semantic Kernel sample notebooks in order
3. Experiment with different models and parameters to understand their impact
4. Apply what you've learned to build your own custom agents

## 💡 **Key Takeaways**

By completing this workshop, you'll gain:

- Understanding of AI agent architecture and implementation
- Hands-on experience with Semantic Kernel
- Knowledge of how to design flexible, modular AI solutions
- Skills to build production-ready AI agents for real-world applications

Let's get started! 🚀
