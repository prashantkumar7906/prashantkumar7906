import os

def create_hero_banner():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 640" width="1920" height="640" style="background:#0E1525; font-family:'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <!-- Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090D18" />
      <stop offset="50%" stop-color="#0E1525" />
      <stop offset="100%" stop-color="#111827" />
    </linearGradient>
    
    <linearGradient id="warmGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF8A3D" />   <!-- Primary Orange -->
      <stop offset="50%" stop-color="#FFB347" />  <!-- Secondary Orange -->
      <stop offset="100%" stop-color="#F6C667" /> <!-- Accent Saffron -->
    </linearGradient>

    <linearGradient id="glassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.01" />
    </linearGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF8A3D" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#F6C667" stop-opacity="0.3" />
    </linearGradient>

    <!-- Ambient Glow Filters -->
    <filter id="orangeGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="90" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="softBlur" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bgGrad)" />

  <!-- Dotted Grid Pattern -->
  <g fill="#ffffff" fill-opacity="0.015">
    <circle cx="100" cy="100" r="1.5" /><circle cx="200" cy="100" r="1.5" /><circle cx="300" cy="100" r="1.5" /><circle cx="400" cy="100" r="1.5" />
    <circle cx="100" cy="200" r="1.5" /><circle cx="200" cy="200" r="1.5" /><circle cx="300" cy="200" r="1.5" /><circle cx="400" cy="200" r="1.5" />
    <circle cx="100" cy="300" r="1.5" /><circle cx="200" cy="300" r="1.5" /><circle cx="300" cy="300" r="1.5" /><circle cx="400" cy="300" r="1.5" />
    <circle cx="100" cy="400" r="1.5" /><circle cx="200" cy="400" r="1.5" /><circle cx="300" cy="400" r="1.5" /><circle cx="400" cy="400" r="1.5" />
    <circle cx="100" cy="500" r="1.5" /><circle cx="200" cy="500" r="1.5" /><circle cx="300" cy="500" r="1.5" /><circle cx="400" cy="500" r="1.5" />
  </g>

  <!-- Ambient Orange Glows (Golden Hour Effect) -->
  <circle cx="1500" cy="300" r="400" fill="#FF8A3D" fill-opacity="0.12" filter="url(#orangeGlow)" />
  <circle cx="1200" cy="480" r="250" fill="#FFB347" fill-opacity="0.08" filter="url(#orangeGlow)" />
  <circle cx="850" cy="150" r="280" fill="#F6C667" fill-opacity="0.05" filter="url(#orangeGlow)" />

  <!-- Organic Wavy Shapes (Inspired by Artwork) -->
  <g fill="url(#warmGrad)" fill-opacity="0.08">
    <path d="M 950,640 C 1150,480 1300,580 1520,380 C 1740,180 1850,220 1920,80 L 1920,640 Z" />
    <path d="M 1150,640 C 1320,520 1450,460 1680,340 C 1850,220 1880,280 1920,160 L 1920,640 Z" fill-opacity="0.05" />
    <path d="M 800,640 C 1080,500 1200,620 1420,440 C 1600,260 1780,380 1920,290 L 1920,640 Z" fill-opacity="0.03" />
  </g>

  <!-- Neural Nodes & Connections -->
  <g stroke="#FF8A3D" stroke-opacity="0.1" stroke-width="1.5" fill="none">
    <line x1="1650" y1="180" x2="1750" y2="120" />
    <line x1="1750" y1="120" x2="1820" y2="200" />
    <line x1="1820" y1="200" x2="1720" y2="260" />
    <line x1="1720" y1="260" x2="1650" y2="180" />
    <line x1="1750" y1="120" x2="1720" y2="260" />

    <!-- Glow Nodes -->
    <circle cx="1650" cy="180" r="6" fill="#FF8A3D" fill-opacity="0.7" filter="url(#softBlur)" />
    <circle cx="1750" cy="120" r="4" fill="#FFFFFF" fill-opacity="0.8" />
    <circle cx="1820" cy="200" r="7" fill="#FFB347" fill-opacity="0.7" filter="url(#softBlur)" />
    <circle cx="1720" cy="260" r="5" fill="#F6C667" fill-opacity="0.6" />
  </g>

  <!-- Circuit Traces -->
  <path d="M 1250,220 L 1320,220 L 1370,270 L 1480,270" stroke="#FF8A3D" stroke-opacity="0.15" stroke-width="1.5" fill="none" />
  <circle cx="1250" cy="220" r="3" fill="#FF8A3D" fill-opacity="0.5" />
  <circle cx="1480" cy="270" r="3" fill="#FFB347" fill-opacity="0.5" />

  <!-- Glassmorphic Dashboard Panel -->
  <g transform="translate(1180, 150)">
    <!-- Base Card -->
    <rect width="600" height="340" rx="24" fill="url(#glassGrad)" stroke="url(#borderGrad)" stroke-width="2" />
    
    <!-- Window buttons -->
    <circle cx="35" cy="35" r="6" fill="#FF8A3D" fill-opacity="0.8" />
    <circle cx="55" cy="35" r="6" fill="#FFB347" fill-opacity="0.6" />
    <circle cx="75" cy="35" r="6" fill="#F6C667" fill-opacity="0.5" />
    <text x="300" y="40" font-size="12" font-weight="700" fill="#FF8A3D" fill-opacity="0.5" text-anchor="middle" letter-spacing="1">PRASHANT.DEV</text>
    <line x1="0" y1="65" x2="600" y2="65" stroke="#ffffff" stroke-opacity="0.05" stroke-width="1.5" />

    <!-- Panel Content -->
    <g transform="translate(40, 95)">
      <!-- Title -->
      <text x="0" y="20" font-size="13" font-weight="700" fill="#FFB347" letter-spacing="1.5">ARCHITECTURE METRICS</text>
      
      <!-- Graph mockup -->
      <path d="M 0,160 Q 60,110 120,130 T 240,80 T 360,110 T 480,50 T 520,60" fill="none" stroke="url(#warmGrad)" stroke-width="3" stroke-linecap="round" />
      <path d="M 0,160 Q 60,110 120,130 T 240,80 T 360,110 T 480,50 T 520,60 L 520,180 L 0,180 Z" fill="url(#warmGrad)" fill-opacity="0.04" />
      
      <!-- Graph Dots -->
      <circle cx="240" cy="80" r="5" fill="#FFFFFF" />
      <circle cx="480" cy="50" r="5" fill="#FF8A3D" filter="url(#softBlur)" />

      <!-- Horizontal grid lines inside graph -->
      <line x1="0" y1="90" x2="520" y2="90" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1" />
      <line x1="0" y1="140" x2="520" y2="140" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1" />

      <!-- Text Tags -->
      <rect x="0" y="195" width="90" height="24" rx="6" fill="#1A2438" stroke="#FF8A3D" stroke-opacity="0.3" stroke-width="1" />
      <text x="45" y="211" font-size="10" font-weight="700" fill="#FF8A3D" text-anchor="middle">99.9% uptime</text>

      <rect x="105" y="195" width="100" height="24" rx="6" fill="#1A2438" stroke="#FFB347" stroke-opacity="0.3" stroke-width="1" />
      <text x="155" y="211" font-size="10" font-weight="700" fill="#FFB347" text-anchor="middle">500+ mentored</text>
    </g>
  </g>

  <!-- Floating Particles -->
  <circle cx="1120" cy="460" r="5" fill="#FF8A3D" fill-opacity="0.4" filter="url(#softBlur)" />
  <circle cx="1780" cy="530" r="8" fill="#FFB347" fill-opacity="0.25" filter="url(#softBlur)" />
  <circle cx="1020" cy="220" r="4" fill="#FFFFFF" fill-opacity="0.3" />

  <!-- Left Content -->
  <g transform="translate(120, 0)">
    <!-- Greetings Badge -->
    <g transform="translate(0, 160)">
      <rect width="180" height="32" rx="16" fill="#1A2438" stroke="#FF8A3D" stroke-width="1" stroke-opacity="0.3" />
      <circle cx="20" cy="16" r="5" fill="#FF8A3D" filter="url(#softBlur)" />
      <text x="36" y="20" font-size="11" font-weight="700" fill="#FFB347" letter-spacing="1.5">HELLO WORLD</text>
    </g>

    <!-- Main Title -->
    <text x="0" y="280" font-size="80" font-weight="800" fill="url(#textGrad)" letter-spacing="-1.5">Prashant Kumar</text>
    
    <!-- Subtitle Roles -->
    <text x="0" y="360" font-size="28" font-weight="700" fill="url(#warmGrad)" letter-spacing="0.5">
      Full Stack Developer <tspan fill="#ffffff" font-weight="300">|</tspan> Corporate Trainer <tspan fill="#ffffff" font-weight="300">|</tspan> Cloud &amp; AI Enthusiast
    </text>

    <!-- Decorative Gradient Accent Line -->
    <rect x="0" y="390" width="400" height="4" rx="2" fill="url(#warmGrad)" />

    <!-- Description -->
    <text x="0" y="445" font-size="20" font-weight="500" fill="#D8DEE9" letter-spacing="0.2">
      Building scalable software <tspan fill="#FF8A3D" font-weight="700">•</tspan> Teaching technology <tspan fill="#FFB347" font-weight="700">•</tspan> Solving real-world problems
    </text>
  </g>
