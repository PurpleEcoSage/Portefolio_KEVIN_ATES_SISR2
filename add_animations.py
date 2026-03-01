import sys

def add_creative_animations(filepath):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("\n\n/* ========================================= */\n")
        f.write("/* CREATIVE ANIMATIONS (GSAP-style pure CSS) */\n")
        f.write("/* ========================================= */\n\n")

        # 1. Base animation classes
        f.write(""".gsap-reveal {
    opacity: 0;
    transform: translateY(50px);
    transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
    will-change: transform, opacity;
}

.gsap-reveal.is-visible {
    opacity: 1;
    transform: translateY(0);
}

.gsap-scale {
    opacity: 0;
    transform: scale(0.9);
    transition: all 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.gsap-scale.is-visible {
    opacity: 1;
    transform: scale(1);
}

.gsap-fade {
    opacity: 0;
    transition: opacity 1.2s ease;
}

.gsap-fade.is-visible {
    opacity: 1;
}

/* Stagger Delays for Grids */
.stagger-1 { transition-delay: 0.1s; }
.stagger-2 { transition-delay: 0.2s; }
.stagger-3 { transition-delay: 0.3s; }
.stagger-4 { transition-delay: 0.4s; }
.stagger-5 { transition-delay: 0.5s; }
.stagger-6 { transition-delay: 0.6s; }

/* 2. Magnetic Hover Effect (simulated) */
.magnetic-btn {
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease;
}

.magnetic-btn:hover {
    transform: translateY(-5px) scale(1.03);
    box-shadow: 0 15px 35px var(--primary-glow);
}

/* 3. Image Parallax/Reveal Container */
.image-reveal-container {
    overflow: hidden;
    position: relative;
    border-radius: 12px;
}

.image-reveal-container img {
    transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1);
    transform: scale(1.1);
}

.image-reveal-container.is-visible img {
    transform: scale(1);
}
.image-reveal-container:hover img {
    transform: scale(1.05); /* Interactive micro-zoom */
}

/* Animated Gradient Background for Hero */
@keyframes breathingGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero {
    background: linear-gradient(-45deg, #f8fafc, #e2e8f0, #cbd5e1, #ffffff);
    background-size: 400% 400%;
    animation: breathingGradient 15s ease infinite;
}

[data-theme="dark"] .hero {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #020617, #0f172a);
    background-size: 400% 400%;
    animation: breathingGradient 15s ease infinite;
}
""")
    print("Creative CSS animations appended successfully.")

if __name__ == "__main__":
    add_creative_animations(sys.argv[1])
