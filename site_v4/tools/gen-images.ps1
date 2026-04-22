# Image generator for site_v4 — Azure FLUX.2-pro
# Usage:  $env:FLUX_KEY='...'; powershell -ExecutionPolicy Bypass -File .\tools\gen-images.ps1
# Key is read from env var only. Never written to disk.

param([string]$Only = '')

$ErrorActionPreference = 'Continue'
$key = $env:FLUX_KEY
if (-not $key) { Write-Error 'Set $env:FLUX_KEY before running'; exit 1 }

$url   = 'https://ba2rba-2051-resource.services.ai.azure.com/providers/blackforestlabs/v1/flux-2-pro?api-version=preview'
$root  = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
$imgDir = Join-Path $root 'img'
New-Item -ItemType Directory -Force -Path $imgDir | Out-Null

# Consistent look: real film stock, zero AI tells, no people, no screens
$style = 'Documentary industrial still-life photograph, archival photojournalism style. Shot on Kodak Portra 400 35mm film, natural color, no color grading. Frame fully filled with dense technical machinery and mechanical detail: pipes, fittings, valves, cables, brackets, components visible everywhere in the image. Tight close-up framing, subject occupies the whole frame edge to edge, no negative space, no empty walls, no empty floor. Realistic factory patina: oil stains, light surface rust, dust, paint chips, wear marks, grease, scratches. Sharp technical focus, shallow depth of field on a key component. No people, no humans, no workers, no hands in frame. No digital screens, no HMI touchscreens, no monitors, no LCD displays. Authentic, technical, real, looks like a real industrial photograph, not AI generated.'

$imgs = @(
  @{ n='hero'; w=1344; h=768; p=(
    "Wide documentary photograph of an industrial utility wall inside a factory maintenance area: a row of five analog brass pressure gauges mounted on a stainless steel manifold, red-handled isolation valves, copper and stainless fittings, pipe racks in the background, a coiled pneumatic hose hanging from a hook. Industrial patina. " + $style) },

  @{ n='int01'; w=1024; h=1024; p=(
    "Documentary photograph of the infeed section of an industrial cardboard case-packer machine on a PET bottle line. Stainless steel conveyor rollers with light blue plastic PET bottles queued. A yellow-painted steel safety guard with black hazard stripes. A small cylindrical photoelectric sensor mounted on a steel bracket, equipped with a compressed air purge fitting (visible copper tube). Lubricant residue on the guide rails. Cool fluorescent factory lighting. " + $style) },

  @{ n='int02'; w=1024; h=1024; p=(
    "Documentary photograph of a large industrial plastic injection molding press on a factory floor: riveted steel blue painted frame, thick black braided hydraulic hoses with brass fittings, a resin granule dryer tower in the background with visible stainless ducting, the open clamp zone showing nickel-plated steel mold tooling, a riveted manufacturer plate on the side, oil drips below. Shop floor lighting through translucent roof panels. " + $style) },

  @{ n='int03'; w=1024; h=1024; p=(
    "Documentary close-up photograph of the open interior of an industrial electrical control cabinet (door removed). Color-coded wires bundled and routed through grey plastic cable trunking, a DIN rail populated with grey relays and miniature circuit breakers, fuse holders, numbered push-in terminal blocks in rows, a copper grounding bar at the bottom, black cable ties. Slight dust. " + $style) },

  @{ n='int04'; w=1024; h=1024; p=(
    "Documentary macro photograph of an industrial electrical test fixture for automotive wire harnesses: a rectangular 32-pin connector adapter block with brass pins arranged in a grid (visible oxidation on a few pins), clamped by a small pneumatic cylinder, colored wires fanned out from the connector, an aluminum jig base drilled with a pattern of holes, a small pneumatic manifold with brass fittings. Factory workbench surface. " + $style) },

  @{ n='int05'; w=1024; h=1024; p=(
    "Documentary photograph of an industrial hydraulic press valve detail: a riveted steel frame, oil-stained black braided hydraulic hoses with swivel fittings, a large analog pressure gauge with a brass bezel reading approximately 80 bar (dial clearly visible with black numerals on white face), a steel pressure accumulator bottle, a hydraulic valve manifold block with hex-head cap screws. Oil drips on the concrete floor below. " + $style) },

  @{ n='int06'; w=1024; h=1024; p=(
    "Documentary photograph of a printed maintenance planning wall board inside an industrial corridor: a large paper Gantt chart pinned to a cork board with colored plastic magnets, hand-annotated with pencil markings, machine reference codes down the left column, week numbers across the top, colored horizontal bars representing scheduled maintenance tasks. Fluorescent corridor light. Small taped legend card in the corner. " + $style) }
)

foreach ($i in $imgs) {
  if ($Only -and ($i.n -notlike "*$Only*")) { continue }
  $out = Join-Path $imgDir "$($i.n).png"
  Write-Host ("-> {0}  {1}x{2}" -f $i.n, $i.w, $i.h)
  $body = @{ prompt=$i.p; model='FLUX.2-pro'; width=$i.w; height=$i.h; n=1 } | ConvertTo-Json -Depth 3
  $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($body)
  try {
    $resp = Invoke-RestMethod -Uri $url -Method Post -Headers @{ Authorization = "Bearer $key"; 'Content-Type' = 'application/json; charset=utf-8' } -Body $bodyBytes -TimeoutSec 240
    $b64 = $resp.data[0].b64_json
    if (-not $b64) { Write-Host "   ! no b64_json"; continue }
    $imgBytes = [Convert]::FromBase64String($b64)
    [System.IO.File]::WriteAllBytes($out, $imgBytes)
    Write-Host ("   ok {0,8} bytes" -f $imgBytes.Length)
  } catch {
    Write-Host ("   !! FAIL {0}" -f $_.Exception.Message)
  }
}
Write-Host 'Done.'
