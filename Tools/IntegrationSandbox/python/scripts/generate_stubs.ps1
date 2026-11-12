$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)
$Python = Join-Path (Get-Location) '.venv\Scripts\python.exe'
if (-not (Test-Path $Python)) { throw 'Virtual environment not found. Run .\setup.ps1 first.' }
& $Python -m grpc_tools.protoc `
  -I ..\proto `
  --python_out=src `
  --pyi_out=src `
  --grpc_python_out=src `
  ..\proto\spaceverse\v1\simulation.proto
if ($LASTEXITCODE -ne 0) { throw 'Protocol Buffers code generation failed.' }
Write-Host 'Generated Python protobuf and gRPC files under src\spaceverse\v1.' -ForegroundColor Green
