
import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="BioPath-Sentinel AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILOS CSS - MODO OSCURO "PRO"
st.markdown("""
    <style>
    .stApp {
        background-color: #020617;
        color: #f8fafc;
    }
    .main-title {
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #ffffff, #14b8a6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .main-subtitle {
        font-size: 22px;
        color: #14b8a6;
        text-align: center;
        font-weight: 300;
        margin-bottom: 40px;
    }
    .product-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 20px;
        height: 100%;
    }
    .future-card {
        background: rgba(30, 41, 59, 0.15);
        border: 1px dashed rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
    .product-badge {
        background-color: rgba(20, 184, 166, 0.2);
        color: #22d3ee;
        padding: 5px 12px;
        border-radius: 50px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 15px;
    }
    .future-badge {
        background-color: rgba(245, 158, 11, 0.1);
        color: #f59e0b;
        padding: 4px 10px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }
    .btn-pago-diabetes {
        display: block;
        text-align: center;
        background: linear-gradient(90deg, #14b8a6, #0ea5e9);
        color: white !important;
        font-weight: 600;
        padding: 12px 24px;
        border-radius: 10px;
        text-decoration: none;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(20, 184, 166, 0.4);
    }
    .btn-pago-hce {
        display: block;
        text-align: center;
        background: transparent;
        color: #22d3ee !important;
        border: 2px solid #22d3ee;
        font-weight: 600;
        padding: 10px 24px;
        border-radius: 10px;
        text-decoration: none;
        margin-top: 20px;
    }
    .disclaimer-box {
        background-color: rgba(30, 41, 59, 0.3);
        border-left: 4px solid #f59e0b;
        padding: 20px;
        border-radius: 8px;
        margin-top: 50px;
        font-size: 14px;
        color: #94a3b8;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO DE LA PLATAFORMA MATRIZ
st.markdown('<h1 class="main-title">BioPath-Sentinel AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Ecosistema de Inteligencia Sanitaria y Analítica Médica</p>', unsafe_allow_html=True)

st.write("---")

# 4. LAS DOS SOLUCIONES COMERCIALES ACTUALES
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="product-card">
        <span class="product-badge">🧠 SFTW PREDICTIVO INDEPENDIENTE</span>
        <h2 style='color: #ffffff; margin-top:0;'>HiSalud Diabetes</h2>
        <p style='color: #14b8a6; font-style: italic; font-size: 18px;'>
            "Anticípate al riesgo. Transforma datos en prevención familiar y clínica."
        </p>
        <p style='color: #94a3b8; font-size: 16px; text-align: justify;'>
            Nuestro asistente analítico inteligente diseñado para <b>personal de salud, enfermeros, nutricionistas, entrenadores de bienestar o cualquier persona</b> que necesite realizar un tamizaje ágil de riesgo de diabetes. Ingresa los factores clave en menos de 2 minutos, genera la métrica estadística basada en IA y almacena el histórico en tu base de datos dedicada.
        </p>
        <h3 style='color: #ffffff; margin-bottom: 5px;'>Suscripción Mensual:</h3>
        <p style='color: #00f5d4; font-size: 28px; font-weight: 700; margin-top:0;'>
            $90.000 COP <span style='font-size: 16px; color:#94a3b8;'>/ mes</span>
        </p>
        <ul style='color: #cbd5e1; padding-left: 20px;'>
            <li>Acceso inmediato al portal interactivo en Streamlit.</li>
            <li>Base de datos aislada en Azure para tus registros.</li>
            <li>Historial visual y reporte de tamizajes.</li>
        </ul>
        <a class="btn-pago-diabetes" href="https://checkout.wompi.co/l/TU_LINK_DE_PAGO" target="_blank">
            💳 Activar HiSalud Diabetes - $90.000
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="product-card">
        <span class="product-badge">🏢 INFRAESTRUCTURA HOSPITALARIA</span>
        <h2 style='color: #ffffff; margin-top:0;'>BioPath HCE Enterprise</h2>
        <p style='color: #22d3ee; font-style: italic; font-size: 18px;'>
            "Gestión clínica Multi-tenant: el corazón operativo de tu institution."
        </p>
        <p style='color: #94a3b8; font-size: 16px; text-align: justify;'>
            La suite integral de Historia Clínica Electrónica (HCE) avanzada basada en <b>FastAPI</b>. Diseñada bajo arquitectura <b>Multi-tenant</b> para clínicas e IPS, permitiendo que múltiples instituciones operen de forma centralizada pero con absoluto aislamiento de datos. Integra consulta, farmacia, laboratorios y facturación en un entorno blindado.
        </p>
        <h3 style='color: #ffffff; margin-bottom: 5px;'>Alquiler Institucional:</h3>
        <p style='color: #22d3ee; font-size: 24px; font-weight: 700; margin-top:0;'>
            Planes Corporativos Personalizados
        </p>
        <ul style='color: #cbd5e1; padding-left: 20px;'>
            <li>Múltiples accesos para personal administrativo y asistencial.</li>
            <li>Identidad y seguridad robusta con Azure AD B2C.</li>
            <li>Privacidad de datos indexada por entorno institucional.</li>
        </ul>
        <a class="btn-pago-hce" href="https://wa.me/57TU_NUMERO_DE_WHATSAPP?text=Hola,%20solicito%20una%20demostración%20empresarial%20de%20BioPath%20HCE" target="_blank">
            💬 Agendar Demo Corporativa / Cotización
        </a>
    </div>
    """, unsafe_allow_html=True)

