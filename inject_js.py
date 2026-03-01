import re
import sys

def inject_js_animations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the Scroll Reveal JS Logic
    old_observer = """        // Scroll reveal animations (already implemented)
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1
        });

        document.querySelectorAll('section').forEach(section => {
            observer.observe(section, {
                rootMargin: '0px 0px -100px 0px'
            });
        });"""

    new_observer = """        // ----------------------------------------------------
        // ADVANCED SCROLL ANIMATIONS (Intersection Observer)
        // ----------------------------------------------------
        const revealOptions = {
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Optional: observer.unobserve(entry.target); // Uncomment to animate only once
                } else {
                    // Remove to re-animate when scrolling back up
                    entry.target.classList.remove('is-visible');
                }
            });
        }, revealOptions);

        // Apply observer to all elements with animation classes
        document.querySelectorAll('.gsap-reveal, .gsap-scale, .gsap-fade').forEach(el => {
            revealObserver.observe(el);
        });
        
        // Keep original section observer for compatibility 
        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('section').forEach(section => sectionObserver.observe(section));
"""

    html = html.replace(old_observer, new_observer)

    # 2. Add classes to elements dynamically for the effect
    # Hero elements
    html = html.replace('<h1', '<h1 class="gsap-reveal"')
    html = html.replace('<p class="subtitle"', '<p class="subtitle gsap-reveal stagger-1"')
    html = html.replace('<div class="cta"', '<div class="cta gsap-scale stagger-2"')
    
    # Section Headers
    html = html.replace('<h2>', '<h2 class="gsap-reveal">')
    
    # Portfolio / Service Grids
    html = html.replace('<div class="portfolio-item">', '<div class="portfolio-item gsap-reveal">')
    html = html.replace('<div class="project-card">', '<div class="project-card gsap-reveal">')
    
    # About
    html = html.replace('<div class="about-text">', '<div class="about-text gsap-fade">')
    html = html.replace('<div class="about-image">', '<div class="about-image image-reveal-container gsap-scale">')

    # Add magnetic class to buttons
    html = html.replace('class="cta-button"', 'class="cta-button magnetic-btn"')
    html = html.replace('class="portfolio-link"', 'class="portfolio-link magnetic-btn"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("Animation JS injected into HTML successfully.")

if __name__ == "__main__":
    inject_js_animations(sys.argv[1])
