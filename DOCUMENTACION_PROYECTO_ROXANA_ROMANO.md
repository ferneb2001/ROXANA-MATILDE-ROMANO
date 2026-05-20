# 📚 DOCUMENTACIÓN COMPLETA - SITIO WEB ROXANA ROMANO
## PROYECTO ARTÍSTICO DIGITAL - FERNANDO ADRIAN NEBRO

---

## 🎯 RESUMEN EJECUTIVO

**Sitio Web:** Catálogo artístico digital de Roxana Matilde Romano
**Tecnología:** HTML5, CSS3, JavaScript vanilla, GitHub Pages
**Diseño:** Responsive, navegación por scroll/táctil, trilingüe (ES/EN/PT)
**Estado:** Completamente funcional y optimizado para todos los dispositivos

---

## 📁 ESTRUCTURA DE CARPETAS Y ARCHIVOS

```
C:\ROXANA MATILDE ROMANO\
├── index.html                    # Archivo principal del sitio web
├── maximas.md                   # Máximas y metodologías de desarrollo
├── DOCUMENTACION_PROYECTO_ROXANA_ROMANO.md # Este documento
├── 
├── CATALOGO/                    # Carpeta con obras de arte
│   ├── Michael - óleo sobre tela - 82 cm x 79 cm - año 2016.jpg
│   ├── [115+ obras organizadas cronológicamente]
│   └── (Formato: Título - técnica - dimensiones - año.jpg)
│
├── CERTIFICADOS/                # Carpeta con certificados
│   ├── DIPLOMATURA EN ARTETERAPIA PROFESIONAL.jpg (PRIORITARIO)
│   ├── Primer premio Rostros Universales.jpg (PRIORITARIO)  
│   └── [9 certificados adicionales]
│
├── BACKUPS/                     # Copias de seguridad automáticas
│   ├── backup_index_20250903_163121.html
│   ├── backup_index_redesign_obras_20250903_172447.html
│   ├── backup_index_boton_mini_20250903_183456.html
│   └── [15+ backups con timestamps]
│
└── backup html/                 # Backup adicional
    └── index.html
```

---

## 🏗️ ARQUITECTURA DEL SITIO WEB

### **ESTRUCTURA DE 8 PÁGINAS:**

1. **Página 1 - Datos Personales** 
   - Foto de perfil, nombre, contacto
   - Enlaces sociales (Instagram, Email)

2. **Página 2 - Declaración de Artista**
   - Fondo blanco, texto justificado
   - Filosofía y enfoque artístico

3. **Página 3 - Biografía**
   - Fondo blanco, texto justificado  
   - Historia personal y trayectoria

4. **Página 4 - Índice**
   - Botones de navegación directa
   - Acceso rápido a secciones principales

5. **Página 5 - Obras** 
   - **REDISEÑADA:** Fondo neutro #f8f9fa
   - Grid responsive con obras cronológicas
   - Lightbox con detalles y contacto

6. **Página 6 - Certificados**
   - Fondo negro elegante
   - Certificados prioritarios primero
   - Lightbox para vista ampliada

7. **Página 7 - Arte en Crudo**
   - **TRILINGÜE:** Español, Inglés, Portugués
   - Botones WhatsApp y Google Maps
   - Invitación turística a Atelier

8. **Página 8 - Clases**
   - Información de talleres y cursos

---

## 🎨 ESQUEMA DE COLORES Y DISEÑO

### **PALETA CROMÁTICA:**
- **Fondo neutro obras:** #f8f9fa (gris muy claro)
- **Texto principal:** #2c2c2c (gris oscuro)
- **Acentos cálidos:** #8b7355 (gris cálido para iconos)
- **Hover elegante:** #a08660 (gris cálido claro)
- **Páginas especiales:** Fondos degradados por página

### **TIPOGRAFÍA:**
- **Fuente:** System fonts (Arial, sans-serif)
- **Jerarquías:** h1 (2.5em), h2 (2em), texto (base)
- **Line-height:** 1.7 para óptima legibilidad

### **ELEMENTOS VISUALES:**
- **Sombras suaves:** `0 2px 8px rgba(0,0,0,0.1)`
- **Transiciones:** 0.3s ease para interacciones
- **Border-radius:** 15px para tarjetas, 12px para botones

---

## 🔧 FUNCIONALIDADES TÉCNICAS

### **NAVEGACIÓN:**
- **Scroll horizontal:** Mouse wheel, trackpad
- **Táctil:** Swipe en dispositivos móviles
- **Teclado:** Flechas izquierda/derecha
- **Indicador:** "X / 8" páginas

### **SISTEMA DE OBRAS:**
```javascript
const catalogWorks = [
    {
        path: "CATALOGO/obra.jpg",
        title: "Título",
        technique: "óleo sobre tela",
        dimensions: "82 cm x 79 cm", 
        year: "2016",
        collection: "Colección privada"
    }
];
```

### **LIGHTBOX:**
- Vista ampliada de obras/certificados
- Botón WhatsApp ultra-compacto
- Información detallada
- Navegación por teclado (ESC para cerrar)

