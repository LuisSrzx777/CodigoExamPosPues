# CodigoExamPosPues

# 🔐 KeyLogger Ético - Herramienta Educativa

## ⚠️ ADVERTENCIA LEGAL Y ÉTICA
**Este software es EXCLUSIVAMENTE para fines educativos en ciberseguridad. El uso no autorizado es ILEGAL y puede constituir un delito grave.**

## 🎯 Objetivo Educativo
Demostrar cómo funcionan los keyloggers para:
- Concienciar sobre amenazas de seguridad
- Aprender técnicas de detección
- Desarrollar contramedidas
- Entender análisis forense digital

## 📊 Análisis de Datos
El keylogger genera:

Log con timestamps de cada tecla

Estadísticas de frecuencia

Patrones de tecleo (fines educativos)

🛡️ Medidas de Seguridad Incorporadas
Límite de tiempo automático

Advertencias éticas constantes

Requiere consentimiento explícito

Solo para ambientes controlados

📚 Casos de Uso Válidos

✅ Laboratorios de ciberseguridad

✅ Pruebas en máquinas propias

✅ Investigación académica

✅ Auditorías autorizadas


❌ Usos Prohibidos

❌ En equipos sin autorización

❌ Para espiar a otras personas

❌ Con fines maliciosos

❌ Fuera de ambientes controlados

🎓 Valor Educativo

Este proyecto enseña:

Programación de bajo nivel

Gestión de eventos del sistema

Ética en ciberseguridad

Análisis forense básico

Detección de malware

📞 Responsabilidad
El usuario es completamente responsable del uso ético y legal de este software. Los desarrolladores no se responsabilizan por uso indebido.






---------------------------------------------------------------------------------------------------


### Clases Principales

#### 1. EthicalKeyLogger
- **Atributos**: Archivo de log, estado, buffer de teclas
- **Métodos**: Iniciar/detener logging, monitoreo, análisis

#### 2. KeyLoggerManager  
- **Atributos**: Instancia del keylogger
- **Métodos**: Gestión del ciclo de vida, temporizador

## 🚀 Características Técnicas

- **Registro timestamp**: Cada tecla con fecha/hora exacta
- **Buffer en memoria**: Optimiza I/O del disco
- **Guardado periódico**: Auto-guardado cada 30 segundos
- **Límite educativo**: Máximo 5 minutos de ejecución
- **Tecla de parada**: F12 para detener manualmente
- **Análisis básico**: Estadísticas de uso

## 🔧 Instalación y Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar (requiere permisos administrador)
sudo python keylogger.py
