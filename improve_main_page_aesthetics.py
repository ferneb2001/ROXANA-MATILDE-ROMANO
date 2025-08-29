import re

def improve_main_page_aesthetics():
    print("MEJORANDO ESTÉTICA DE LA PÁGINA PRINCIPAL")
    print("=" * 50)
    
    # Leer archivo base que funciona
    with open("roxana_navegacion_arreglada.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # 1. MEJORAR CSS GENERAL DE LA PÁGINA 1
    nuevo_css_pagina1 = """
        /* Página 1 específica */
        .page1 {
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40px 20px;
        }
        
        .page1 .content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            max-width: 500px;
            width: 100%;
        }
        
        .profile-photo {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            object-fit: cover;
            object-position: center center;
            border: 5px solid rgba(255,255,255,0.8);
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            margin-bottom: 25px;
            transition: transform 0.3s ease;
        }
        
        .profile-photo:hover {
            transform: scale(1.05);
        }
        
        .page1 h1 {
            font-size: 2.2em;
            font-weight: bold;
            margin-bottom: 8px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            letter-spacing: 1px;
        }
        
        .page1 .subtitle {
            font-size: 1.3em;
            opacity: 0.9;
            margin-bottom: 35px;
            font-style: italic;
            font-weight: 300;
        }
        
        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 12px;
            width: 100%;
            max-width: 420px;
        }
        
        .contact-item {
            background: rgba(255,255,255,0.15);
            padding: 14px 20px;
            border-radius: 30px;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.3);
            backdrop-filter: blur(10px);
            font-size: 15px;
            font-weight: 500;
        }
        
        .contact-item:hover {
            background: rgba(255,255,255,0.25);
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            border-color: rgba(255,255,255,0.5);
        }
        
        .contact-item a {
            color: inherit;
            text-decoration: none;
            display: block;
            width: 100%;
        }
        
        /* Responsive para página 1 */
        @media (max-width: 768px) {
            .page1 {
                padding: 30px 15px;
            }
            
            .profile-photo {
                width: 180px;
                height: 180px;
            }
            
            .page1 h1 {
                font-size: 1.8em;
            }
            
            .page1 .subtitle {
                font-size: 1.1em;
            }
            
            .contact-info {
                max-width: 350px;
            }
        }
        
        @media (max-width: 480px) {
            .profile-photo {
                width: 160px;
                height: 160px;
            }
            
            .page1 h1 {
                font-size: 1.6em;
            }
        }"""
    
    # Insertar el nuevo CSS antes del cierre de </style>
    contenido = contenido.replace('</style>', nuevo_css_pagina1 + '\n    </style>')
    
    # 2. MEJORAR LA ESTRUCTURA HTML DE LA PÁGINA 1
    nueva_estructura_pagina1 = '''        <!-- Página 1: Datos Personales -->
        <div class="page page1">
            <div class="content">
                <img src="FOTO RO.jpg" alt="Roxana Matilde Romano" class="profile-photo">
                <h1>ROXANA MATILDE ROMANO</h1>
                <p class="subtitle">Artista Visual</p>
                
                <div class="contact-info">
                    <div class="contact-item">
                        <a href="https://wa.me/5492615988180">💬 +54 9 261-5988180</a>
                    </div>
                    <div class="contact-item">
                        <a href="mailto:roxanamatilderomano@gmail.com">✉️ roxanamatilderomano@gmail.com</a>
                    </div>
                    <div class="contact-item">
                        📍 Manuel A. Sáez 2101 - Las Heras - Mendoza
                    </div>
                    <div class="contact-item">
                        <a href="https://youtube.com/@roxanamatilderomano" target="_blank">📺 @roxanamatilderomano</a>
                    </div>
                    <div class="contact-item">
                        <a href="https://instagram.com/roxanamatilderomano2017" target="_blank">📷 @roxanamatilderomano2017</a>
                    </div>
                </div>
            </div>
        </div>'''
    
    # Reemplazar solo la página 1
    patron_pagina1 = r'(\s*<!-- Página 1: Datos Personales -->.*?</div>\s*</div>)'
    contenido = re.sub(patron_pagina1, nueva_estructura_pagina1, contenido, flags=re.DOTALL)
    
    # 3. MEJORAR EL GRADIENTE DE FONDO DE LA PÁGINA 1
    contenido = contenido.replace(
        '.page1 { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); }',
        '.page1 { background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #2c3e50 100%); }'
    )
    
    # 4. ELIMINAR CSS CONFLICTIVO VIEJO
    # Eliminar definiciones duplicadas que puedan causar problemas
    contenido = re.sub(r'\.profile-photo \{[^}]*\}(?=.*\.profile-photo)', '', contenido, flags=re.DOTALL)
    contenido = re.sub(r'\.contact-info \{[^}]*\}(?=.*\.contact-info)', '', contenido, flags=re.DOTALL)
    contenido = re.sub(r'\.contact-item \{[^}]*\}(?=.*\.contact-item)', '', contenido, flags=re.DOTALL)
    
    # Guardar archivo mejorado
    with open("roxana_estetica_mejorada.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Foto más grande (220px) con hover effect")
    print("✓ Mejor centrado y espaciado vertical")
    print("✓ Typography mejorada (letra más elegante)")
    print("✓ Contact items con backdrop-filter blur")
    print("✓ Hover effects suaves con transform y sombras")
    print("✓ Gradiente de fondo mejorado")
    print("✓ Responsive design optimizado")
    print("✓ Estructura HTML simplificada")
    print("\nArchivo: roxana_estetica_mejorada.html")
    print("\nMejoras estéticas:")
    print("- Foto más prominente con borde elegante")
    print("- Mejor jerarquía visual")
    print("- Efectos hover profesionales")
    print("- Spacing consistente y balanceado")
    print("- Typography más sofisticada")

if __name__ == "__main__":
    improve_main_page_aesthetics()