import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Comando nativo inicial obligatorio)
st.set_page_config(
    page_title="BioPath-Sentinel AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. PERSONALIZACIÓN DE COLOR DE FONDO Y TEXTOS BASE VIA CSS SEGURO
st.markdown("""
    <style>
    .stApp {
        background-color: #020617;
        color: #f8fafc;
    }
    h1, h2, h3, h4 {
        color: #ffffff !important;
    }
    p, li {
        color: #cbd5e1 !important;
    }
    /* Estilo sutil para los bordes de los contenedores nativos */
    .stElementContainer div[data-testid="stContainer"] {
        border-color: rgba(255, 255, 255, 0.1) !important;
        background-color: rgba(30, 41, 59, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO PRINCIPAL
st.markdown("<h1 style='text-align: center; font-size: 45px;'>BioPath-Sentinel AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #14b8a6 !important; font-size: 20px; font-weight: 300;'>Ecosistema de Inteligencia Sanitaria y Analítica Médica</p>", unsafe_allow_html=True)

st.write("---")

# 4. LAS DOS SOLUCIONES OPERATIVAS ACTUALES
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.caption("SFTW PREDICTIVO INDEPENDIENTE")
        st.subheader("HiSalud Diabetes")
        
        st.markdown(":italic[[Anticípate al riesgo. Transforma datos en prevención familiar y clínica.]]")
        
        st.write(
            "Nuestro asistente analítico inteligente diseñado para **personal de salud, enfermeros, "
            "nutricionistas, entrenadores de bienestar o cualquier persona** que necesite realizar un "
            "tamizaje ágil de riesgo de diabetes. Ingresa los factores clave en menos de 2 minutos, "
            "genera la métrica estadística basada en IA y almacena el histórico en tu base de datos dedicada."
        )
        
        st.write("### Suscripción Mensual:")
        st.markdown("<h2 style='color: #00f5d4 !important; margin-top: -10px;'>$90.000 COP <span style='font-size: 16px; color:#94a3b8;'>/ mes</span></h2>", unsafe_allow_html=True)
        
        st.markdown("- Acceso inmediato al portal interactivo en Streamlit.\n- Base de datos aislada en Azure para tus registros.\n- Historial visual y reporte de tamizajes.")
        
        # Botón de Pago directo que redirige a tu pasarela de Wompi
        st.link_button(
            label="Activar HiSalud Diabetes - $90.000",
            url="https://checkout.wompi.co/l/TU_LINK_DE_PAGO",  # Reemplaza 'TU_LINK_DE_PAGO' por tu ID final de Wompi cuando lo pegues en GitHub
            use_container_width=True
        )

with col2:
    with st.container(border=True):
        st.caption("INFRAESTRUCTURA HOSPITALARIA")
        st.subheader("BioPath HCE Enterprise")
        
        st.markdown(":italic[[Gestión clínica Multi-tenant: el corazón operativo de tu institución.]]")
        
        st.write(
            "La suite integral de Historia Clínica Electrónica (HCE) avanzada basada en **FastAPI**. "
            "Diseñada bajo arquitectura **Multi-tenant** para clínicas e IPS, permitiendo que múltiples "
            "instituciones operen de forma centralizada pero con absoluto aislamiento de datos. "
            "Integra consulta, farmacia, laboratorios y facturación en un entorno blindado."
        )
        
        st.write("### Alquiler Institucional:")
        st.markdown("<h2 style='color: #22d3ee !important; margin-top: -10px;'>Planes Corporativos</h2>", unsafe_allow_html=True)
        
        st.markdown("- Múltiples accesos para personal administrativo y asistencial.\n- Identidad y seguridad robusta con Azure AD B2C.\n- Privacidad de datos indexada por entorno institucional.")
        
        # Botón de contacto comercial directo para cotizaciones institucionales
        st.link_button(
            label="💬 Agendar Demo Corporativa / Cotización",
            url="https://wa.me/573000000000?text=Hola,%20solicito%20una%20demostración%20empresarial%20de%20BioPath%20HCE", # Reemplaza el número de teléfono por el tuyo
            use_container_width=True
        )

# 5. PRÓXIMOS LANZAMIENTOS (Ecosistema Futuro)
st.write("---")
st.markdown("<h3 style='text-align: center;'>Próximas Soluciones en Desarrollo (Ecosistema HiSalud)</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8 !important;'>Expandiendo la prevención inteligente a más áreas del cuidado clínico.</p>", unsafe_allow_html=True)

col_f1, col_f2 = st.columns(2)

with col_f1:
    with st.container(border=True):
        st.caption("CARDIOVASCULAR")
        st.markdown("**HiSalud Hipertensión**")
        st.write("Modelos predictivos analíticos para evaluar el riesgo de presión arterial elevada y eventos cardiovasculares tempranos.")

with col_f2:
    with st.container(border=True):
        st.caption("ENDOCRINOLOGÍA")
        st.markdown("**HiSalud Metabólica**")
        st.write("Evaluación integral de síndrome metabólico, combinando métricas de peso, lípidos y perfiles genómicos preliminares.")

# 6. INGRESO DE USUARIOS CON TUS SUBDOMINIOS REALES (.ONLINE)
st.write("---")
st.markdown("<h3 style='text-align: center;'>¿Ya tienes una cuenta activa?</h3>", unsafe_allow_html=True)

col_c1, col_c2 = st.columns(2)

with col_c1:
    st.link_button(
        label="Entrar a HiSalud Diabetes",
        url="https://diabetes.biopathsentinel.online",
        use_container_width=True
    )

with col_c2:
    st.link_button(
        label="Entrar a BioPath HCE Enterprise",
        url="https://clinicas.biopathsentinel.online",
        use_container_width=True
    )

# 7. AVISO LEGAL
st.write("---")
st.warning(
    "AVISO LEGAL Y CONDICIONES DE USO: Esta plataforma proporciona estimaciones analíticas "
    "basadas en modelos estadísticos de factores de riesgo. No reemplaza, ni constituye un "
    "diagnóstico médico formal, ni sustituye el criterio del personal de salud calificado. "
    "Es responsabilidad del usuario realizar los exámenes de laboratorio pertinentes para la "
    "confirmación de cualquier diagnóstico."
)
   
