[CmdletBinding()]
param([string]$PythonPath)
$ErrorActionPreference = 'Stop'
$checkerPath = Join-Path $PSScriptRoot 'check.py'

if ($PythonPath) {
    & $PythonPath $checkerPath
} else {
    $repoPath = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
    $localPython = Join-Path $repoPath '.venv/Scripts/python.exe'
    $unixPython = Join-Path $repoPath '.venv/bin/python'
    if (Test-Path -LiteralPath $localPython) {
        & $localPython $checkerPath
    } elseif (Test-Path -LiteralPath $unixPython) {
        & $unixPython $checkerPath
    } elseif (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3 $checkerPath
    } elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
        & python3 $checkerPath
    } else {
        throw 'Python 3.10+ 경로를 -PythonPath로 지정하세요. README의 검사 환경 설치 절차를 확인하세요.'
    }
}
if ($LASTEXITCODE -ne 0) { throw '문서·계약 검사에 실패했습니다.' }
