# Maya global shortcuts for Windows.
# This listener only launches Maya's fixed local scripts; it accepts no user-supplied commands.
Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class MayaHotKeys {
  [DllImport("user32.dll")] public static extern bool RegisterHotKey(IntPtr hWnd, int id, uint fsModifiers, uint vk);
  [DllImport("user32.dll")] public static extern bool UnregisterHotKey(IntPtr hWnd, int id);
  [DllImport("user32.dll")] public static extern int GetMessage(out MSG lpMsg, IntPtr hWnd, uint min, uint max);
  [DllImport("user32.dll")] public static extern bool TranslateMessage(ref MSG lpMsg);
  [DllImport("user32.dll")] public static extern IntPtr DispatchMessage(ref MSG lpMsg);
  [StructLayout(LayoutKind.Sequential)] public struct POINT { public int x; public int y; }
  [StructLayout(LayoutKind.Sequential)] public struct MSG { public IntPtr hWnd; public uint message; public UIntPtr wParam; public IntPtr lParam; public uint time; public POINT pt; }
}
'@

$root = $PSScriptRoot
$launcher = Get-Command py -ErrorAction SilentlyContinue
if ($launcher) {
    $python = $launcher.Source
    $pythonArgs = @('-3')
} else {
    $python = (Get-Command python -ErrorAction Stop).Source
    $pythonArgs = @()
}
$mods = 0x0002 -bor 0x0001 # CTRL + ALT
$keys = @{ 1 = 0x4D; 2 = 0x57; 3 = 0x53 } # M, W, S
$registered = @()
foreach ($entry in $keys.GetEnumerator()) {
    if ([MayaHotKeys]::RegisterHotKey([IntPtr]::Zero, $entry.Key, $mods, $entry.Value)) { $registered += $entry.Key }
}
if ($registered.Count -eq 0) { Write-Error 'Maya shortcuts are already in use or could not be registered.'; exit 1 }
Write-Host 'Maya shortcuts active: Ctrl+Alt+M launch/focus, Ctrl+Alt+W wake, Ctrl+Alt+S status.'
try {
    while ($true) {
        $msg = New-Object MayaHotKeys+MSG
        if ([MayaHotKeys]::GetMessage([ref]$msg, [IntPtr]::Zero, 0, 0) -le 0) { break }
        $id = [int]$msg.wParam
        switch ($id) {
            1 { Start-Process $python -ArgumentList ($pythonArgs + @((Join-Path $root 'maya_service.py'), 'wake')) -WorkingDirectory $root -WindowStyle Hidden; Start-Process $python -ArgumentList ($pythonArgs + @((Join-Path $root 'maya_app.py'))) -WorkingDirectory $root }
            2 { Start-Process $python -ArgumentList ($pythonArgs + @((Join-Path $root 'maya_service.py'), 'wake')) -WorkingDirectory $root -WindowStyle Hidden }
            3 { Start-Process $python -ArgumentList ($pythonArgs + @((Join-Path $root 'maya_service.py'), 'status')) -WorkingDirectory $root -NoNewWindow -Wait }
        }
        [MayaHotKeys]::TranslateMessage([ref]$msg) | Out-Null
        [MayaHotKeys]::DispatchMessage([ref]$msg) | Out-Null
    }
}
finally {
    foreach ($id in $registered) { [MayaHotKeys]::UnregisterHotKey([IntPtr]::Zero, $id) | Out-Null }
}
