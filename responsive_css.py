import re
import sys

def make_responsive(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Update Typography to be completely fluid using clamp()
    # H1
    css = re.sub(
        r"(h1\s*\{[^\}]*?)font-size:\s*clamp\([^)]+\);",
        r"\1font-size: clamp(2.5rem, 8vw, 4.5rem);",
        css,
        flags=re.DOTALL
    )
    # H2
    css = re.sub(
        r"(h2\s*\{[^\}]*?)font-size:\s*clamp\([^)]+\);",
        r"\1font-size: clamp(2rem, 5vw, 3.5rem);",
        css,
        flags=re.DOTALL
    )

    # 2. Refine Mobile Menu (Make it full screen and glassmorphic)
    css = re.sub(
        r"(\.mobile-menu\s*\{[^\}]*?)background:\s*var\(--secondary\);",
        r"\1background: var(--glass-bg);\n    backdrop-filter: blur(20px);\n    -webkit-backdrop-filter: blur(20px);",
        css,
        flags=re.DOTALL
    )
    css = re.sub(
        r"(\[data-theme=\"dark\"\]\s*\.mobile-menu\s*\{[^\}]*?)background:\s*[^;]+;",
        r"\1background: var(--glass-bg);",
        css,
        flags=re.DOTALL
    )
    
    # Make mobile menu take up 100% width on small screens
    css = css.replace("width: 80%;", "width: 100%;")
    css = css.replace("left: -100%;", "right: -100%; left: auto;")
    css = css.replace(".mobile-menu.active {\n    left: 0;\n}", ".mobile-menu.active {\n    right: 0;\n}")

    # 3. Enhance Grid Layouts for Mobile
    # For .about-content and .team-content
    css = re.sub(
        r"@media\s*\(\s*max-width:\s*768px\s*\)\s*\{\s*\.nav-links",
        """@media (max-width: 768px) {
    .container {
        padding: 0 1.5rem;
    }
    
    .hero {
        min-height: 100svh; /* Better support for mobile browsers */
    }
    
    .nav-links""",
        css
    )
    
    # Fix the About image on mobile
    css = re.sub(
        r"(\.about-image\s*\{[^\}]*?)height:\s*400px;",
        r"\1height: auto;\n    aspect-ratio: 4/3;",
        css,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(css)
    print("CSS responsiveness applied successfully.")

if __name__ == "__main__":
    make_responsive(sys.argv[1])
