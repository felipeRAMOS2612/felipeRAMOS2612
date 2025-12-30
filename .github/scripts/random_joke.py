import json
import random
import os

# Configuración de colores Tokyo Night
COLOR_BG = "#1a1b27"
COLOR_BORDER = "#bf91f3"
COLOR_TEXT = "#c0caf5"
COLOR_ACCENT = "#70a5fd"

def get_joke():
    with open('.github/scripts/jokes.json', 'r', encoding='utf-8') as f:
        jokes = json.load(f)
    return random.choice(jokes)

def create_svg(joke):
    # Plantilla SVG simple pero bonita
    svg_template = f'''
    <svg width="500" height="120" viewBox="0 0 500 120" fill="none" xmlns="http://www.w3.org/2000/svg">
      <style>
        .text {{ font-family: 'Segoe UI', Ubuntu, Sans-Serif; font-size: 16px; fill: {COLOR_TEXT}; }}
        .border {{ stroke: {COLOR_BORDER}; stroke-width: 2; fill: {COLOR_BG}; rx: 10; }}
        .title {{ font-weight: bold; fill: {COLOR_ACCENT}; font-size: 14px; }}
      </style>
      <rect x="1" y="1" width="498" height="118" class="border"/>
      <text x="20" y="30" class="title">✨ Chiste del Día (Dev)</text>
      <foreignObject x="20" y="45" width="460" height="60">
        <div xmlns="http://www.w3.org/1999/xhtml" style="color:{COLOR_TEXT}; font-family: 'Segoe UI', sans-serif; font-size: 16px; display: flex; align-items: center; height: 100%;">
          {joke}
        </div>
      </foreignObject>
    </svg>
    '''
    
    # Guardar en la carpeta output (crearla si no existe)
    os.makedirs('output', exist_ok=True)
    with open('output/joke-es.svg', 'w', encoding='utf-8') as f:
        f.write(svg_template)

if __name__ == "__main__":
    joke = get_joke()
    create_svg(joke)
