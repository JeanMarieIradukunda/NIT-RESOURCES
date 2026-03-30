$rootPath = "C:\inetpub\nit-resources"
$newIcon = '<link rel="icon" href="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" type="image/png">'

Get-ChildItem -Path $rootPath -Recurse -Filter "index.html" | ForEach-Object {

    $file = $_.FullName
    $content = Get-Content $file -Raw

    # Remove existing favicon links
    $content = $content -replace '<link[^>]*rel=["'']?icon["'']?[^>]*>', ''

    # Insert new favicon before </head>
    if ($content -match '</head>') {
        $content = $content -replace '</head>', "    $newIcon`n</head>"
        Copy-Item $file "$file.bak" -Force
        Set-Content -Path $file -Value $content -Encoding UTF8

        Write-Host "Updated: $file"
    }
    else {
        Write-Host "Skipped (no </head>): $file"
    }
}
