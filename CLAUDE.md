
## Repository Overview

This is an Obsidian vault containing comprehensive notes on AI, Machine Learning, and Data Science concepts. All notes are written in Markdown and organized hierarchically by topic. The vault serves as a personal knowledge base (Hypomnemata) tracking important concepts, research papers, and technical explanations.

## Directory Structure

```
AI/
├── Machine Learning & Data Science/
│   ├── Architecture/          # Neural network architectures (Transformers, RNNs, LSTMs, etc.)
│   ├── Natural Language Processing/
│   ├── Reinforcement Learning/
│   ├── Supervised Learning/
│   ├── Unsupervised Learning/
│   ├── Probability/
│   ├── Statistics/
│   ├── Vector Search/
│   ├── Performance Metrics/
│   ├── Distance Metrics/
│   ├── Large Language Models/
│   ├── Parameter-Efficient Fine-Tuning/
│   └── ... (additional subdirectories)
│
├── Research Paper Explanations/
│   ├── Parameter Efficient Fine Tuning/
│   ├── Representation Learning/
│   ├── Transformers/
│   ├── Upcycling/
│   └── Individual paper notes (.md files)
│
└── media/                     # Images and diagrams referenced in notes
```

## Working with this Vault

### Obsidian-Specific Conventions

- **Wiki-style links**: Notes use `[[Note Title]]` syntax for internal linking
- **Forward and backward links**: Obsidian tracks bidirectional relationships between notes
- **Embedded images**: Images are referenced using `![[image.png]]` syntax and stored in `media/` or `AI/media/`
- **Section links**: Use `[[Note#Section]]` to link to specific sections

### Content Organization

- Each major topic area has a `README.md` that provides an overview
- Notes are atomic: each file focuses on a single concept or paper
- Research paper notes include links to original papers and aim for comprehensive explanations with images and diagrams
- Conceptual notes range from foundational (e.g., "Basics.md") to advanced topics (e.g., "RLHF.md")

### Markdown Conventions

- Notes use standard GitHub-flavored Markdown
- Mathematical notation may be present using LaTeX syntax (`$...$` for inline, `$$...$$` for blocks)
- Code blocks use triple backticks with language specifiers
- Notes may include embedded images using Obsidian's `![[]]` syntax

### Writing Style and Formatting Rules

**Do NOT:**
- Add a top-level heading to notes (the filename serves as the title)
- Use em dashes (—) in content
- Use horizontal rules (`---`) between sections
- Add newlines before or after headings (Markdown renderers handle spacing automatically)
- Add unnecessary blank lines elsewhere in the document
- Create a "Related Notes" or "See Also" section at the bottom

**Do:**
- Use British English spelling and conventions
- Use Obsidian-style wiki-links (`[[Note Title]]`) to reference other notes in the vault
- Integrate links naturally within the prose, not as separate link lists
- Keep formatting clean and minimal

### Git Configuration

- `.gitignore` excludes: `.DS_Store`, `._*` (Apple resource forks), and `.obsidian/` (Obsidian settings)
- The vault is version controlled with Git
- Untracked files in git status indicate new notes being drafted

## Common Tasks

### Adding New Notes

When creating new notes:
- Place in the appropriate subdirectory based on topic
- Use clear, descriptive filenames (e.g., "Thompson Sampling.md", not "ts.md")
- Add a `README.md` if creating a new subdirectory
- Use wiki-links to connect to related concepts
- For research papers, include author, year, and paper title in the filename

### Editing Existing Notes

- Preserve existing link structure when renaming or reorganizing
- Maintain consistency with existing formatting conventions
- Keep mathematical notation and code examples properly formatted
- Ensure embedded images remain accessible

### Finding Content

- Search by topic: notes are organized hierarchically by subject area
- Check README files for directory overviews
- Related concepts are linked using wiki-links
- Research papers are in `AI/Research Paper Explanations/`
- Conceptual notes are in `AI/Machine Learning & Data Science/`

## Note-Taking Philosophy

This vault follows the Hypomnemata approach - capturing important learnings and concepts for future reference. Notes emphasize:
- Clarity and comprehensiveness over brevity
- Visual aids (diagrams, images) to enhance understanding
- Connections between concepts through linking
- Both theoretical foundations and practical applications