# 5. NUEVA SECCIÓN: FUTUROS LANZAMIENTOS DE HISALUD
st.write("---")
st.markdown("<h3 style='text-align: center; color: white;'>Próximas Soluciones en Desarrollo (Ecosistema HiSalud)</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size:16px;'>Expandiendo la prevención inteligente a más áreas del cuidado clínico.</p>", unsafe_allow_html=True)

col_f1, col_f2 = st.columns(2)

with col_f1:
    st.markdown("""
    <div class="future-card">
        <span class="future-badge">❤️ CARDIOVASCULAR</span>
        <h4 style='color: #ffffff; margin: 5px 0;'>HiSalud Hipertensión</h4>
        <p style='color: #94a3b8; font-size: 14px; margin-bottom: 0;'>
            Modelos predictivos analíticos para evaluar el riesgo de presión arterial elevada y eventos cardiovasculares tempranos.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
    <div class="future-card">
        <span class="future-badge">🧪 ENDOCRINOLOGÍA</span>
        <h4 style='color: #ffffff; margin: 5px 0;'>HiSalud Metabólica</h4>
        <p style='color: #94a3b8; font-size: 14px; margin-bottom: 0;'>
            Evaluación integral de síndrome metabólico, combinando métricas de peso, lípidos y perfiles genómicos preliminares.
        </p>
    </div>
    """, unsafe_allow_html=True)

# 6. INGRESO DE USUARIOS YA REGISTRADOS (CON LINKS REALES)
st.write("---")
st.markdown("<h3 style='text-align: center; color: white;'>¿Ya tienes una cuenta activa?</h3>", unsafe_allow_html=True)

col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("""
        <a href="https://diabetes.biopathsentinel.online" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                background-color: #1e293b;
                color: #f8fafc;
                border: 1px solid rgba(255,255,255,0.1);
                padding: 10px;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                transition: 0.3s;
            ">
                🚀 Entrar a HiSalud Diabetes
            </button>
        </a>
    """, unsafe_allow_html=True)

with col_c2:
    st.markdown("""
        <a href="https://clinicas.biopathsentinel.online" target="_blank" style="text-decoration: none;">
            <button style="
                width: 100%;
                background-color: #1e293b;
                color: #f8fafc;
                border: 1px solid rgba(255,255,255,0.1);
                padding: 10px;
                border-radius: 8px;
                font-weight: 600;
                cursor: pointer;
                transition: 0.3s;
            ">
                🏢 Entrar a BioPath HCE Enterprise
            </button>
        </a>
    """, unsafe_allow_html=True)

# 7. AVISO LEGAL
st.markdown("""
<div class="disclaimer-box">
    <b>⚠️ AVISO LEGAL Y CONDICIONES DE USO:</b><br>
    Esta plataforma proporciona estimaciones analíticas basadas en modelos estadísticos de factores de riesgo. 
    <b>No reemplaza, ni constituye un diagnóstico médico formal</b>, ni sustituye el criterio del personal de salud calificado. 
    Es responsabilidad del usuario realizar los exámenes de laboratorio pertinentes para la confirmación de cualquier diagnóstico.
</div>
""", unsafe_allow_html=True)