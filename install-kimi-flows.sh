#!/bin/bash
# DevFlow Flow Skills Installer for Kimi CLI
# Installs DevFlow flow skills to user's agents directory

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SOURCE="${SCRIPT_DIR}/.kimi/skills/devflow"

# Default: copy mode
USE_SYMLINK=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --symlink)
            USE_SYMLINK=true
            shift
            ;;
        --help|-h)
            echo "DevFlow Flow Skills Installer for Kimi CLI"
            echo ""
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --symlink    Create symlinks instead of copying (for development)"
            echo "  --help, -h   Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                    # Install by copying files"
            echo "  $0 --symlink          # Install using symlinks (auto-updates)"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Check if source directory exists
if [[ ! -d "${SKILLS_SOURCE}" ]]; then
    echo -e "${RED}Error: Skills source directory not found: ${SKILLS_SOURCE}${NC}"
    echo "Make sure you're running this script from the docutray-claude-code-plugins repository."
    exit 1
fi

# Detect user's skills directory (priority order from Kimi CLI docs)
detect_skills_dir() {
    local dirs=(
        "${HOME}/.config/agents/skills"
        "${HOME}/.agents/skills"
        "${HOME}/.kimi/skills"
        "${HOME}/.claude/skills"
        "${HOME}/.codex/skills"
    )
    
    for dir in "${dirs[@]}"; do
        if [[ -d "${dir}" ]]; then
            echo "${dir}"
            return
        fi
    done
    
    # Default to recommended location
    echo "${HOME}/.config/agents/skills"
}

SKILLS_DIR=$(detect_skills_dir)
TARGET_DIR="${SKILLS_DIR}/devflow"

echo -e "${BLUE}DevFlow Flow Skills Installer for Kimi CLI${NC}"
echo ""
echo -e "Source: ${SKILLS_SOURCE}"
echo -e "Target: ${TARGET_DIR}"
echo ""

# Create directory if needed
if [[ ! -d "${SKILLS_DIR}" ]]; then
    echo -e "${YELLOW}Creating skills directory: ${SKILLS_DIR}${NC}"
    mkdir -p "${SKILLS_DIR}"
fi

# Check if already exists
if [[ -d "${TARGET_DIR}" ]] || [[ -L "${TARGET_DIR}" ]]; then
    echo -e "${YELLOW}DevFlow skills already installed.${NC}"
    
    # Backup existing installation
    BACKUP_NAME="devflow.backup.$(date +%Y%m%d_%H%M%S)"
    BACKUP_PATH="${SKILLS_DIR}/${BACKUP_NAME}"
    
    echo -e "${YELLOW}Creating backup: ${BACKUP_PATH}${NC}"
    mv "${TARGET_DIR}" "${BACKUP_PATH}"
fi

# Install
if [[ "${USE_SYMLINK}" == true ]]; then
    echo -e "${BLUE}Installing with symlinks (development mode)...${NC}"
    ln -s "${SKILLS_SOURCE}" "${TARGET_DIR}"
    echo -e "${GREEN}✓ Symlinked DevFlow skills${NC}"
    echo ""
    echo -e "${YELLOW}Note: Changes to the repository will automatically reflect.${NC}"
    echo -e "${YELLOW}      To update: cd ${SCRIPT_DIR} && git pull${NC}"
else
    echo -e "${BLUE}Installing by copying files...${NC}"
    cp -r "${SKILLS_SOURCE}" "${TARGET_DIR}"
    echo -e "${GREEN}✓ Copied DevFlow skills${NC}"
    echo ""
    echo -e "${YELLOW}Note: To update, run this script again.${NC}"
fi

echo ""
echo -e "${GREEN}Installation complete!${NC}"
echo ""
echo "Installed flow skills:"
echo "  • /flow:devflow-feat       - Create feature specifications"
echo "  • /flow:devflow-dev        - Implement features"
echo "  • /flow:devflow-check      - Run validations"
echo "  • /flow:devflow-review-pr  - Review pull requests"
echo "  • /flow:devflow-research   - Research topics"
echo "  • /flow:devflow-epic       - Plan epics"
echo ""
echo "Usage:"
echo "  1. Start Kimi CLI: kimi"
echo "  2. Use any flow: /flow:devflow-feat"
echo ""
echo "Documentation:"
echo "  ${SCRIPT_DIR}/.kimi/skills/devflow/"