### **RESPONSIVE DESIGN:**
```css
@media (max-width: 768px) {
    .page { padding: 15px 15px 40px 15px; }
    .page2, .page3 { padding: 15px 15px 60px 15px; }
}
```

---

## 📋 PROCEDIMIENTOS Y FLUJOS DE TRABAJO

### **1. AGREGAR NUEVA OBRA:**

**Paso 1:** Subir imagen a carpeta `CATALOGO/`
**Formato:** `Título - técnica - dimensiones - año XXXX.jpg`

**Paso 2:** Editar `index.html`, buscar array `catalogWorks`
**Ubicación:** Insertar cronológicamente (más reciente primero)

```javascript
{
    path: "CATALOGO/nueva-obra.jpg",
    type: "image", 
    title: "Título Obra",
    technique: "óleo sobre tela",
    dimensions: "XX cm x XX cm",
    year: "XXXX",
    collection: ""
}
```

**Paso 3:** Aplicar protocolo de subida GitHub

### **2. AGREGAR CERTIFICADO:**

**Paso 1:** Subir a `CERTIFICADOS/`
**Paso 2:** Agregar a array `certificateData`
**Ubicación:** Primeras posiciones para certificados importantes

### **3. PROTOCOLO DE SUBIDA GITHUB:**

```bash
git add .
git commit -m "Descripción específica de cambios realizados"
git push origin main
```
**Tiempo de despliegue:** 2-3 minutos
**URL del sitio:** https://ferneb2001.github.io/ROXANA-MATILDE-ROMANO/

### **4. BACKUP AUTOMÁTICO:**
- Siempre crear backup antes de cambios
- Formato: `backup_index_descripcion_YYYYMMDD_HHMMSS.html`
- Conservar para posibles rollbacks

---

## 🌐 SEO — OPTIMIZACIÓN PARA BUSCADORES (Mayo 2026)

### **QUÉ SE AGREGÓ:**
El sitio no tenía metadata visible para Google ni para redes sociales. Se agregaron 5 capas de mejoras en el `<head>` del `index.html`.

### **1. Meta tags primarios**
- `description`: Texto que Google muestra debajo del título en los resultados
- `keywords`: 13 palabras clave en español (artista visual, Mendoza, óleo, etc.)
- `author`: Roxana Matilde Romano
- `robots`: index, follow (permite indexación completa)
- `canonical`: URL oficial del sitio

### **2. Open Graph (Facebook, WhatsApp, LinkedIn)**
Cuando alguien comparte el link, aparece una tarjeta con foto, título y descripción.

### **3. Twitter Card**
Lo mismo para Twitter/X.

### **4. Schema.org VisualArtist**
Datos estructurados que le dicen a Google exactamente que es una artista visual: nombre, dirección, teléfono, premios, redes sociales.

### **CAMBIO DE TÍTULO:**
- "Artista Plástica" → **"Artista Visual"** en toda la web y en todo el SEO (6 lugares)

### **CONFIGURACIÓN TÉCNICA:**
- Git Credential Manager configurado para que los pushes funcionen sin pedir contraseña cada vez
- URL del repositorio actualizada a: `https://github.com/ferneb2001/ROXANA-MATILDE-ROMANO.git`

### **COMPLETADO Mayo 2026:**
- ✅ Imagen de preview: `CATALOGO/Sin título - óleo sobre tela - 170 cm x 100 cm - año 2023.jpg`
- ✅ og:image:width 1200 / og:image:height 706 agregados
- ✅ "Artista plástica" → "Artista Visual" en og:description y twitter:description

---

## 🤖 AGENTE IA — CHATBOT GEMINI (Mayo 2026)

### **ARQUITECTURA:**
El chatbot usa **Cloudflare Workers como proxy** para proteger la API key.

```
Visitante → index.html → Cloudflare Worker → Gemini API
```

La API key NUNCA está en el código HTML — está guardada como secreto en Cloudflare.

### **CLOUDFLARE WORKER:**
- **Nombre:** roxana-gemini-proxy
- **URL:** https://roxana-gemini-proxy.ferneb2001.workers.dev
- **Panel:** dash.cloudflare.com → Workers & Pages → roxana-gemini-proxy
- **Variable secreta:** `GEMINI_API_KEY` (guardada en Ajustes → Variables y secretos)
- **Modelo:** gemini-2.5-flash
- **CORS permitido:** https://ferneb2001.github.io

### **POR QUÉ CLOUDFLARE Y NO API KEY DIRECTA:**
GitHub escanea automáticamente todos los repositorios públicos y reporta las API keys a Google, que las bloquea. Con el proxy de Cloudflare la key nunca aparece en el código.

### **PROYECTO GEMINI:**
- **Nombre:** ROXANA ROMANO ARTISTA VISUAL
- **Panel:** aistudio.google.com → Claves de API
- **Si la key falla:** crear nueva en aistudio.google.com y actualizarla en Cloudflare (Ajustes → Variables y secretos) — NO en el HTML

### **CHATBOT EN EL SITIO:**
- Botón flotante color #8b7355, esquina inferior derecha
- Conoce obras, series, técnicas, premios, clases, Atelier, contacto
- Responde en español, inglés o portugués
- Deriva precios y disponibilidad al WhatsApp: +5492615988180

