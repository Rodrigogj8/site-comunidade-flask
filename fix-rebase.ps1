# Script para corrigir mensagens de commit
$rebaseFile = ".git/rebase-merge/git-rebase-todo"
if (Test-Path $rebaseFile) {
    $content = @"
reword 456b701 Atualizações no site Flask: melhorias no main.py, base.html e login.html
reword 5e1183f Atualizações no sistema de login e formulários
pick aa325c3 feat: Implementar sistema de formulários com Flask-WTF
pick a3b912b feat: Site de comunidade com Flask - versão inicial
"@
    [System.IO.File]::WriteAllText((Resolve-Path $rebaseFile), $content, [System.Text.Encoding]::UTF8)
}

