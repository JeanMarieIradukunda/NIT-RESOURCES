# ===================================================
# Academic Resource Portal Enhancer (Parent Directory Header)
# Updates all index.html files in nit-resources
# ===================================================

$RootPath = "C:\inetpub\nit-resources"
$BootstrapCSS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
$BootstrapIcons = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css"

# ---------- FILE SIZE ----------
function Format-FileSize($bytes) {
    if ($bytes -ge 1GB) { "{0:N2} GB" -f ($bytes / 1GB) }
    elseif ($bytes -ge 1MB) { "{0:N1} MB" -f ($bytes / 1MB) }
    elseif ($bytes -ge 1KB) { "{0:N0} KB" -f ($bytes / 1KB) }
    else { "$bytes B" }
}

# ---------- COLOR BY FOLDER NAME ----------
function Get-FolderClass($name) {
    switch -Regex ($name.ToLower()) {
        "exam"      { "exams" }
        "course|l3" { "courses" }
        "class|l4"  { "classes" }
        "resource|l5|project" { "resources" }
        default     { "courses" }
    }
}

# ---------- ENHANCE INDEX ----------
function Enhance-Index($Path) {

    # Read current index.html content if exists
    $indexFile = Join-Path $Path "index.html"
    if (-Not (Test-Path $indexFile)) { return }

    $HTML = Get-Content -Path $indexFile -Raw

    # Extract the dashboard title
    $TitleMatch = [regex]::Match($HTML, '<h1>(.*?)</h1>')
    $Title = if ($TitleMatch.Success) { $TitleMatch.Groups[1].Value } else { Split-Path $Path -Leaf }

    # Determine parent link
    $ParentPath = Split-Path $Path -Parent
    $IncludeParent = if ($ParentPath -ne $Path) { $true } else { $false }

    # Construct parent header HTML
    $ParentHeader = ""
    if ($IncludeParent) {
        $ParentHeader = @"
<div class='parent-header mb-3 p-3 rounded' style='background:#f0f9ff; display:flex; align-items:center; gap:12px;'>
    <a href='../' style='text-decoration:none; color:#1e40af; font-weight:600; display:flex; align-items:center; gap:6px;'>
        <i class='bi bi-arrow-left-circle-fill' style='font-size:1.5rem;'></i> Parent Directory
    </a>
</div>
"@
    }

    # Insert parent header inside the dashboard-card, just above folder-row
    $HTML = [regex]::Replace($HTML, "(<div class='folder-row'>)", "$ParentHeader`$1", [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

    # Save updated HTML back
    Set-Content -Path $indexFile -Value $HTML -Encoding UTF8
    Write-Host "Enhanced parent header in $indexFile" -ForegroundColor Green
}

# ---------- RECURSIVE ----------
function Process-Folder($Path) {
    Enhance-Index $Path
    Get-ChildItem $Path -Directory | ForEach-Object {
        Process-Folder $_.FullName
    }
}

Process-Folder $RootPath
Write-Host "ALL index.html files now include professional Parent Directory header!" -ForegroundColor Cyan
