"""
FlashBoss Centralized Color System
Provides the unified color palette for all FlashBoss modules
"""

# Midnight Purple background - the "infinite ink" that persists through RESETs
BG_THEME = '\033[48;2;23;20;33m'

def get_flashboss_colors():
    """
    FlashBoss Final Simplified Color Palette
    """
    return {
        # =============================================
        # CORE PALETTE (Moon Theme)
        # =============================================
        "MOON_CREAM": "\033[38;5;230m",    # Primary readable text
        "CORAL": "\033[38;2;200;130;130m",  # Washed chalk red
        
        # =============================================
        # NEUTRALS
        # =============================================
        "WHITE": "\033[97m",               # High contrast fallback (text)
        "WHITE_BG": "\033[47m",            # White background for speech bubbles
        "GREY": "\033[38;5;245m",          # Subtle hints, "coming soon" features
        "GUNMETAL": "\033[38;5;249m",      # Light gunmetal for emoji fallback symbols (**)
        
        # =============================================
        # GERMAN ARTICLES (Simplified)
        # =============================================
        "ARTICLE_MASC": "\033[38;2;100;135;170m",  # der (masculine) - prussian blue (more pigment)
        "ARTICLE_FEM": "\033[38;2;180;150;175m",  # die (feminine) - dusty chalk pink-purple
        "ARTICLE_NEUTER": "\033[38;2;170;200;190m", # das (neuter) - pale atlantic green
        
        # =============================================
        # CUSTOM INK COLORS (True Color)
        # =============================================
        # Uses RGB values for consistent display across terminals
        "GREEN": "\033[38;2;130;190;130m",  # Sage chalk green
        "YELLOW": "\033[38;2;255;235;128m",  # Washed chalk gold
        "RED": "\033[38;2;200;130;130m",   # Washed chalk red
        "CYAN": "\033[38;2;140;180;200m",  # Soft sky blue

        # =============================================
        # LEGACY COMPATIBILITY
        # =============================================
        "BLUE": "\033[38;2;100;135;170m",   # Prussian blue (more pigment)
        "MAGENTA": "\033[38;2;180;150;175m",  # Dusty chalk pink-purple
        "BOLD": "\033[1m",                 # Never changed
        "RESET": "\033[0m" + BG_THEME      # Standard reset + re-apply background
    }

def _color_single_article(article, colors):
    """Color a single article (no slashes)."""
    # German articles
    if article == "der":
        return f"{colors['ARTICLE_MASC']}{article}{colors['RESET']}"
    elif article == "die":
        return f"{colors['ARTICLE_FEM']}{article}{colors['RESET']}"
    elif article == "das":
        return f"{colors['ARTICLE_NEUTER']}{article}{colors['RESET']}"
    # Spanish articles (masculine = blue, feminine = purple)
    elif article in ("el", "los"):
        return f"{colors['ARTICLE_MASC']}{article}{colors['RESET']}"
    elif article in ("la", "las"):
        return f"{colors['ARTICLE_FEM']}{article}{colors['RESET']}"
    # Italian articles (masculine = blue, feminine = purple)
    elif article in ("il", "lo", "i", "gli"):
        return f"{colors['ARTICLE_MASC']}{article}{colors['RESET']}"
    elif article in ("la", "le"):
        return f"{colors['ARTICLE_FEM']}{article}{colors['RESET']}"
    # Any other article: just return it in bold
    elif article:
        return f"{colors['BOLD']}{article}{colors['RESET']}"
    else:
        return ""


def get_italian_elided_display(article, target_word, elides, colors):
    """
    Get the display string for Italian cards handling elision.

    When Elides is true, displays l' + word with l' colored by gender:
    - lo (masculine) -> blue l'
    - la (feminine) -> magenta l'

    Args:
        article: The unelided article (il, lo, la, i, gli, le)
        target_word: The target word
        elides: Boolean indicating if elision applies
        colors: Color dictionary

    Returns:
        Tuple of (display_article, display_word, visible_article_length)
        - display_article: colored article string for display
        - display_word: the word (unchanged)
        - visible_article_length: length for layout calculations (e.g., 2 for "l'")
    """
    if elides:
        # Elision case: display as l' with color based on underlying gender
        if article == "lo":
            # Masculine elision -> blue l'
            colored_article = f"{colors['ARTICLE_MASC']}l'{colors['RESET']}"
        elif article == "la":
            # Feminine elision -> magenta l'
            colored_article = f"{colors['ARTICLE_FEM']}l'{colors['RESET']}"
        else:
            # Unexpected elision case - fall back to bold
            colored_article = f"{colors['BOLD']}l'{colors['RESET']}"
        return colored_article, target_word, 2  # "l'" is 2 visible characters
    else:
        # No elision: use standard article coloring
        colored_article = _color_single_article(article, colors)
        return colored_article, target_word, len(article) if article else 0

def get_article_color(article, colors):
    """
    Article color function supporting German, Spanish, and Italian articles.
    German: der (masc), die (fem), das (neuter)
    Spanish: el (masc), la (fem), los (masc pl), las (fem pl)
    Italian: il, lo, i, gli (masc), la, le (fem)
    Compound articles (der/die, der/das, el/la, etc.): each part colored separately
    Other languages: returns article in bold

    Note: For Italian elision (l' before vowels), use get_italian_elided_display() instead.
    """
    if not article:
        return ""

    # Handle compound articles like "der/die", "der/das"
    if "/" in article:
        parts = article.split("/")
        colored_parts = []
        for part in parts:
            colored_parts.append(_color_single_article(part.strip(), colors))
        # Join with neutral-colored slash
        return "/".join(colored_parts)

    # Single article
    return _color_single_article(article, colors)

def get_colors(flashcards=None):
    """
    Simplified color system with force color mode support
    If no flashcards provided, tries to get from main module
    """
    # Get base colors
    base_colors = get_flashboss_colors()
    
    # If flashcards not provided, try to get from main module
    if flashcards is None:
        try:
            import main
            flashcards = getattr(main, 'flashcards', None)
        except ImportError:
            pass
    
    return base_colors