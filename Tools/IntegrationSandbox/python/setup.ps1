$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

$Version = & python --version 2>&1
if ($LASTEXITCODE -ne 0) { throw 'Python was not found. Install Python 3.11 or newer and reopen PowerShell.' }
$VersionCheck = & python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ([version]$VersionCheck -lt [version]'3.11') { throw "Python 3.11 or newer is required. Found $VersionCheck." }
Write-Host "Using $Version"

if (-not (Test-Path '.venv\Scripts\python.exe')) {
    & python -m venv .venv
    if ($LASTEXITCODE -ne 0) { throw 'Could not create virtual environment.' }
}
$Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
& $Python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw 'pip upgrade failed.' }
& $Python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Dependency installation failed.' }
& $Python -m grpc_tools.protoc -I ..\proto --python_out=src --pyi_out=src --grpc_python_out=src ..\proto\spaceverse\v1\simulation.proto
if ($LASTEXITCODE -ne 0) { throw 'Protocol Buffers generation failed.' }
Write-Host 'Setup complete. Run .\run_tests.ps1, then .\run_server.ps1.' -ForegroundColor Green
