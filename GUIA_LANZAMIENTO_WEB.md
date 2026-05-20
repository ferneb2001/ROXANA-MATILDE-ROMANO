# GUÍA DE LANZAMIENTO WEB
## Proceso completo para posicionar un sitio web — Fernando Adrian Nebro

---

## REQUISITOS PREVIOS

Antes de arrancar necesitás tener:
- [ ] Sitio web publicado y funcionando
- [ ] URL del sitio
- [ ] Cuenta de Google del titular
- [ ] Número de WhatsApp de contacto
- [ ] Dirección física (si tiene local/atelier/oficina)
- [ ] Fotos: del lugar, de la persona, del trabajo/productos
- [ ] API key de Gemini (gratuita en aistudio.google.com)

---

## PASO 1 — SEO BÁSICO EN EL HTML

En el `<head>` del `index.html` agregar:

### Meta tags primarios
```html
<meta name="description" content="[Descripción del sitio, 150-160 caracteres]">
<meta name="keywords" content="[palabra1, palabra2, palabra3, ...]">
<meta name="author" content="[Nombre del titular]">
<meta name="robots" content="index, follow">
<link rel="canonical" href="[URL del sitio]">
```

### Open Graph (preview en WhatsApp, Facebook, LinkedIn)
```html
<meta property="og:type" content="profile">
<meta property="og:title" content="[Nombre — Profesión | Ciudad]">
<meta property="og:description" content="[Descripción breve]">
<meta property="og:url" content="[URL del sitio]">
<meta property="og:image" content="[URL imagen horizontal 1200x630px]">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_AR">
```

### Twitter Card
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Nombre — Profesión]">
<meta name="twitter:description" content="[Descripción breve]">
<meta name="twitter:image" content="[URL misma imagen horizontal]">
```

### Imagen para preview en redes
- Debe ser **horizontal**, mínimo 1.5:1 (ideal 1.9:1 = 1200x630px)
- Elegir la foto/obra más impactante
- La URL debe apuntar a la imagen dentro del repositorio

---

## PASO 2 — AGENTE IA CON GEMINI

### ⚠️ IMPORTANTE: NO poner la API key directo en el HTML
Si el repositorio es público (GitHub Pages, Netlify), GitHub escanea el código y reporta la key a Google, que la bloquea automáticamente. La solución es usar **Cloudflare Workers como proxy**.

---

### 2a. Crear el proxy en Cloudflare Workers (OBLIGATORIO para repos públicos)

**Cloudflare Workers es gratuito** (100.000 requests/día).

**Pasos:**
1. Crear cuenta en **cloudflare.com**
2. Ir a **Workers & Pages** → **Crear aplicación** → **¡Comienza con Hola Mundo!**
3. Nombrar el worker: `[proyecto]-gemini-proxy`
4. Hacer clic en **Deploy**
5. Ir a **Editar código**, seleccionar todo (Ctrl+A) y reemplazar con:

```javascript
export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': 'https://TU-DOMINIO.com',
          'Access-Control-Allow-Methods': 'POST',
          'Access-Control-Allow-Headers': 'Content-Type',
        }
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    const body = await request.json();

    const response = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${env.GEMINI_API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      }
    );

    const data = await response.json();

    return new Response(JSON.stringify(data), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://TU-DOMINIO.com',
      }
    });
  }
};
```

6. Reemplazar `https://TU-DOMINIO.com` con el dominio real del sitio (en los 2 lugares)
7. Hacer clic en **Desplegar**
8. Volver al panel del worker → **Ajustes** → **Variables y secretos** → **+ Agregar**
   - Tipo: **Secreto**
   - Nombre: `GEMINI_API_KEY`
   - Valor: pegar la API key de Gemini (sin pasarla por ningún chat)
9. Hacer clic en **Desplegar**

**URL del worker resultante:** `https://[nombre-worker].[usuario].workers.dev`

---

### 2b. Obtener API key de Gemini
1. Ir a **aistudio.google.com**
2. Iniciar sesión con cuenta Google
3. **Get API key** → **Create API key** → elegir proyecto
4. Pegar la key directamente en Cloudflare (paso 8 arriba) — nunca en el chat ni en el código

