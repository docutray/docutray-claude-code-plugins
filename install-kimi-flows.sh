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
SKILLS_SOURCE="${SCRIPT_DIR}/.kimi/skills"

# Skills to install
SKILLS=("devflow-dev" "devflow-feat" "devflow-check" "devflow-research" "devflow-epic" "devflow-review-pr")

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

# Target skills directory (Kimi CLI standard location)
SKILLS_DIR="${HOME}/.config/agents/skills"

echo -e "${BLUE}DevFlow Flow Skills Installer for Kimi CLI${NC}"
echo ""
echo -e "Source: ${SKILLS_SOURCE}"
echo -e "Target: ${SKILLS_DIR}"
echo ""

# Create directory if needed
if [[ ! -d "${SKILLS_DIR}" ]]; then
    echo -e "${YELLOW}Creating skills directory: ${SKILLS_DIR}${NC}"
    mkdir -p "${SKILLS_DIR}"
fi

# Install each skill
install_skill() {
    local skill_name="$1"
    local source_path="${SKILLS_SOURCE}/${skill_name}"
    local target_path="${SKILLS_DIR}/${skill_name}"
    
    # Check if source exists
    if [[ ! -d "${source_path}" ]]; then
        echo -e "${YELLOW}Warning: Skill source not found: ${skill_name}${NC}"
        return
    fi
    
    # Backup existing installation
    if [[ -d "${target_path}" ]] || [[ -L "${target_path}" ]]; then
        local backup_name="${skill_name}.backup.$(date +%Y%m%d_%H%M%S)"
        local backup_path="${SKILLS_DIR}/${backup_name}"
        
        echo -e "${YELLOW}  Backing up existing: ${skill_name}${NC}"
        mv "${target_path}" "${backup_path}"
    fi
    
    # Install
    if [[ "${USE_SYMLINK}" == true ]]; then
        ln -s "${source_path}" "${target_path}"
        echo -e "${GREEN}  ✓ ${skill_name} (symlinked)${NC}"
    else
        cp -r "${source_path}" "${target_path}"
        echo -e "${GREEN}  ✓ ${skill_name} (copied)${NC}"
    fi
}

# Install all skills
echo -e "${BLUE}Installing flow skills...${NC}"
for skill in "${SKILLS[@]}"; do
    install_skill "${skill}"
done

echo ""
if [[ "${USE_SYMLINK}" == true ]]; then
    echo -e "${YELLOW}Note: Changes to the repository will automatically reflect.${NC}"
    echo -e "${YELLOW}      To update: cd ${SCRIPT_DIR} && git pull${NC}"
else
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
echo "  ${SKILLS_SOURCE}/"