</svg>"""
    with open('assets/hero-banner.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_separator():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 40" width="850" height="40" fill="none">
  <defs>
    <linearGradient id="warmGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF8A3D" stop-opacity="0" />
      <stop offset="15%" stop-color="#FF8A3D" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#FFB347" stop-opacity="1" />
      <stop offset="85%" stop-color="#F6C667" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#F6C667" stop-opacity="0" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <!-- Organic waves instead of sharp lines -->
  <path d="M 50,20 Q 242.5,5 425,20 T 800,20" stroke="url(#warmGrad)" stroke-width="2.5" filter="url(#glow)" stroke-linecap="round" />
  <path d="M 50,20 Q 242.5,35 425,20 T 800,20" stroke="url(#warmGrad)" stroke-width="1.2" stroke-opacity="0.4" stroke-linecap="round" />
  
  <circle cx="425" cy="20" r="5" fill="#FFFFFF" />
  <circle cx="425" cy="20" r="9" stroke="#FF8A3D" stroke-width="1.5" />
</svg>"""
    with open('assets/separator.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_project_card(filename, title, description, features, tags):
    # Determine icon path based on title
    icon_path = ""
    icon_color = "#FF8A3D"
    if "Library" in title:
        icon_path = '<path d="M4 6H2v14c0 1.1.9 2 2 2h14v-2H4V6zm16-4H8c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-1 9H9V9h10v2zm-4 4H9v-2h6v2zm4-8H9V5h10v2z"/>'
    elif "Trust" in title:
        icon_path = '<path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2z"/>'
    elif "Compario" in title:
        icon_path = '<path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"/>'
        icon_color = "#FFB347"
    elif "XHAudio" in title:
        icon_path = '<path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>'
        icon_color = "#F6C667"
    else:  # IoT
        icon_path = '<path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>'
        icon_color = "#FF8A3D"

    # Build tag SVG pills
    tag_html = ""
    x_offset = 0
    colors = ["#FF8A3D", "#FFB347", "#F6C667", "#E5E7EB"]
    bg_colors = ["#2A1B15", "#2A2115", "#2A2515", "#212936"]
    border_colors = ["#FF8A3D", "#FFB347", "#F6C667", "#475569"]
    
    for idx, tag in enumerate(tags[:4]):
        w = len(tag) * 7 + 22
        tag_html += f"""
    <!-- Tag: {tag} -->
    <rect x="{x_offset}" y="0" width="{w}" height="24" rx="8" fill="{bg_colors[idx]}" stroke="{border_colors[idx]}" stroke-opacity="0.3" stroke-width="1" />
    <text x="{x_offset + w/2}" y="15" font-size="10" font-weight="700" fill="{colors[idx]}" text-anchor="middle">{tag}</text>"""
        x_offset += w + 8

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" width="400" height="220" style="background:#0E1525; font-family:'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A2438" />
      <stop offset="100%" stop-color="#0E1525" />
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF8A3D" stop-opacity="0.4"/>
      <stop offset="50%" stop-color="#FFB347" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#F6C667" stop-opacity="0.2"/>
    </linearGradient>
    <filter id="blurGlow">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="398" height="218" rx="24" fill="url(#cardGrad)" stroke="url(#borderGrad)" stroke-width="1.5" />

  <!-- Subtle glow in top right -->
  <circle cx="360" cy="40" r="25" fill="{icon_color}" fill-opacity="0.06" filter="url(#blurGlow)" />

  <!-- Project Icon -->
  <g transform="translate(24, 24)" fill="{icon_color}">
    {icon_path}
  </g>

  <!-- Status / Link indicator -->
  <g transform="translate(348, 24)">
    <!-- Rounded status pill -->
    <rect x="-80" y="0" width="85" height="20" rx="10" fill="#111827" stroke="#FF8A3D" stroke-opacity="0.2" />
    <circle cx="-70" cy="10" r="3.5" fill="{icon_color}" />
    <text x="-60" y="13" font-size="9" font-weight="700" fill="#D8DEE9">SHOWCASE</text>
  </g>

  <!-- Title -->
  <text x="24" y="80" font-size="18" font-weight="700" fill="#FFFFFF">{title}</text>

  <!-- Description -->
  <text x="24" y="105" font-size="12" font-weight="400" fill="#D8DEE9" width="352">
    <tspan x="24" dy="0">{description[0]}</tspan>
    <tspan x="24" dy="16">{description[1]}</tspan>
  </text>

  <!-- Features list -->
  <text x="24" y="146" font-size="10" font-weight="700" fill="#FFB347" letter-spacing="0.5">{features.upper()}</text>

  <!-- Tech pills -->
  <g transform="translate(24, 166)">
    {tag_html}
  </g>
</svg>"""
    
    with open(f'assets/{filename}', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_section_header(filename, title):
    # Choose icon based on title
    icon_path = ""
    if "ABOUT" in title:
        icon_path = '<circle cx="30" cy="30" r="12" stroke="#FF8A3D" stroke-width="2.5" fill="none"/><circle cx="30" cy="30" r="4" fill="#FFB347"/>'
    elif "FOCUS" in title:
        icon_path = '<rect x="18" y="18" width="24" height="24" rx="6" stroke="#FF8A3D" stroke-width="2.5" fill="none"/><circle cx="30" cy="30" r="3" fill="#FFB347"/>'
    elif "TECH" in title:
        icon_path = '<path d="M22,18 L38,18 L30,38 Z" stroke="#FF8A3D" stroke-width="2.5" fill="none" stroke-linejoin="round"/>'
    elif "PROJECTS" in title:
        icon_path = '<rect x="18" y="18" width="24" height="24" rx="4" fill="none" stroke="#FF8A3D" stroke-width="2.5"/><path d="M18,26 L42,26" stroke="#FF8A3D" stroke-width="1.5"/>'
    elif "RESEARCH" in title:
        icon_path = '<path d="M30,18 L38,26 L30,34 L22,26 Z" stroke="#FF8A3D" stroke-width="2.5" fill="none"/><line x1="30" y1="22" x2="30" y2="30" stroke="#FFB347" stroke-width="2"/>'
    elif "CREDENTIALS" in title or "CERTIFICATIONS" in title:
        icon_path = '<polygon points="30,16 34,24 42,26 36,32 38,40 30,36 22,40 24,32 18,26 26,24" stroke="#FF8A3D" stroke-width="2.5" stroke-linejoin="round" fill="none"/>'
    elif "STATS" in title or "METRICS" in title:
        icon_path = '<path d="M20,40 L20,30 M30,40 L30,22 M40,40 L40,18" stroke="#FF8A3D" stroke-width="2.5" stroke-linecap="round"/><circle cx="30" cy="30" r="1" fill="none"/>'
    elif "GOALS" in title:
        icon_path = '<circle cx="30" cy="30" r="12" stroke="#FF8A3D" stroke-width="2.5" fill="none"/><circle cx="30" cy="30" r="6" stroke="#FFB347" stroke-width="1.5" fill="none"/>'
    else:  # CONNECT
        icon_path = '<path d="M18,20 H42 V40 H18 Z M18,20 L30,32 L42,20" stroke="#FF8A3D" stroke-width="2.5" fill="none" stroke-linejoin="round"/>'

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 60" width="850" height="60" fill="none">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF8A3D" />
      <stop offset="50%" stop-color="#FFB347" />
      <stop offset="100%" stop-color="#F6C667" />
    </linearGradient>
    <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF8A3D" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#FF8A3D" stop-opacity="0.0" />
    </linearGradient>
  </defs>

  <!-- Header Icon -->
  <g>
    {icon_path}
  </g>

  <!-- Title Text -->
  <text x="56" y="38" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800" fill="url(#headerGrad)" letter-spacing="2">{title.upper()}</text>

  <!-- Accent dotted line -->
  <line x1="300" y1="32" x2="820" y2="32" stroke="url(#lineGrad)" stroke-width="1.5" stroke-dasharray="6,4" />
</svg>"""
    
    with open(f'assets/{filename}', 'w', encoding='utf-8') as f:
        f.write(svg)

# Main Executable Flow
if __name__ == '__main__':
    os.makedirs('assets', exist_ok=True)
    
    create_hero_banner()
    create_separator()
    
    # 5 Project Cards
    create_project_card(
        'project-lms.svg', 
        'Library Management System',
        ['Enterprise system managing catalogs, digital checkouts,', 'subscriptions, and secure Razorpay payment gateways.'],
        'admin dashboard • subscriptions • payments',
        ['React', 'Laravel', 'MySQL', 'Razorpay']
    )
    create_project_card(
        'project-hariom.svg', 
        'Hariom Trust Platform',
        ['Temple booking and donation system designed to', 'streamline visitor check-ins and secure transactions.'],
        'donation management • temple booking • responsive',
        ['React', 'PHP', 'MySQL', 'Bootstrap']
    )
    create_project_card(
        'project-compario.svg', 
        'Compario Ecommerce',
        ['Modern product listings interface showcasing dynamic', 'filtering options and fluid custom layout animations.'],
        'ecommerce frontend • responsive • animations',
        ['React', 'Tailwind', 'CSS3', 'Animations']
    )
    create_project_card(
        'project-xhaudio.svg', 
        'XHAudio Player',
        ['Lightweight desktop/mobile web music player featuring', 'rich visualizations, playlist controls, and modern UX.'],
        'audio visualizer • playlists • modern ui',
        ['JavaScript', 'Tailwind', 'HTML5', 'Web Audio']
    )
    create_project_card(
        'project-iot.svg', 
        'IoT Healthcare System',
        ['IEEE publication outlining a secure microservices', 'architecture for real-time remote telemetry streaming.'],
        'ieee research • microservices • cloud iot',
        ['Python', 'Java', 'AWS Cloud', 'Docker']
    )
    
    # 9 Headers
    create_section_header('header-about.svg', 'about me')
    create_section_header('header-focus.svg', 'current focus')
    create_section_header('header-tech.svg', 'technical ecosystem')
    create_section_header('header-projects.svg', 'featured projects')
    create_section_header('header-research.svg', 'research publication')
    create_section_header('header-certifications.svg', 'professional credentials')
    create_section_header('header-stats.svg', 'metrics &amp; analytics')
    create_section_header('header-goals.svg', 'current goals')
    create_section_header('header-connect.svg', 'connect &amp; collaborate')
    
    print("Successfully generated all portfolio SVGs!")
