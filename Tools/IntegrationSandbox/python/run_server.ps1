$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $Python)) { throw 'Run .\setup.ps1 first.' }
$env:PYTHONPATH = (Join-Path $PSScriptRoot 'src')
& $Python -m spaceverse_mock.server --host 127.0.0.1 --port 50051
if ($LASTEXITCODE -ne 0) { throw 'Mock server exited with an error.' }
