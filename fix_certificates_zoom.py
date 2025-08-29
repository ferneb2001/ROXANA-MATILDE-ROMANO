import re

def fix_certificates_zoom():
    print("CORRIGIENDO ZOOM EN CERTIFICADOS")
    print("=" * 40)
    
    # Leer archivo actual
    with open("roxana_final_corregida.html", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Verificar si existe la función openLightbox
    if 'function openLightbox' not in contenido:
        print("Agregando funciones de lightbox completas...")
        
        lightbox_html = '''
        <!-- Lightbox -->
        <div id="lightbox" class="lightbox" onclick="closeLightbox()" style="display: none;">
            <div class="lightbox-content" onclick="event.stopPropagation()">
                <span class="close" onclick="closeLightbox()">&times;</span>
                <img id="lightboxImg" class="lightbox-img" src="" alt="">
                <div id="lightboxInfo" class="lightbox-info"></div>
            </div>
        </div>'''
        
        # Agregar HTML del lightbox antes del cierre de body
        contenido = contenido.replace('</body>', lightbox_html + '\n    </body>')
        
        # Agregar CSS del lightbox
        lightbox_css = '''
        .lightbox {
            display: none;
            position: fixed;
            z-index: 9999;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.9);
            justify-content: center;
            align-items: center;
        }
        
        .lightbox-content {
            position: relative;
            max-width: 90%;
            max-height: 90%;
            text-align: center;
        }
        
        .lightbox-img {
            max-width: 100%;
            max-height: 80vh;
            object-fit: contain;
        }
        
        .lightbox-info {
            color: white;
            padding: 15px;
            text-align: center;
        }
        
        .close {
            position: absolute;
            top: -40px;
            right: 0;
            color: white;
            font-size: 35px;
            font-weight: bold;
            cursor: pointer;
        }
        
        .close:hover {
            opacity: 0.7;
        }'''
        
        # Insertar CSS antes del cierre de style
        contenido = contenido.replace('</style>', lightbox_css + '\n    </style>')
    
    # Corregir función de certificados para incluir onclick
    patron_cert = r'(function loadCertificados\(\) \{.*?)(\}\s*\})'
    
    nueva_funcion_cert = '''function loadCertificados() {
            const container = document.getElementById('certificadosContainer');
            if (!container || !certificateData || !Array.isArray(certificateData)) return;
            
            container.innerHTML = '';
            
            certificateData.forEach((cert, index) => {
                const div = document.createElement('div');
                div.className = 'obra-item';
                
                const certName = cert.split('/').pop().split('.')[0];
                
                div.innerHTML = `
                    <img src="${cert}" alt="Certificado ${index + 1}" class="obra-img"
                         style="cursor: pointer;"
                         onclick="openLightbox('${cert}', 'Certificado ${index + 1}', '${certName}')"
                         onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPkNlcnRpZmljYWRvPC90ZXh0Pjwvc3ZnPg=='>
                    <div class="obra-title">Certificado ${index + 1}</div>
                    <div class="obra-details">${certName}</div>
                `;
                container.appendChild(div);
            });
        }'''
    
    contenido = re.sub(patron_cert, nueva_funcion_cert + '\n        }', contenido, flags=re.DOTALL)
    
    # Asegurar que las funciones de lightbox estén presentes
    if 'function openLightbox' not in contenido:
        lightbox_functions = '''
        // Funciones de lightbox
        function openLightbox(imgSrc, title, details) {
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxInfo = document.getElementById('lightboxInfo');
            
            if (lightbox && lightboxImg && lightboxInfo) {
                lightboxImg.src = imgSrc;
                lightboxInfo.innerHTML = `<h3>${title}</h3><p>${details}</p>`;
                lightbox.style.display = 'flex';
            }
        }
        
        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            if (lightbox) {
                lightbox.style.display = 'none';
            }
        }'''
        
        # Insertar antes del cierre del script
        contenido = contenido.replace('</script>', lightbox_functions + '\n    </script>')
    
    # Guardar archivo corregido
    with open("roxana_certificados_zoom.html", "w", encoding="utf-8") as f:
        f.write(contenido)
    
    print("✓ Lightbox HTML agregado")
    print("✓ CSS de lightbox agregado") 
    print("✓ Función loadCertificados corregida")
    print("✓ Funciones JavaScript de lightbox agregadas")
    print("\nArchivo: roxana_certificados_zoom.html")
    print("\nPrueba:")
    print("1. Abre roxana_certificados_zoom.html")
    print("2. Ve a página 4 (Certificados)")
    print("3. Haz click en cualquier certificado")

if __name__ == "__main__":
    fix_certificates_zoom()