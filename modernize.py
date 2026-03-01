import re
import sys

def modernize_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Update variables
    root_vars = """:root {
    --primary: #E63946;
    --primary-glow: rgba(230, 57, 70, 0.4);
    --secondary: #ffffff;
    --dark: #0f172a;
    --gray: #64748b;
    --light-gray: #f8fafc;
    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(255, 255, 255, 0.5);
    --glass-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
    --font-heading: 'Outfit', sans-serif;
    --font-body: 'Inter', sans-serif;
}

[data-theme="dark"] {
    --secondary: #0f172a;
    --dark: #f8fafc;
    --gray: #94a3b8;
    --light-gray: #1e293b;
    --glass-bg: rgba(15, 23, 42, 0.6);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
}"""

    css = re.sub(
        r':root\s*\{.*?\}.*?\[data-theme="dark"\]\s*\{.*?\}',
        root_vars,
        css,
        flags=re.DOTALL
    )

    # 2. Update fonts globally
    css = re.sub(r"font-family:\s*'Montserrat'[^;]*;", "font-family: var(--font-heading);", css)
    
    css = re.sub(
        r"body\s*\{[^\}]*font-family:[^\}]*\}",
        """body {
    font-family: var(--font-body);
    font-weight: 400;
    color: var(--dark);
    line-height: 1.7;
    overflow-x: hidden;
    background: var(--secondary);
    transition: background-color 0.4s ease, color 0.4s ease;
}""",
        css,
        flags=re.DOTALL
    )

    # 3. Add glassmorphism to components
    # Nav
    css = css.replace("backdrop-filter: blur(10px);", "backdrop-filter: blur(16px); border-bottom: 1px solid var(--glass-border);")
    css = css.replace("-webkit-backdrop-filter: blur(10px);", "-webkit-backdrop-filter: blur(16px);")
    
    # Cards (Service, Portfolio, Pricing, Contact, Testimonial)
    card_selectors = [
        ".service-card", ".portfolio-item", ".pricing-card", 
        ".contact-form", ".testimonial-card", ".project-card"
    ]
    
    for selector in card_selectors:
        css = re.sub(
            rf"({selector}\s*\{{[^\}}]*?)background:\s*var\(--secondary\);",
            r"\1background: var(--glass-bg);\n    backdrop-filter: blur(12px);\n    -webkit-backdrop-filter: blur(12px);\n    border: 1px solid var(--glass-border);\n    box-shadow: var(--glass-shadow);",
            css,
            flags=re.DOTALL
        )
        css = re.sub(
            rf"(\[data-theme=\"dark\"\]\s*{selector}\s*\{{[^\}}]*?)background:\s*#[0-9a-fA-F]+;",
            r"\1background: var(--glass-bg);\n    border-color: var(--glass-border);",
            css,
            flags=re.DOTALL
        )

    # 4. Hero section gradients
    css = re.sub(
        r"(\.hero\s*\{[^\}]*?)background:\s*linear-gradient[^;]+;",
        r"\1background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);\n    position: relative;",
        css,
        flags=re.DOTALL
    )
    css = re.sub(
        r"(\[data-theme=\"dark\"\]\s*\.hero\s*\{[^\}]*?)background:\s*linear-gradient[^;]+;",
        r"\1background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);",
        css,
        flags=re.DOTALL
    )
    
    # 5. Buttons Glow
    css = re.sub(
        r"(\.cta-button\s*\{[^\}]*?)box-shadow:\s*[^;]+;",
        r"\1box-shadow: 0 10px 30px var(--primary-glow);",
        css,
        flags=re.DOTALL
    )
    css = re.sub(
        r"(\.cta-button:hover\s*\{[^\}]*?)box-shadow:\s*[^;]+;",
        r"\1box-shadow: 0 20px 50px var(--primary-glow);",
        css,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(css)

    print("CSS modernized successfully.")

if __name__ == "__main__":
    modernize_css(sys.argv[1])
