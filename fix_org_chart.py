import sys

def fix_org_chart(filepath):
    with open(filepath, 'a', encoding='utf-8') as f:
        # Append specific mobile fixes for the org chart
        f.write("\n\n/* ========================================= */\n")
        f.write("/* ORG CHART MOBILE RESPONSIVENESS FIXES */\n")
        f.write("/* ========================================= */\n\n")

        f.write("""
/* Ensure the container gracefully handles horizontal scrolling on small screens */
.org-chart-container {
    width: 100%;
    margin-top: 3rem;
    padding: 1.5rem;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 12px;
    box-shadow: var(--glass-shadow);
    /* Prevent cutting off shadow and allow horizontal scrolling */
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; /* Smooth scroll on iOS */
}

/* Ensure the tree itself shrinks and doesn't break layout */
.tree {
    display: inline-block;
    min-width: 100%; /* Take up at least 100% to allow centering, but can grow if needed */
    padding-bottom: 2rem;
}

.tree ul {
    /* Adding some padding to prevent nodes from hitting the edges when scrolling */
    padding-top: 20px; 
    position: relative;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
}

/* Adjust the nodes to be slightly smaller and stack better on mobile */
@media (max-width: 900px) {
    .tree li {
        padding: 15px 2px 0 2px;
    }
    
    .tree li::before, .tree li::after {
        top: 0;
    }
    
    .tree li .node {
        padding: 10px;
        min-width: 120px; /* Reduce minimum width */
        font-size: 0.85rem;
    }
    
    .tree li .node strong {
        font-size: 0.95rem;
    }
    
    /* Specific adjustment for the PDG node and root branches */
    .tree > ul > li {
        padding-top: 0;
    }
}

/* On very small devices, switch to a vertical stacked list approach for deep branches */
/* But since it's an org chart, horizontal scroll with touch is usually the best UX */
/* We rely on the overflow-x: auto from .org-chart-container */

""")
    print("Org chart responsiveness fixes appended.")

if __name__ == "__main__":
    fix_org_chart(sys.argv[1])
