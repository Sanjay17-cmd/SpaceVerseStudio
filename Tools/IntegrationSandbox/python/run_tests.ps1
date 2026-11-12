$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $Python)) { throw 'Run .\setup.ps1 first.' }
$env:PYTHONPATH = (Join-Path $PSScriptRoot 'src')
& $Python -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Contract tests failed.' }
