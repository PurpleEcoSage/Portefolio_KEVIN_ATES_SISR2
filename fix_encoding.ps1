$path = "index.html"
$content = Get-Content $path -Raw

# Helper to build string from char code
function C($code) { return [string][char]$code }

$replacements = @{}

# Ã© -> é
$k = (C 0xC3) + (C 0xA9)
$replacements[$k] = "é"

# Ã¨ -> è
$k = (C 0xC3) + (C 0xA8)
$replacements[$k] = "è"

# Ãª -> ê
$k = (C 0xC3) + (C 0xAA)
$replacements[$k] = "ê"

# Ã¢ -> â
$k = (C 0xC3) + (C 0xA2)
$replacements[$k] = "â"

# Ã´ -> ô
$k = (C 0xC3) + (C 0xB4)
$replacements[$k] = "ô"

# Ã® -> î
$k = (C 0xC3) + (C 0xAE)
$replacements[$k] = "î"

# Ã¯ -> ï
$k = (C 0xC3) + (C 0xAF)
$replacements[$k] = "ï"

# Ã» -> û
$k = (C 0xC3) + (C 0xBB)
$replacements[$k] = "û"

# Ã¹ -> ù
$k = (C 0xC3) + (C 0xB9)
$replacements[$k] = "ù"

# Ã§ -> ç
$k = (C 0xC3) + (C 0xA7)
$replacements[$k] = "ç"

# Å“ -> œ
$k = (C 0xC5) + (C 0x93)
$replacements[$k] = "œ"

# Ã‰ -> É
$k = (C 0xC3) + (C 0x89)
$replacements[$k] = "É"

# Ã€ -> À
$k = (C 0xC3) + (C 0x80)
$replacements[$k] = "À"

# Ã  -> à (nbsp)
$k = (C 0xC3) + (C 0xA0)
$replacements[$k] = "à"

# â€™ -> '
$k = (C 0xE2) + (C 0x80) + (C 0x99)
$replacements[$k] = "'"

# â€“ -> -
$k = (C 0xE2) + (C 0x80) + (C 0x93)
$replacements[$k] = "-"

# â€¢ -> •
$k = (C 0xE2) + (C 0x80) + (C 0xA2)
$replacements[$k] = "•"

foreach ($key in $replacements.Keys) {
    if ($content.Contains($key)) {
        $content = $content.Replace($key, $replacements[$key])
    }
}

$content | Set-Content $path -Encoding UTF8
Write-Host "Encoding fix complete."