---

### 2c. Agregar el chatbot al HTML
En el `index.html`, insertar antes de `</body>`:

```javascript
const GEMINI_URL = 'https://[nombre-worker].[usuario].workers.dev';
```

**El chatbot NO lleva API key en el HTML** — solo la URL del Worker.

**Personalizar el SYSTEM_PROMPT con:**
- Nombre y profesión del titular
- Servicios que ofrece
- Precios (o indicar que se deriva al contacto)
- Dirección
- Contacto (WhatsApp, email, redes)
- Idiomas que habla

**El chatbot incluye:**
- Botón flotante esquina inferior derecha
- Ventana de chat con historial de conversación
- Saludo automático al abrir
- Manejo de errores con fallback al WhatsApp
- Responsive para móviles

**Colores a adaptar según el sitio:**
- Color principal del botón: cambiar `#8b7355` por el color del sitio
- Color de mensajes del usuario: mismo color

---

## PASO 3 — GOOGLE BUSINESS PROFILE

**URL:** business.google.com

### Datos a completar:
| Campo | Contenido |
|-------|-----------|
| Nombre | [Nombre completo — Profesión] |
| Categoría principal | [La más específica disponible] |
| Categoría secundaria | [Complementaria si aplica] |
| Tipo | Tienda local (si recibe visitas) |
| Dirección | Calle, número, ciudad, provincia |
| Teléfono | +549XXXXXXXXXX |
| Sitio web | URL del sitio |
| Chat | WhatsApp → `https://wa.me/549XXXXXXXXXX` |

### Descripción (máx 750 caracteres):
```
[Profesión y especialidad]. [Servicios principales]. [Premio o logro destacado si tiene].
[Qué puede hacer el cliente: visitar, comprar, consultar]. Consultas por WhatsApp.
```

### Fotos a subir:
- Foto de portada: la más impactante
- Logotipo: foto del titular o logo
- Fotos del lugar: interior y exterior
- Fotos del trabajo/productos: 3-5 imágenes
- Fotos de la persona trabajando

---

## PASO 4 — GOOGLE SEARCH CONSOLE

**URL:** search.google.com/search-console

### Proceso:
1. Agregar propiedad → **Prefijo de la URL**
2. Pegar la URL exacta del sitio
3. Verificar con **Etiqueta HTML**:
   - Copiar el `<meta name="google-site-verification" content="...">` que genera
   - Pegarlo en el `<head>` del index.html, antes del SEO
   - Hacer commit y push
   - Esperar 2-3 minutos
   - Clic en "Verificar"
4. Ir a **Inspección de URLs**
5. Pegar la URL del sitio
6. Clic en **"Solicitar indexación"**

### Tiempos esperados:
- Verificación: inmediata
- Fotos Google Business aprobadas: horas a 1 día
- Sitio en resultados de búsqueda: 2-4 días
- Perfil de Maps visible al público: 3-7 días

---

## PASO 5 — INSTAGRAM

- Agregar la URL del sitio en la **bio** del perfil de Instagram
- Usar hashtags relevantes en las publicaciones
- Reels del proceso de trabajo → mayor alcance orgánico

---

## CHECKLIST FINAL

- [ ] SEO meta tags agregados al HTML
- [ ] Imagen horizontal 1.5:1 o más para preview en redes
- [ ] Open Graph y Twitter Card configurados
- [ ] Agente IA con Gemini funcionando
- [ ] Google Business Profile creado con fotos
- [ ] Google Search Console verificado
- [ ] Indexación solicitada
- [ ] Link en bio de Instagram

---

## TIEMPOS TOTALES

| Tarea | Tiempo estimado |
|-------|----------------|
| SEO + Agente IA | 30-60 min |
| Google Business Profile | 15 min |
| Google Search Console | 10 min |
| Instagram bio | 2 min |
| **Total** | **~1 hora** |

---

*Guía creada por Fernando Adrian Nebro — Mayo 2026*
*Aplicada en: Sitio web Roxana Matilde Romano*
