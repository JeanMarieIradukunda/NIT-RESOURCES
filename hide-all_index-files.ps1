# Path to the main directory
$basePath = "C:\inetpub\nit-resources"

# Recursively find all index.html files
$indexFiles = Get-ChildItem -Path $basePath -Recurse -Filter "index.html"

foreach ($file in $indexFiles) {
    Write-Host "Processing $($file.FullName)..."

    # Read the content of the file
    $content = Get-Content -Path $file.FullName

    # Remove lines containing 'index.html' or 'index.html.bak'
    $updatedContent = $content | Where-Object { $_ -notmatch "index\.html(\.bak)?" }

    # Save changes back to the file
    Set-Content -Path $file.FullName -Value $updatedContent -Force

    Write-Host "Updated $($file.FullName)"
}

Write-Host "All index.html files have been updated."
