# ===================================================
# Academic Resource Portal Generator (UNIFIED UI)
# All index.html files match the Dashboard design
# ===================================================

$RootPath = "C:\inetpub\nit-resources"
$SortBy = "name"

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

# ---------- GENERATE INDEX ----------
function Generate-Index($Path) {

    $Title = Split-Path $Path -Leaf
    $Items = Get-ChildItem $Path | Where-Object { $_.Name -ne "index.html" }
    $Folders = $Items | Where-Object { $_.PSIsContainer }
    $Files   = $Items | Where-Object { -not $_.PSIsContainer }

    if ($SortBy -eq "size") {
        $Files = $Files | Sort-Object Length
    } else {
        $Files = $Files | Sort-Object Name
    }

    $Cards = ""

    # -------- FOLDER CARDS --------
    foreach ($f in $Folders) {
        $fileCount = (Get-ChildItem $f.FullName -File -Recurse | Measure-Object).Count
        $class = Get-FolderClass $f.Name

        $Cards += @"
<a href='$($f.Name)/' class='folder-card $class'>
    <i class='bi bi-folder-fill'></i>
    <div class='folder-title'>$($f.Name)</div>
    <div class='folder-meta'>Files: $fileCount</div>
</a>
"@
    }

    # -------- FILE CARDS --------
    foreach ($file in $Files) {
        $size = Format-FileSize $file.Length
        $ext  = $file.Extension.TrimStart('.').ToUpper()

        $Cards += @"
<a href='$($file.Name)' class='folder-card resources'>
    <i class='bi bi-file-earmark-fill'></i>
    <div class='folder-title'>$($file.BaseName)</div>
    <div class='folder-meta'>$ext · $size</div>
</a>
"@
    }

    # -------- PARENT LINK --------
    if ((Split-Path $Path -Parent) -ne $Path) {
        $Cards = @"
<a href='../' class='folder-card courses'>
    <i class='bi bi-arrow-left-circle-fill'></i>
    <div class='folder-title'>Parent Directory</div>
    <div class='folder-meta'>Go Back</div>
</a>
"@ + $Cards
    }

$HTML = @"
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>$Title</title>

<link href='$BootstrapCSS' rel='stylesheet'>
<link href='$BootstrapIcons' rel='stylesheet'>

<style>
body {
    font-family: "Segoe UI", system-ui, sans-serif;
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.dashboard-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 35px 30px;
    max-width: 1100px;
    width: 100%;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}
.dashboard-title {
    text-align: center;
    margin-bottom: 30px;
}
.dashboard-title h1 {
    font-size: 1.8rem;
    font-weight: 700;
    color: #1f2937;
}
.dashboard-title p {
    color: #6b7280;
}
.folder-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 25px;
}
.folder-card {
    text-decoration: none;
    border-radius: 16px;
    padding: 25px 20px;
    text-align: center;
    transition: all 0.25s ease;
    color: #111827;
}
.folder-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 25px rgba(0,0,0,0.18);
}
.folder-card i {
    font-size: 52px;
    margin-bottom: 12px;
}
.folder-title {
    font-weight: 700;
    font-size: 1.05rem;
}
.folder-meta {
    font-size: 0.85rem;
    color: #374151;
}

/* COLORS */
.exams { background:#fde68a; }
.courses { background:#bfdbfe; }
.classes { background:#bbf7d0; }
.resources { background:#e9d5ff; }

.exams i { color:#92400e; }
.courses i { color:#1e40af; }
.classes i { color:#065f46; }
.resources i { color:#6b21a8; }

@media (max-width: 992px) {
    .folder-row { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 576px) {
    .folder-row { grid-template-columns: 1fr; }
}
</style>
</head>

<body>

<div class='dashboard-card'>
    <div class='dashboard-title'>
        <h1>$Title</h1>
        <p>Academic Resource Portal</p>
    </div>

    <div class='folder-row'>
        $Cards
    </div>
</div>

</body>
</html>
"@

    $HTML | Set-Content -Encoding UTF8 "$Path\index.html"
    Write-Host "Generated UI index in $Path" -ForegroundColor Green
}

# ---------- RECURSIVE ----------
function Process-Folder($Path) {
    Generate-Index $Path
    Get-ChildItem $Path -Directory | ForEach-Object {
        Process-Folder $_.FullName
    }
}

Process-Folder $RootPath
Write-Host "ALL index.html files now match the Academic Resource Portal design!" -ForegroundColor Cyan
