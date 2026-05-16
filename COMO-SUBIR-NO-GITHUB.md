# Como subir este design system no GitHub

Guia passo a passo para criar o repositorio privado e fazer o primeiro push.

## Pre-requisitos

- Conta no GitHub (caso jamais tenha: github.com/signup, gratis)
- Git instalado no Windows
  - Verificar: abra PowerShell e digite `git --version`
  - Se jamais tem: baixe em https://git-scm.com/download/win e instale

## Passo 1 · Criar o repositorio no GitHub (web)

1. Va em [github.com/new](https://github.com/new)
2. **Repository name:** `fred-parreira-design-system`
3. **Description:** "Design System oficial da marca pessoal Fred Parreira"
4. Marque **Private** (privado)
5. **Jamais marque** "Initialize this repository with a README" (vamos enviar o nosso)
6. Click **Create repository**

GitHub vai te mostrar uma pagina com instrucoes. Pode ignorar, siga este guia.

## Passo 2 · Configurar git local (so na primeira vez)

Abra **PowerShell** ou **Git Bash** e configure seu nome e e-mail (uma unica vez):

```bash
git config --global user.name "Fred Parreira"
git config --global user.email "parreira.frederico@gmail.com"
```

## Passo 3 · Inicializar git e fazer o primeiro commit

No PowerShell ou Git Bash, navegue ate a pasta:

```bash
cd "C:\Users\parre\Downloads\Gustavo Novo - Carroseis\fred-parreira-design-system"
```

Inicialize git, adicione tudo, commit:

```bash
git init
git add .
git commit -m "feat: initial release of Fred Parreira Design System v1.0"
```

## Passo 4 · Conectar ao repositorio remoto e fazer push

Substitua `SEU-USER` pelo seu username do GitHub:

```bash
git branch -M main
git remote add origin https://github.com/SEU-USER/fred-parreira-design-system.git
git push -u origin main
```

Na primeira vez, o git vai te pedir login do GitHub. Recomendo usar um **Personal Access Token** ao inves da senha:

1. Em github.com, va em **Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. **Generate new token (classic)**
3. Da um nome ("design-system-push"), expira em 90 dias (ou no expiration), marca permissao **repo**
4. Copia o token (so aparece uma vez)
5. No prompt do git, cole o token quando ele pedir "Password"

## Passo 5 · Verificar

Va em `https://github.com/SEU-USER/fred-parreira-design-system` e veja se todos os arquivos subiram.

Pronto! Voce tem um design system versionado e privado no GitHub.

## Atualizar versoes futuras

Quando fizer mudancas:

```bash
cd "C:\Users\parre\Downloads\Gustavo Novo - Carroseis\fred-parreira-design-system"
git add .
git commit -m "feat: descricao da mudanca"
git push
```

E atualize o `CHANGELOG.md` antes do commit.

## Como compartilhar com outras pessoas (mantendo privado)

Em **Settings → Collaborators → Add people**, adicione o GitHub username de quem precisa ter acesso. Eles recebem convite por email.

## (Opcional) Ativar GitHub Pages no repo privado

GitHub Pages funciona de graca em repos **publicos**. Em repos **privados**, so funciona com GitHub Pro/Team (planos pagos).

Se voce migrar para Public no futuro:
1. **Settings → Pages**
2. **Source: Deploy from a branch**
3. **Branch: main / `/docs`**
4. Clica em **Save**

Em 1-2 minutos o brandbook ficara em:
`https://SEU-USER.github.io/fred-parreira-design-system/`

## Solucao de problemas comuns

**"Permission denied (publickey)"** → use HTTPS no `git remote add` (jamais SSH) ou configure uma chave SSH no GitHub.

**"Authentication failed"** → seu Personal Access Token expirou. Gere um novo.

**"Repository not found"** → verifique se o nome do repo no `git remote add` esta exato (incluindo SEU-USER correto).

**"Failed to push some refs"** → outro alguem (ou voce em outra maquina) ja fez push antes. Faca `git pull --rebase` primeiro, depois `git push`.
