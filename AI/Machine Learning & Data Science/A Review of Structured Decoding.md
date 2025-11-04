LLMs, by default, output unstructured or unconstrained text (constrained only by the tokens available in the decoder). This poses a significant problem when you try to use LLMs to automate tasks requiring calls to existing software interfaces which require structured inputs like JSON. 

Functionality like OpenAI's [function calling](https://platform.openai.com/docs/guides/function-calling#how-it-works) or Anthropics [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) rely heavily on structured decoding to work reliably.
## Prompting
The simplest solution is to just include the required schema of the response in the system prompt. This can work somewhat well with large models trained on this kind of data specifically, but LLMs are known to hallucinate and not follow these kinds of instructions perfectly. For more complex schemas with specific types, enums, etc. the failure rate with this approach can be high. 
## Constrained/Structured Decoding 
With structured decoding you force the LLM to only output certain tokens by limiting the token pool it can sample from. 

A very simple example of this is [JSON Mode](https://platform.openai.com/docs/guides/structured-outputs#json-mode) where a set of rules are used to force the model to only output valid JSON. For example, when the LLM generates it's first token in the response, it will literally only be able to sample `[` or `{` since those are the only valid ways to start a JSON body. 

We can take this further using something like [JSON Schema](https://json-schema.org/) which enables more complex schema definitions with typing and enums. Now, when the LLM is decoding the value corresponding to a specific field, it might only be able to sample digits if the type of that field is integer. 
## Affect on Performance
There are some open questions around how structured decoding affects the accuracy of LLM responses. The [Speak Freely paper](https://arxiv.org/pdf/2408.02442) seems to indicate that there is a significant degradation in performance when using structured decoding vs natural responses.  However, [this blog by .txt](https://blog.dottxt.ai/say-what-you-mean.html) highlights some severely flawed methodology used when obtaining the results in the paper, and shows the opposite effect on their own benchmarks. Overall, there doesn't seem to be much consensus on the affects of structured decoding on performance.
## Context-Free Grammars (CFGs) and Extended Backus-Naur Form
Context-free grammars (CFGs) and Extended Backus-Naur Form (EBNF) are foundational tools in defining formal languages, including the schemas and response formats used in structured decoding by LLM providers. They serve as the underlying formalism for specifying precise, unambiguous syntax rules, which can be translated into schemas or constraints guiding the model's output.
#### CFGs and EBNF as Formal Specifications
- **CFGs** are a type of formal grammar used to describe the syntax of programming languages and data formats. They specify production rules for symbol sequences, ensuring the structure'scorrectness.
- **EBNF** is an extension of CFGs that simplifies their notation with additional constructs—such as optional elements, repetitions, and alternations—making the grammar more readable and expressive.