#!/bin/bash
# ============================================================
#  archkj-dotfiles — First Time GitHub Setup
#  Run this ONCE to create the repo on GitHub and push
#  Requires: gh (GitHub CLI) — installs it if missing
#  Usage: bash setup-github.sh
# ============================================================

set -e

DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RED='\033[0;31m'
GREEN='\033[0;32m'
MAGENTA='\033[1;35m'
CYAN='\033[0;36m'
NC='\033[0m'

log()     { echo -e "${MAGENTA}[github]${NC} $1"; }
ok()      { echo -e "${GREEN}[✓]${NC} $1"; }
warn()    { echo -e "${RED}[!]${NC} $1"; }
section() { echo -e "\n${CYAN}══════════════════════════════${NC}\n${CYAN} $1${NC}\n${CYAN}══════════════════════════════${NC}"; }

# ── Install GitHub CLI ───────────────────────────────────────
section "GitHub CLI"

if ! command -v gh &>/dev/null; then
    log "Installing GitHub CLI (gh)..."
    sudo pacman -S --needed --noconfirm github-cli
    ok "gh installed"
else
    ok "gh already installed"
fi

# ── Authenticate ─────────────────────────────────────────────
section "GitHub Authentication"

if ! gh auth status &>/dev/null; then
    log "Logging in to GitHub..."
    gh auth login
    ok "Authenticated"
else
    ok "Already authenticated as $(gh api user --jq .login)"
fi

# ── Create Repo ──────────────────────────────────────────────
section "Creating GitHub Repository"

REPO_NAME="archkj-dotfiles"
GH_USER=$(gh api user --jq .login)

if gh repo view "$GH_USER/$REPO_NAME" &>/dev/null; then
    warn "Repo $GH_USER/$REPO_NAME already exists on GitHub"
else
    log "Creating public repo: $GH_USER/$REPO_NAME..."
    gh repo create "$REPO_NAME" \
        --public \
        --description "KJ's Arch Linux + Hyprland dotfiles — cyberpunk red/pink theme. Clone and run install.sh." \
        --homepage "https://github.com/$GH_USER/$REPO_NAME"
    ok "Repo created: https://github.com/$GH_USER/$REPO_NAME"
fi

# ── Init local git ───────────────────────────────────────────
section "Local Git Setup"

cd "$DOTFILES_DIR"

if [ ! -d ".git" ]; then
    git init
    git branch -M main
    ok "Git initialized"
fi

if ! git remote get-url origin &>/dev/null; then
    git remote add origin "https://github.com/$GH_USER/$REPO_NAME.git"
    ok "Remote set"
else
    ok "Remote: $(git remote get-url origin)"
fi

# ── Run collector ────────────────────────────────────────────
section "Running Collector"

bash "$DOTFILES_DIR/collect.sh"

# ── Done ─────────────────────────────────────────────────────
section "All Done!"

echo -e "${GREEN}Your dotfiles repo is live at:${NC}"
echo -e "${CYAN}https://github.com/$GH_USER/$REPO_NAME${NC}\n"
echo -e "To update in future, just run:"
echo -e "  ${CYAN}bash collect.sh${NC}"
echo ""
