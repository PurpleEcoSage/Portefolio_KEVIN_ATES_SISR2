import sys

def add_user_node_highlight(filepath):
    css_code = """
/* ========================================= */
/* HIGHLIGHT KEVIN ATES NODE (USER NODE)     */
/* ========================================= */
.tree li .user-node {
    border: 3px solid #f59e0b !important; /* Amber/Yellow border */
    box-shadow: 0 0 15px rgba(245, 158, 11, 0.4) !important;
    background: rgba(245, 158, 11, 0.1) !important;
    transform: scale(1.05); /* Make it stand out slightly */
    z-index: 2;
    position: relative;
    animation: pulseYellow 2s infinite !important;
}

.tree li .user-node strong {
    color: #b45309 !important; /* Darker amber text for strong element */
}
.tree li .user-node p {
    color: #d97706 !important; /* Lighter amber for P element */
    font-weight: bold;
}

[data-theme="dark"] .tree li .user-node {
    background: rgba(245, 158, 11, 0.15) !important;
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.3) !important;
}
[data-theme="dark"] .tree li .user-node strong {
    color: #fcd34d !important; /* Bright yellow/amber for dark mode */
}
[data-theme="dark"] .tree li .user-node p {
    color: #fde68a !important; 
}

@keyframes pulseYellow {
    0% {
        box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.6);
    }
    70% {
        box-shadow: 0 0 0 15px rgba(245, 158, 11, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(245, 158, 11, 0);
    }
}
"""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_code)
    print("User node highlight added.")

if __name__ == "__main__":
    add_user_node_highlight(sys.argv[1])
