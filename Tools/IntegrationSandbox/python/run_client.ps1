param(
    [string]$Target = '127.0.0.1:50051',
    [string]$EntityId = 'terra-001',
    [int]$Count = 10,
    [int]$IntervalMs = 500
)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$Python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
if (-not (Test-Path $Python)) { throw 'Run .\setup.ps1 first.' }
$env:PYTHONPATH = (Join-Path $PSScriptRoot 'src')
& $Python -m spaceverse_mock.client --target $Target --entity-id $EntityId --count $Count --interval-ms $IntervalMs
if ($LASTEXITCODE -ne 0) { throw 'Mock client failed.' }
