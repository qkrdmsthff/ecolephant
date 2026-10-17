[CmdletBinding()]
param([string]$PythonPath, [string]$AsOf)
$ErrorActionPreference = 'Stop'
$entryPath = Join-Path $PSScriptRoot 'doc_gardening.py'
$repoPath = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$entryArgs = @($entryPath)
if ($AsOf) { $entryArgs += @('--as-of', $AsOf) }
if ($PythonPath) {
    & $PythonPath @entryArgs
} elseif (Test-Path -LiteralPath (Join-Path $repoPath '.venv/Scripts/python.exe')) {
    & (Join-Path $repoPath '.venv/Scripts/python.exe') @entryArgs
} elseif (Test-Path -LiteralPath (Join-Path $repoPath '.venv/bin/python')) {
    & (Join-Path $repoPath '.venv/bin/python') @entryArgs
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 @entryArgs
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    & python3 @entryArgs
} else { throw 'Python 3.10+ 경로를 지정하세요.' }
if ($LASTEXITCODE -ne 0) { throw '문서 정비 보고에 실패했습니다.' }