---

## 🌍 POSICIONAMIENTO WEB (Mayo 2026)

### **GOOGLE BUSINESS PROFILE:**
- **Estado:** Activo y verificado
- **Nombre:** Roxana Matilde Romano — Artista Visual
- **Dirección:** Manuel A. Sáez 2101, Las Heras, Mendoza
- **Categoría:** Galería de arte / Academia de arte
- **Fotos:** Subidas (Atelier, obras, Roxana pintando)
- **WhatsApp chat:** https://wa.me/5492615988180
- **Panel:** business.google.com (cuenta de Roxana)

### **GOOGLE SEARCH CONSOLE:**
- **Estado:** Verificado e indexación solicitada
- **Método de verificación:** Etiqueta HTML en index.html
- **Meta tag:** `<meta name="google-site-verification" content="iOwEnc2F5fDV1Att-XWbp8MwDOb-OIi9UcqdO1Ov_co">`
- **Panel:** search.google.com/search-console (cuenta de Roxana)
- **Sitio en Google:** Aparece como primer resultado al buscar "Roxana Matilde Romano Artista Visual"

### **INSTAGRAM:**
- Link del sitio agregado en la bio del perfil

---

## 🔍 OPTIMIZACIONES APLICADAS

### **UX/UI MEJORAS:**
1. ✅ **Botones navegación eliminados** - Interfaz limpia
2. ✅ **Obras con fondo neutro** - Arte como protagonista
3. ✅ **Botones ultra-compactos** - Móviles optimizados
4. ✅ **Colores coordinados** - Gris cálido elegante
5. ✅ **Texto trilingüe** - Mercado turístico internacional

### **RESPONSIVE OPTIMIZADO:**
- **Desktop:** Grid 3-4 columnas, hover elegante
- **Tablet:** Grid 2-3 columnas, botones medianos  
- **Mobile:** Grid 1-2 columnas, botones mini

### **PERFORMANCE:**
- **Imágenes lazy loading** con fallback
- **CSS optimizado** sin frameworks pesados
- **JavaScript vanilla** para máxima velocidad

---

## 🔗 ENLACES Y CONTACTOS

### **SITIO WEB LIVE:**
https://ferneb2001.github.io/ROXANA-MATILDE-ROMANO/

### **REPOSITORIO GITHUB:**
https://github.com/ferneb2001/ROXANA-MATILDE-ROMANO

### **CONTACTOS INTEGRADOS:**
- **WhatsApp:** +5492615988180
- **Dirección Atelier:** Manuel A. Sáez 2101, Las Heras, Mendoza
- **Instagram:** @roxana.matilde.romano
- **Email:** roxanamatilderomano@gmail.com

---

## 🚨 PUNTOS CRÍTICOS PARA RECORDAR

### **NUNCA ELIMINAR:**
- ❌ Arrays `catalogWorks` y `certificateData`
- ❌ Función `goToPage()` y navegación
- ❌ CSS responsive media queries
- ❌ Estructura de 8 páginas establecida

### **SIEMPRE HACER:**
- ✅ Backup antes de cualquier cambio
- ✅ Verificar funcionalidad en móvil/desktop
- ✅ Conservar orden cronológico en obras
- ✅ Mantener formato trilingüe página 7

### **PROTOCOLO DE EMERGENCIA:**
Si algo sale mal, usar backup más reciente:
```bash
cp backup_index_[fecha_mas_reciente].html index.html
git add index.html
git commit -m "Rollback a versión estable"
git push origin main
```

---

## 📈 MÉTRICAS Y LOGROS

### **ESTADÍSTICAS TÉCNICAS:**
- **115+ obras catalogadas** cronológicamente
- **11 certificados** organizados por importancia
- **3 idiomas** (ES/EN/PT) en Arte en Crudo
- **15+ backups** de seguridad creados
- **8 commits exitosos** durante optimización

### **MEJORAS UX CONSEGUIDAS:**
- **50% reducción** tamaño botones WhatsApp
- **Navegación 100% táctil** sin botones molestos
- **Fondo neutro** que realza las obras de arte
- **Coordinación cromática** perfecta
- **Responsive optimizado** para todos los dispositivos

---

## 🎯 FUTURAS EXPANSIONES

### **FUNCIONALIDADES POTENCIALES:**
1. **Sistema de filtrado** por año/técnica/colección
2. **Galería de proceso creativo** por obra
3. **Blog de artista** integrado
4. **Tienda online** para obras disponibles
5. **Sistema de reservas** para visitas al Atelier

### **MANTENIMIENTO SUGERIDO:**
- **Mensual:** Agregar nuevas obras creadas
- **Semestral:** Actualizar certificados/logros
- **Anual:** Revisar diseño y tendencias UX

---

*📚 Documentación creada por Fernando Adrian Nebro aplicando máximas de verificación integral y conservación de funcionalidad. Última actualización: Mayo 2026.*

*🎨 "El arte cobra vida cuando se comparte con alma y corazón" - Roxana Romano*