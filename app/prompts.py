EXPLAIN_CODE_PROMPT = """
You are an expert code explainer. Analyze the following {language} code and provide a detailed explanation.

Code:
```
{code}
```

Return your response as valid JSON with this exact structure:
{{
  "explanation": "Detailed explanation of what the code does",
  "improvements": "List of strings with Improvement suggestions (optional)",
  "edge_cases": "List of strings with Edge cases discussions if any (optional)"
}}

Important: Return ONLY valid JSON, no markdown formatting or code blocks.
"""