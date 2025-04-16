@echo off
:: Verificar si Python esta instalado
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python no esta instalado. Redirigiendo a la pagina de instalacion...
    start https://www.python.org/downloads/
    exit /b
)

:: Verificar si pip esta instalado
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip no esta instalado. Instalando pip...
    python -m ensurepip --upgrade
)

:: Verificar si el entorno virtual ya existe
if exist "entornoVirtualTrashProject" (
    echo El entorno virtual ya existe. Activando el entorno...
) else (
    :: Crear entorno virtual si no existe
    python -m venv entornoVirtualTrashProject
    echo Entorno virtual creado con exito.
)

:: Activar el entorno virtual
call entornoVirtualTrashProject\Scripts\activate

:: Instalar dependencias desde requirements.txt
pip install -r requirements.txt

:: Mensaje de exito
echo ✅ Entorno virtual creado e instalado con exito.
echo Backend de Python con SQLAlchemy para PostgreSQL por Lenin Ospina Lamprea, MIT License.

:: Ejecutar la aplicacion
echo ▶ Ejecutando: python App.py
python App.py